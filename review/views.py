from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import analyze_code
from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult

class TaskStatusView(APIView):
    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        if task_result.state == 'SUCCESS':
            return Response({'state': task_result.state, 'result': task_result.result})
        return Response({'state': task_result.state})
class CodeAnalysisView(APIView):
    def post(self, request):
        code_url = request.data.get('code_url')
        if code_url:
            task = analyze_code.delay(code_url)
            return Response({'task_id': task.id, 'status': 'Code analysis started'}, status=202)
        return Response({'error': 'No code provided'}, status=400)