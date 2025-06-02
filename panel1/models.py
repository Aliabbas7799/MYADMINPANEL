from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=70, blank=True, null=True)
    email     = models.EmailField(unique=False, null=False)
    role      = models.CharField(max_length=30, default="User")
    status    = models.CharField(max_length=30, default="Active")
      

 
    def __str__(self):
        return self.user_name
 
 
class Task(models.Model):
    task_title       = models.CharField(max_length=70, blank=True, null=True)
    task_description = models.TextField(blank=True, null=True)
    status           = models.CharField(max_length=30, default="Pending")
    created_at       = models.DateTimeField(auto_now_add=True)
    is_deleted          = models.BooleanField(default=False)   
    updated_at          = models.DateTimeField(auto_now=True)
    assigned_to      = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
 
    def __str__(self):
        return self.task_title