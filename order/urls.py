from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list-view'),
    path('create/', views.OrderCreateView.as_view(), name='order-create-view'),
    path('<pk>/', views.OrderDetailView.as_view(), name='order-detail-view'),
]
