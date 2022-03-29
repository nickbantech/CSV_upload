from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models



    
class State_1(models.Model):
    state = models.CharField(max_length=100,blank=False, null=False,)

    
    def __str__(self):
        return self.state

class City_1(models.Model):
    city = models.CharField(max_length=100,blank=False, null=False)

    def __str__(self):
        return self.city

class Student_1(models.Model):
    gender_choice = (("Male","Male"),
                    ("Female","Female")
    )
    student_F_name = models.CharField(max_length=50,blank=False, null=False)
    student_M_name = models.CharField(max_length=50,blank=False, null=False)
    student_L_name = models.CharField(max_length=50,blank=False, null=False)
    student_state = models.ForeignKey(State_1,on_delete=models.CASCADE)
    student_city = models.ForeignKey(City_1,on_delete=models.CASCADE)
    student_gender = models.CharField(max_length = 10,choices=gender_choice)
        
    def __str__(self):
        return self.student_F_name











