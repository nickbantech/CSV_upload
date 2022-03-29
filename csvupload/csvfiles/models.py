from tkinter import CASCADE
from django.db import models
class State(models.Model):
    pass
    # state = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.state

class City(models.Model):
    pass
    # city = models.CharField(max_length=100)

    # def __self__(self):
    #     return self.city

class Student(models.Model):
    student_F_name = models.CharField(max_length=50)
    student_M_name = models.CharField(max_length=50)
    student_L_name = models.CharField(max_length=50)
    student_state = models.CharField(max_length=50)
    student_city = models.CharField(max_length=50)

    def __str__(self):
        return self.student_F_name











