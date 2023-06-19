from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('afisha/', PerformanceHome.as_view(), name='afisha'),
    path('afisha/filter/', FiterPerformance.as_view(), name='filter'),
    path('repertuar/', repertuar, name='repertuar'),
    path('performance/<slug:performance_slug>/', ShowPerformance.as_view(), name='performance'),
    path('repertuar/<slug:category_slug>/', PerfromanceCategory.as_view(), name='pcategory'),
    path('addpage/', AddPerformance.as_view(), name='add_page'),
]