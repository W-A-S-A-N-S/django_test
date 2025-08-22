from django.urls import path
from . import views

urlpatterns = [
    # path('', views.good, name='home'),
    path('', views.hello, name='hello'),
    path('hello/', views.hello, name='hello'),
    path('lion/<str:name>/', views.lion, name='lion'),
    path('good/', views.good, name='good'),
    path('moon/', views.moon, name='moon'),
    path('add/<int:num1>/<int:num2>/', views.add),
    path('multiply/<int:num1>/<int:num2>/', views.multiply),
    path('memo/', views.memo_list, name='memo_list'),
    path('memo/<int:memo_id>', views.one_memo, name='one_memo'),
    #path('memo/stats/', views.memo_stats, name='memo_stats'),
]
