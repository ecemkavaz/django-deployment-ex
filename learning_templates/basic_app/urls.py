from django.urls import path
from basic_app import views

# Template tagging
app_name = 'my_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),


]
