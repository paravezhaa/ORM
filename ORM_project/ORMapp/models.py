from django.db import models
from django.contrib import admin

class Employee(models.Model):
    e_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'e_id',
        'name',
        'salary',
        'age',
        'email',
    )


