from . import views
from django.urls import path


urlpatterns = [
    path('', views.demo, name='demo')
    #path('mathoperations/', views.mathoperations, name='mathoperations')
]

