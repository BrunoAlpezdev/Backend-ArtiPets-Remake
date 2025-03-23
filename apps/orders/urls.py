from django.urls import path
from . import views
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Funciona!"})

urlpatterns = [
    path('test/', test_view, name='test_view'),
]