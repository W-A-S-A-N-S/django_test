from django.urls import path
from . import views
app_name='accounts'

urlpatterns = [
    path('login/', views.my_login, name='my_login'),
    path('logout/', views.my_logout, name='my_logout'),
    path('signup/', views.my_signup, name='my_signup'),
]