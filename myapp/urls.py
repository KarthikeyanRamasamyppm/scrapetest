from django.urls import path
from .views import login_view, ProductListView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('products/', ProductListView.as_view(), name='products'),
]