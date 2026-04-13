from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('', views.listings, name='listings'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/mark-sold/', views.mark_sold, name='mark_sold'),
]
