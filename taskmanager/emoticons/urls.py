from django.urls import path
from .views import index


app_name = 'emoticons'
urlpatterns = [
    path('', index, name='index'),
    
]