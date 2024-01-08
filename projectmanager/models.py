from django.db import models


class Project(models.Model):
    title = models.CharField('Название  проекта', max_length=50)
    description = models.TextField('Описание проекта')
    project_manager = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name='Рукводитель')
    is_active = models.BooleanField('Состояние активности', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('progress', 'В работе'),
        ('closed', 'Закрыта')
    ]
    title = models.CharField('Название задачи', max_length=255)
    deadline = models.DateField('Срок исполнения')
    description = models.TextField('Описание задачи')
    status = models.CharField('Статус задачи', choices=STATUS_CHOICES, max_length=10, default='new')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект')
    employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.title}'

    def task_status(self):
        return self.get_status_display()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Employee(models.Model):
    last_name = models.CharField('Фамилия', max_length=20)
    first_name = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=25, blank=True)
    job_title = models.CharField('Должность', max_length=50)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Comment(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, verbose_name='Задача')
    text = models.TextField('Текст комментария')
    created_date = models.DateField(auto_now_add=True)
