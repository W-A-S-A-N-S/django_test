from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # path('', views.good, name='home'),
    path('', views.index, name='index'),
    path('sans', views.sans, name='sans'),
    path('papyrus', views.papyrus, name='papyrus'),
    path('memo/', views.memo_list, name='memo_list'),
    path('my_memo/', views.my_memo_list, name='my_memo_list'),
    path('memo/create/', views.memo_create, name='memo_create'),
    path('<int:pk>/', views.memo_detail, name='memo_detail'),
    path('<int:pk>/update/', views.memo_update, name='memo_update'),
    path('<int:pk>/delete/', views.memo_delete, name='memo_delete'),
    path('memo/<int:memo_id>', views.one_memo, name='one_memo'),
    path('art_create', views.art_create, name='art_create'),
    # path('hello/', views.hello, name='hello'),
    # path('lion/<str:name>/', views.lion, name='lion'),
    # path('good/', views.good, name='good'),
    # path('moon/', views.moon, name='moon'),
    # path('add/<int:num1>/<int:num2>/', views.add),
    # path('multiply/<int:num1>/<int:num2>/', views.multiply),
    #path('memo/stats/', views.memo_stats, name='memo_stats'),
]
