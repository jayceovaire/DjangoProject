from django.shortcuts import render
from rest_framework import status

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_task(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['PUT'])
def update_task(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error":"Task does not exist"})

    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error":"Task does not exist"})
    task.delete()

    return Response({"message":"Task deleted"})


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

