
from django.urls import path
from .import views

urlpatterns = [
    path('',views.todoadd,name='todoadd'),
    # path('detail/',views.detail,name='detail'),
    path('delet/<int:taskid>/',views.delet,name='delet'),
    path('update/<int:id>/',views.update,name='update'),
    path('tasklist/',views.tasklist.as_view(),name='tasklist'),
    path('taskdetail/<int:pk>/',views.taskdetail.as_view(),name='taskdetail'),
    path('taskupdate/<int:pk>/',views.taskupdate.as_view(),name='taskupdate'),
    path('taskdelet /<int:pk>/',views.taskdelet .as_view(),name='taskdelet '),
] 