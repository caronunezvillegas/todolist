from django.urls import path
from .views import delete_task, list_tasks, create_task, edit_task, login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('list_tasks/', list_tasks, name='tasks'),
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('', logout_view, name='logout'),
]
