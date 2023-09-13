from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('template/', views.template, name='template'),
    path('billing/', views.billing, name='billing'),
    path('notifications/', views.notifications, name='notifications'),
    path('tables', views.tables, name='tables'),
    path('map', views.map, name='map'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout')
]
