
from django.urls import path
from .views import my_view,generate

urlpatterns = [
    path('', my_view),
    path('generate/', generate, name='generate'),
]