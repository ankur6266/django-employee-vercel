from django.shortcuts import render,redirect
from app2.models import Employees
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.
#  Fuction For read data from the database 
def Index(request):
    emp = Employees.objects.all()

    context={
        'emp': emp,
    }
    return render(request, 'index.html',context)

#  End Fuction For read data from the database 

# def ADD(request):
#     if request.method == "POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         address=request.POST.get('address')
#         phone=request.POST.get('phone')

#         emp = Employees(
#             name=name,
#             email=email,
#             address=address,
#             phone=phone
#         )
#         emp.save()
#         return redirect('index')
#     return render(request,'index.html')

# chatgpt code
# TO add employee details in database and show in website using get and post methods 
@csrf_exempt
def ADD(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        name = data["name"]
        email = data['email']
        address = data['address']
        phone = data['phone']

        # Check if the 'name' field is present and not empty
        if name:
            emp = Employees(
                name=name,
                email=email,
                address=address,
                phone=phone
            )
            emp.save()
            return HttpResponse({'Employee added successfully'})
            
        else:
            # Handle error when 'name' field is empty
            context = {
                'error_message': 'Name field is required.',
            }
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

# End TO add employee details in database and show in website using get and post methods 



#Edit funtion for 

def EDIT(request):
    emp = Employees.objects.all()
    context={
        'emp':emp,
    }
    return redirect(request,'index.html',context)

# End Edit function 

# update details for Emp 
# def UPDATE(request,id):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         address=request.POST.get('address')
#         phone=request.POST.get('phone')

#         emp = Employees(
#             id =id,        #if we do not use  id so it will add a new record 
#             name =name,
#             email=email,
#             address=address,
#             phone=phone
#         )
#         redirect('home')
#     return render(request,'index.html')

# chagpt code
def UPDATE(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp = Employees.objects.get(id=id)   #if we do not use  id so it will add a new record 
        emp.name = name
        emp.email = email
        emp.address = address
        emp.phone = phone
        emp.save()

        return redirect('home')
    else:
        emp = Employees.objects.get(id=id)
        return render(request,'index.html', {'emp': emp})
    
#  delete a employeed details    
# def DELETE(request,id):
#     emp=Employees.objects.filter(id=id)
#     emp.delete()   #you need to use id for delete particular data otherwise it will delte all the data 

#     context={
#         'emp':emp,
#     }

#     return redirect(request,'home')

def DELETE(request,id):
    emp = Employees.objects.get(id=id)
    emp.delete()
    return redirect('home')