from django.contrib import admin
from django.urls import path, include

import fscohort
# from fscohort.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view, name='home'),
    path('', include("fscohort.urls")),
]
