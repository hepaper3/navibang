from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('profile_info>', views.show_profile, name="show_profile"),
]
