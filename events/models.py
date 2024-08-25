from django.db import models
from django.conf import settings

from django.utils import timezone
from django.core.exceptions import ValidationError

class Event(models.Model):
    EVENT_STATUS = {
        ("Pending", "Pending"),
        ("Conducted", "Conducted"),
        ("Cancelled", "Cancelled")
    }

    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=EVENT_STATUS, default="Pending")
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user.email}"

    def save(self, *args, **kwargs):
        if self.date < timezone.now():
            raise ValidationError("The event date cannot be in the past.")
        super().save(*args, **kwargs)
