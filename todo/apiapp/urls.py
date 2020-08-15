from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('task-list/',views.taskList,name='task-list'),
    path('detail-task/<str:id>/',views.detailView,name='detail-list'),
    path('create-task/',views.createTask,name='create-task'),
    path('update-task/<str:id>/',views.updateTask,name='update-task'),
    path('delete-task/<str:id>/',views.deleteTask,name='delete-task'),
]