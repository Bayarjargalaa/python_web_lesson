from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from lesson_app.models import Task

def index(request):
    # tasks_list=Task.objects.all()
    # output="; ".join(f"{t.title}: {t.text}" for t in tasks_list)
    
    # if not output:
    #     output="There are no created tasks!"
    # return HttpResponse(output)
    
    return HttpResponse("Deparment Details page")
def view_department(request, task_id):
    if task_id==1:
        task_name="Developers"
    elif task_id==2:
        task_name="Trainers"
    html_output=f"<html><body><h1>Department Name: {task_name}, Department ID: {task_id} </h1></body></html>"
    return HttpResponse(html_output)

def view_department_by_id(request, department_id):   
    departments={
        1: 'Developers',
        2: 'Trainers',
        3: 'Marketing'
    } 
    department_name=departments.get(department_id, 'Unknown Department')
    
    context={'department_name': department_name,
        'department_id': department_id}
    return render(request, 'department-detail.html', context)

def view_department_by_name(request, department_name): 
    if department_name.lower()=='Developers'.lower() :       
        department_id=1   
    elif department_name.lower()=='Trainers'.lower() :
        department_id=2
    else:
        return HttpResponse("Department not found!", status=404)
    return redirect('view_department_by_id', department_id=department_id)
    
    
