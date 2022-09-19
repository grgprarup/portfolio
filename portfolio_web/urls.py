from django.urls import path
from portfolio_web import views

app_name = 'portfolio_web'

urlpatterns = [
    path('', views.index, name='index'),
]
