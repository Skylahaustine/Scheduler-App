from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView

)

urlpatterns=[
    path('', TaskListView.as_view(), name= 'task_list'),
    path('new/',TaskCreateView.as_view(), name='task_new'),
    path('<int:pk>/delete/',
        TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/edit/',
        TaskUpdateView.as_view(), name='task_edit')

]