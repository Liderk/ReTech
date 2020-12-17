from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name='company')

    def __str__(self):
        return self.name


class Task(models.Model):
    """a simple model of the ToDo list."""
    name = models.CharField(max_length=250)
    task = models.TextField(blank=True, null=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='task'
    )

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    companies = models.ManyToManyField(Company, blank=True)
    company_access = models.CharField(max_length=250, blank=True, null=True)
