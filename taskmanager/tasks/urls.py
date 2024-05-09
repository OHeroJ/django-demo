from django.urls import path
from django.views.generic import TemplateView
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView)

app_name = 'tasks' # 域名空间
urlpatterns = [
    path("", TemplateView.as_view(template_name="tasks/home.html"), name="home"),
    path("help/", TemplateView.as_view(template_name="tasks/help.html"), name="help"),
    path("tasks/", TaskListView.as_view(), name="task-list"),  # GET
    path("tasks/new/", TaskCreateView.as_view(), name="task-create"),  # POST
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),  # GET
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task-update"),  # PUT/PATCH
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),  # DELETE
]