from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
from emp_app.models import Employee

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        result=[{"name":e.name,"department":e.department,"salary":e.salary,"location":e.location,"experience":e.experience,"age":e.age,"email":e.email,"phone":e.phone} for e in qs]

        return JsonResponse({"data":result,"status":"200 ok"})

    def post(self,request,*args,**kwargs):

        data=loads(request.body)

        Employee.objects.create(name=data.get("name"),department=data.get("department"),salary=data.get("salary"),location=data.get("location"),experience=data.get("experience"),age=data.get("age"),email=data.get("email"),phone=data.get("phone"))

        return JsonResponse({"data":"record inserted","status":"201 created"})

        