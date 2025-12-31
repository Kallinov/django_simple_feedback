from django.db import models

class Status(models.TextChoices): # Enum for status in FeedBack model
    NEW = 'new', 'Новый'
    IN_PROGRESS = 'in_progress', 'В работе'
    CLOSED = 'closed', 'Просмотрен'  