from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='homepage'),
    path('create', views.post_create),
    path('<slug:id>/edit', views.post_update, name='update'),
    path('<slug:id>/delete', views.post_delete, name='delete'),
    path('<slug:id>', views.post_detail, name='detail'),
]
