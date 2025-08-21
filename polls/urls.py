from django.urls import path
from . import views

urlpatterns = [
    # path('', views.good, name='home'),
    path('hello/', views.hello, name='hello'),
    path('lion/<str:name>/', views.lion, name='lion'),
    path('good/', views.good, name='good'),
    path('moon/', views.moon, name='moon'),
]
