from django.urls import path
from .views import home_view, student_list, student_add

urlpatterns = [
    path('', home_view),
    # path('about', about, name='about'),
    path('list/', student_list),
    path('add/', student_add),
]

