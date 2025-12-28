# Ex01 Django ORM Web Application
## Date: 15.11.2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Employee, EmployeeAdmin

admin.site.register(Employee, EmployeeAdmin)

models.py
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

```
## OUTPUT
![alt text](<orm output1.png>)

![alt text](<orm output.png>)

## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
