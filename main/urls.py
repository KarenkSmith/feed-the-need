from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   # path('feeds/', views.feeds, name='feeds'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/signup', views.signup, name='signup'),
   path('user/<int:user_id>/', views.profile, name='profile'),
]