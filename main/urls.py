from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   # path('feeds/', views.feeds, name='feeds'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/signup', views.signup, name='signup'),
   path('user/<int:profile_id>/', views.profile, name='profile'),
   path('user/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
   path('user/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
   # path('user/create/', views.ProfileCreate.as_view(), name='profile_create'),
   path('user/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
   path('additems/', views.AddItems.as_view(), name='add_items'),
]