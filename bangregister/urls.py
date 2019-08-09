from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('show/<int:roompost_id>', views.show, name='show'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('roomupdate/<int:roompost_id>', views.roomupdate, name='roomupdate'),
    path('delete/<int:roompost_id>', views.delete, name='delete'),
    path('scrap/<int:roompost_id>', views.scrap, name='scrap'),
    path('like/<int:roompost_id>', views.like, name='like'),
    path('result/', views.result, name='result'),
    path('commentcreate/<int:roompost_id>', views.commentcreate, name='commentcreate'),

]
