from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    vendor = models.CharField(max_length=40, blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length=5, choices=(('grams', 'Grams'), ('kg', 'KiloGrams'),))

    def __str__(self):
        return f"{self.name} "


class Category(models.Model):
    name = models.CharField(max_length=20)


class Notification(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('broadcast', 'Broadcast'),
        ('individual', 'Individual'),
    ]

    message = models.TextField()
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.message

class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.notification.message}'