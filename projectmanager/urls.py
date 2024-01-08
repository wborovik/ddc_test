from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>', views.show_project, name='project'),
    path('task/<int:task_id>', views.show_task, name='task'),
    path('task/<int:task_id>/<int:comment_id>', views.show_task, name='comment'),
    path('delete_comment/<int:task_id>/<int:comment_id>', views.delete_comment, name='delete_comment')
]
