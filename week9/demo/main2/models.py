from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class StudentManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Student(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = StudentManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('main2:student_list')


class Comment(models.Model):
    text = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text
