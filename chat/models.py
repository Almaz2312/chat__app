from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User)


class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    send_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)