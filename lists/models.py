from django.db import models
from django.utils.timezone import now

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    task_text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority_level = models.IntegerField()
    def toggle_completion(self):
        """track when tasks have been completed and update timestamp"""
        self.completed = not self.completed
        self.completed_at = now() if self.completed else None
        self.save()

    def __str__(self):
        return self.title