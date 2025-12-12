from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core_app.dataclass import TodoDTO
from core_app.serializer.todo_request import TodoCreateRequestSerializer, TodoUpdateRequestSerializer

# In-memory storage for demonstration
TODO_LIST = []
TODO_ID_COUNTER = 1

class TodoListCreateAPIView(APIView):
    def get(self, request):
        # List all todos
        return Response([todo.__dict__ for todo in TODO_LIST])

    def post(self, request):
        serializer = TodoCreateRequestSerializer(data=request.data)
        if serializer.is_valid():
            global TODO_ID_COUNTER
            todo = serializer.to_dto()
            todo.id = TODO_ID_COUNTER  # Assign an ID
            TODO_ID_COUNTER += 1
            TODO_LIST.append(todo)
            return Response(todo.__dict__, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, todo_id):
        for todo in TODO_LIST:
            if todo.id == todo_id:
                return todo
        return None

    def get(self, request, todo_id):
        todo = self.get_object(todo_id)
        if not todo:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(todo.__dict__)

    def put(self, request, todo_id):
        todo = self.get_object(todo_id)
        if not todo:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoUpdateRequestSerializer(data=request.data)
        if serializer.is_valid():
            updated_todo = serializer.to_dto(todo)
            updated_todo.id = todo.id
            index = TODO_LIST.index(todo)
            TODO_LIST[index] = updated_todo
            return Response(updated_todo.__dict__)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id):
        todo = self.get_object(todo_id)
        if not todo:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        TODO_LIST.remove(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
