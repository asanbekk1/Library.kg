from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    EDUCATION = (
        ('HS', 'High School'),
        ('B', 'Bachelor'),
        ('M', 'Master'),
        ('P', 'PhD'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    experience = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Определяем зарплату
        if self.experience < 1:
            self.salary = 30000
        elif 1 <= self.experience < 3:
            self.salary = 50000
        elif 3 <= self.experience < 5:
            self.salary = 70000
        elif 5 <= self.experience < 7:
            self.salary = 100000
        else: self.experience = 'Вы слишком опытны, вам это покажется скучным'


        super().save(*args, **kwargs)