from django.urls import path
from .import views
urlpatterns = [
    path('', views.Homeview),
    path('detail/<str:pk>', views.detailview, name='detail'),
    path('CreateView', views.CreateView, name='create'),
    path('UpdateView/<str:pk>', views.UpdateView, name='update'),
    path('deleteView/<str:pk>', views. deleteView, name='delete')
]
