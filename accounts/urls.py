from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('profile_info', views.show_profile, name="show_profile"),
    path('signup_complete', views.signup_complete, name="signup_complete"),
    path('my_scrap', views.my_scrap, name='my_scrap'),
    path('my_post', views.my_post, name='my_post'),
]
