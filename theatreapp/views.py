from random import randint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from .utils import *
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages
from datetime import date
from .forms import *
from robokassa.forms import RobokassaForm


def pay_with_robokassa(request):
    rand = randint(5000, 5500)
    form = RobokassaForm(initial={
        'OutSum': 100,
        'InvId': rand,
        'Desc': request.user.username,
        # 'Email': 'request.user.email',
    })
    return render(request, 'pay_with_robokassa.html', {'form': form})

def index(request):
    form = GetEmail()
    if request.method == 'POST':
        form = GetEmail(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'text': form.cleaned_data['text'],
            }
            html_body = render_to_string('email.html', data)
            msg = EmailMultiAlternatives(subject='Вопрос от пользователя блога', to=['lyblygambit@yandex.ru'])
            msg.attach_alternative(html_body, 'text/html')
            msg.send()
            print('good')
        return redirect('/')
    return render(request, 'index.html', {'form': form, 'title': 'Обратная связь'})

def repertuar(request):
    category = Category.objects.all()
    context = {
        'category': category,
        'title': 'Репертуар',
    }
    return render(request, 'repertuar.html', context)

class GenreDate:

    def get_genres(self):
        return Genre.objects.all()

    def get_date(self):
        lst = list()
        dct = Performance.objects.all().values('date')
        for i in dct:
            for n in i.values():
                lst.append(str(n))
        final = set(lst)
        return final

class PerfromanceCategory(DataMixin, GenreDate, ListView):
    model = Performance
    template_name = 'pcategory.html'
    context_object_name = 'pcategory'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Performance.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).select_related('category')

class PerformanceHome(DataMixin, GenreDate, ListView):
    model = Performance
    template_name = 'afisha.html'
    context_object_name = 'performances'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Афиша')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Performance.objects.filter(is_published=True).select_related('category')

class ShowPerformance(DataMixin, DetailView, GenreDate):
    model = Performance
    template_name = 'performance.html'
    slug_url_kwarg = 'performance_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        seance = Performance.objects.get(slug=self.kwargs['performance_slug'])
        tickets = Ticket.objects.filter(seance=seance)
        context = super().get_context_data()
        p = Performance.objects.get(slug=self.kwargs['performance_slug'])
        context.update(dict(tickets=tickets, title=f'{str(p.name)}'))
        return context

    def post(self, request, *args, **kwargs):
        seance = Performance.objects.get(slug=self.kwargs['performance_slug'])
        if seance.date == date.today():
            messages.error(request, 'Извините, но это мероприятие уже прошло')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            for key, value in request.POST.items():
                if key.startswith('seat'):
                    row, seat = key.split('-')[-2:]
                    ticket_check = Ticket.objects.filter(seance=seance, row=row, seat=seat)
                    if seance.seats == 0:
                        messages.error(request, 'Извините, все места на это мероприятие заняты!')
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    elif ticket_check:
                        messages.error(request, 'Сиденье %s в ряде %s уже занято! Пожалуйста, выберите другое место!' % (seat, row))
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    else:
                        ticket = Ticket(seance=seance, row=row, seat=seat)
                        ticket.save()
                        data = {
                            'seance': ticket.seance,
                            'hall': seance.hall,
                            'row': ticket.row,
                            'seat': ticket.seat,
                        }
                        html_body = render_to_string('email_ticket.html', data)
                        msg = EmailMultiAlternatives(subject=f'Билет на представление {data["seance"]}', to=['lyblygambit@yandex.ru'])
                        msg.attach_alternative(html_body, 'text/html')
                        msg.send()
                        print('good')
                        seance.seats -= 1
                        seance.save()
                        return pay_with_robokassa(request)

class FiterPerformance(PerformanceHome, GenreDate, ListView):
    def get_queryset(self):
        queryset = Performance.objects.filter(
            Q(date__in=self.request.GET.getlist('date')) &
            Q(genre__in=self.request.GET.getlist('genre'))
        )
        return queryset

class AddPerformance(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPerformance
    template_name = 'addpage.html'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание мероприятия')
        return dict(list(context.items()) + list(c_def.items()))



