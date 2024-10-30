from django.db import models
from rest_framework.exceptions import ValidationError


class UserModel(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.username

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError('Passwords do not match')
        super().clean()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
