from core_app.models import Todo

def create_todo(dc):
    todo = Todo.objects.create(
        title=dc.title,
        description=dc.description,
        is_completed=dc.is_completed
    )
    return todo


def list_todos():
    return Todo.objects.all()


def get_todo(id):
    return Todo.objects.get(id=id)


def update_todo(id, dc):
    todo = Todo.objects.get(id=id)
    todo.title = dc.title
    todo.description = dc.description
    todo.is_completed = dc.is_completed
    todo.save()
    return todo


def delete_todo(id):
    todo = Todo.objects.get(id=id)
    todo.delete()
