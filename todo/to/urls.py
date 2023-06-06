from django.urls import path
from .import views
urlpatterns = [
    path('', views.Homeview),
    path('detail/<str:pk>', views.detailview, name='detail')
]
