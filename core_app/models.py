from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def get_all_todos():
    return Todo.objects.all()


def create_todo(data):
    return Todo.objects.create(**data)


def get_todo(id):
    return Todo.objects.get(pk=id)


def update_todo(id, data):
    todo = Todo.objects.get(pk=id)
    for key, value in data.items():
        setattr(todo, key, value)
    todo.save()
    return todo


def delete_todo(id):
    Todo.objects.get(pk=id).delete()
