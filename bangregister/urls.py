from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('show/<int:room_id>', views.show, name='show'),
    path('register/', views.register, name='register'),
]
