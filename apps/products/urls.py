from django.urls import path
from . import views
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Funciona!"})

urlpatterns = [
    path('test/', test_view, name='test_view'),
]

"""
urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
]
"""