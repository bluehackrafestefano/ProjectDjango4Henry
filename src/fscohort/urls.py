from django.urls import path
from .views import home_view, student_detail, student_list, student_add

urlpatterns = [
    path('', home_view, name='home'),
    # path('about', about, name='about'),
    path('list/', student_list, name='list'),
    path('add/', student_add, name='add'),
    path('<int:id>', student_detail, name='detail'),
]

