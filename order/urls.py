from django.urls import path
from . import views

urlpatterns = [
    path('<pk>/', views.OrderDetailView.as_view(), name='order-detail-view'),
    path('', views.OrderCreateView.as_view(), name='order-create-view'),
    path('', views.OrderListView.as_view(), name='order-list-view'),
]
