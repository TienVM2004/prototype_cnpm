from django.urls import path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.home_view, name = 'home'), 
    path('view_1/', views.view_1, name = 'view_1'), 
    # path('<int:id>/', views.sub_view_2, name = 'view_2'),
    # path('<int:id>/', views.sub_view_3, name = 'view_3'),
]