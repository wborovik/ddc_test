from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddCommentForm
from .models import Project, Task, Comment


def index(request):
    data = {
        'projects': Project.objects.all()
    }
    return render(request, 'projectmanager/index.html', data)


def show_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    data = {
        'title': project.title,
        'status': 'Статус проекта',
        'project': project,
        'tasks': project.task_set.all()
    }
    return render(request, 'projectmanager/project.html', data)


def show_task(request, task_id, comment_id=None):
    form = AddCommentForm()
    task = get_object_or_404(Task, id=task_id)

    if comment_id:
        comment = get_object_or_404(Comment, id=comment_id)
        form = AddCommentForm(data=(request.POST or None), instance=comment)
    if request.method == 'POST':
        return update_or_create_comment(request, task, comment_id)

    data = {
        'task_id': task.id,
        'title': task.title,
        'project': task.project.title,
        'project_id': task.project_id,
        'employee': task.employee,
        'description': task.description,
        'status': task.get_status_display,
        'deadline': task.deadline,
        'comments': task.comment_set.all().order_by('-id'),
        'form': form
    }
    return render(request, 'projectmanager/task.html', data)


def update_or_create_comment(request, task, comment_id=None):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        comment = form.save(commit=False)
        values_for_update = {
            'text': comment.text,
            'task': task
        }
        if form.is_valid():
            Comment.objects.update_or_create(id=comment_id, defaults=values_for_update)
        else:
            form.add_error(None, 'Ошибка при добавлении комментария')

    return redirect('task', task.id)


def delete_comment(request, task_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()

    return redirect('task', task_id)
