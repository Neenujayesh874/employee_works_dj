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

        result=[{"id":e.id,"name":e.name,"department":e.department,"salary":e.salary,"location":e.location,"experience":e.experience,"age":e.age,"email":e.email,"phone":e.phone} for e in qs]

        return JsonResponse({"data":result,"status":"200 ok"})

    def post(self,request,*args,**kwargs):

        data=loads(request.body)

        Employee.objects.create(**data)

        return JsonResponse({"message":"record inserted","status":"201 created"})


@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        result={"id":qs.id,"name":qs.name,"department":qs.department,"salary":qs.salary,"location":qs.location,"experience":qs.experience,"age":qs.age,"email":qs.email,"phone":qs.phone}

        return JsonResponse({"data":result,"status":"200 ok"})
    
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data=loads(request.body)

        Employee.objects.filter(id=id).update(**data)

        return JsonResponse({"message":"record updated","status":"200 ok"})
    
    def delete(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return JsonResponse({"message":"record deleted","status":"200 ok"})