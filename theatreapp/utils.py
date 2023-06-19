from .models import *


menu = [{'title': 'Главная страница'}]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        u_menu = menu.copy()
        context['menu'] = u_menu
        return context