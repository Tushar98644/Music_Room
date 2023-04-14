from django.contrib import admin
from django.urls import path, include
from .views import tushar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tushar',tushar),
]