from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

# Create your views here.
def employees(request):
   employees = Employee.objects.all()
   return HttpResponse(employees.values())