from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)


class Task(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(default="")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=3)  # 1: High, 2: Medium, 3: Low
    status = models.IntegerField(default=0)  # 0: To Do, 1: In Progress, 2: Done
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
