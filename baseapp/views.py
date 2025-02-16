from django.shortcuts import render,redirect
from .forms import StudentRegisterForm
from .models import Student,Trainer
from hostel.models import Room,RoomAssign
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

@login_required()
def home(request):
    
    context={}
    student_count=Student.objects.all().count()
    room_count=Room.objects.all().count()
    room_assigned_count=RoomAssign.objects.all().count()
    room_available=room_count-RoomAssign.objects.all().count()

    context['room_assigned_count']=room_assigned_count
    context['student_count']=student_count
    context['room_count']=room_count
    context['room_available']=room_available
    return render(request,'dashboard.html',context)


def student_register(request):
    if request.method=="POST":
        form=StudentRegisterForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            messages.success(request,"Form has been submitted successfully")
            
            return redirect('home')
        

    else:
        form=StudentRegisterForm()        
            
    
    
    
    context={'form':form,}
    return render(request,'student_register.html',context)
    





def displaystudent(request):
    studentlist=Student.objects.all()
    return render(request,'managestudents.html',{'list':studentlist})

def updatestudent(request,pk):
    studentobj=Student.objects.get(id=pk)
    if request.method=="POST":
        form=StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/')
            
    username=studentobj.user.username
    email=studentobj.user.email

    form=StudentRegisterForm(instance=studentobj,initial={'username':username,'email':email,})
    return render(request,'updatestudent.html',{'form':form})


def deletestudent(request,pk):
    studentobj=Student.objects.get(id=pk)
    studentobj.delete()
    return redirect('display')





def get_trainers(request):
    # Get branch_id and course_id from the AJAX request
    branch_id = request.GET.get('branch_id')
    course_id = request.GET.get('course_id')
    
    # Filter trainers by both branch and course
    trainers = Trainer.objects.filter(branch_id=branch_id, course_id=course_id).values('id', 'trainer_name')

    # Return the filtered list of trainers as a JSON response
    return JsonResponse({'trainers': list(trainers)})