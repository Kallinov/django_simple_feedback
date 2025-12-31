from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from .enums import Status

valid_status = [choice[0] for choice in Status.choices]

class FeedBack(models.Model):
    email = models.EmailField(null=True)
    message = models.CharField()
    status = models.CharField(choices=Status.choices,
    default=Status.NEW)


    def clean(self): # Python-level validation
        if self.status not in valid_status:
            raise ValidationError('Status "{self.status}" is invalid')
        return super().clean()
    
    def save(self):
        self.full_clean()
        return super().save()

    def __str__(self):
        return f'Email: {self.email}; Message: {self.message}; Status: {self.status}'
    
    class Meta: # Database-level validation
        constraints = [
            models.CheckConstraint(
                condition=Q(status__in=valid_status),
                name='validate_values'
            )
        ]