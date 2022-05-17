from .import views
from django.urls import path
urlpatterns = [
path('top10',views.Top10, name='top10'),
]