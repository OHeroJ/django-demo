from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Epic(models.Model):
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name="created_epics", on_delete=models.CASCADE)
    

class Task(models.Model):
    STATUS_CHOICES = [
        ("UNASSINGNED", "Unassigned"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Completed"),
        ("ARCHIVED", "Archived"),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False, default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="UNASSIGNED", db_comment="Can be UNASSIGNED, IN_PROGRESS, DONE, ARCHIVED")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 我们将该值设置为cascade，这将删除任务
    creator = models.ForeignKey(User, related_name="createed_tasks", on_delete=models.CASCADE)
    # 当所有者对象被删除时，所有者被设置为null以防止删除Task对象
    owner = models.ForeignKey(User, related_name="owned_tasks", on_delete=models.SET_NULL, null=True, db_comment="Foreign Key to the User who currently owns the task")
    epic = models.ForeignKey(Epic, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table_comment = "Holds information about tasks"
        
        
class Sprint(models.Model):
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name="created_sprints", on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, related_name='sprints', blank=True)
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(end_date__gt=models.F('start_date')), name='end_date_after_start_date'),
        ]
    
    

        
        
