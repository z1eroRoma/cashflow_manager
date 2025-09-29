from django.urls import path
from .views import CashFlowListView, CashFlowCreateView, CashFlowUpdateView, CashFlowDeleteView, GetSubcategories

app_name = 'cashflow'

urlpatterns = [
    path('', CashFlowListView.as_view(), name='list'),
    path('create/', CashFlowCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', CashFlowUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CashFlowDeleteView.as_view(), name='delete'),
    path('api/subcategories/', GetSubcategories.as_view(), name='get_subcategories'),
]
