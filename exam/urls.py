from django.urls import path
from .views import home_page, single_page

urlpatterns = [
    path('', home_page, name='home'),
    path('post/<int:pk>/', single_page, name='single'), 
]
