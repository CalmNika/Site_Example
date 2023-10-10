from django.http import JsonResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    task_data = [{'title': task.title, 'description': task.description, 'created_at': task.created_at, 'updated_at': task.updated_at} for task in tasks]

    return JsonResponse({'tasks': task_data})