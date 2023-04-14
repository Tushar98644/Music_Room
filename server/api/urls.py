from django.urls import path
from .views import Roomview , CreateRoomview

urlpatterns = [
      path('',Roomview.as_view()),
      path('create',CreateRoomview.as_view()),
]