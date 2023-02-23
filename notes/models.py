from django.conf import settings
from django.contrib import admin
from django.db import models

# Create your models here


class Author(models.Model):
    NOTER_BRONZE = 'B'
    NOTER_SILVER = 'S'
    NOTER_GOLD = 'G'

    NOTE_LEVELS = [
        (NOTER_BRONZE, 'Bronze'),
        (NOTER_SILVER, 'Silver'),
        (NOTER_GOLD, 'Gold'),
    ]
    nickname = models.CharField(max_length=128, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    tier = models.CharField(
        max_length=1, choices=NOTE_LEVELS, default=NOTER_BRONZE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nickname}' if self.nickname else f'{self.user.first_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']



class Note(models.Model):
    entry = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, related_name=("notes"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.entry
