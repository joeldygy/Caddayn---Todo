from rest_framework import serializers
from core_app.todo.dataclass import TodoDTO

class TodoResponseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    is_completed = serializers.BooleanField()

    @staticmethod
    def from_dto(todo_dto: TodoDTO):
        return {
            "title": todo_dto.title,
            "description": todo_dto.description,
            "is_completed": todo_dto.is_completed
        }