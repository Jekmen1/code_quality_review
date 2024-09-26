from django.urls import path
from .views import CodeAnalysisView, TaskStatusView

urlpatterns = [
    path('analyze/', CodeAnalysisView.as_view(), name='code_analyze'),
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),
]