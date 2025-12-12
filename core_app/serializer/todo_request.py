from rest_framework import serializers
from core_app.dataclass import TodoDTO


class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
    is_completed = serializers.BooleanField(default=False)

    def to_dto(self):
        return TodoDTO(
            title=self.validated_data.get("title"),
            description=self.validated_data.get("description", ""),
            is_completed=self.validated_data.get("is_completed", False)
        )


class TodoUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
    is_completed = serializers.BooleanField()

    def to_dto(self, existing):
        return TodoDTO(
            title=self.validated_data.get("title", existing.title),
            description=self.validated_data.get("description", existing.description),
            is_completed=self.validated_data.get("is_completed", existing.is_completed),
        )

