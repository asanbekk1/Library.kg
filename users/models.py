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

    # Дополнительные поля
    phone = models.CharField(max_length=15, default='+996', blank=True, null=True)
    age = models.PositiveIntegerField(default=18, blank=True, null=True)  # Измените значение по умолчанию, если нужно
    gender = models.CharField(max_length=1, choices=GENDER, default='M', blank=True, null=True)
    education = models.CharField(max_length=2, choices=EDUCATION, default='HS', blank=True, null=True)
    experience = models.IntegerField(default=0)  # Опыт работы в годах
    salary = models.IntegerField(blank=True, null=True)  # Добавлено поле salary

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
        else:
            self.salary = 150000

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username