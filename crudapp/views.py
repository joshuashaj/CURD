from django.shortcuts import render,redirect
from crudapp.forms import EmployeeForm
from crudapp.models import Employee

# Create your views here.
def index(request):
    employee = Employee.objects.all()
    return render(request,'index.html',{'employee':employee})

def add(request):
    if request.method == "POST":
        empform =EmployeeForm(request.POST)
        if empform.is_valid():
            try:
                empform.save()
                return redirect('/')
            except:
                pass
    else:
        empform = EmployeeForm
    return render(request,'add.html',{'empform':empform})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    empform = EmployeeForm(request.POST,instance=employee)
    if empform.is_valid():
            try:
                empform.save()
                return redirect('/')
            except:
                pass
    return render(request, 'edit.html', {'employee': employee})

def destroy(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')