from django.shortcuts import render,redirect
from .forms import StudentregisterForm
from .forms import RoomAssignForm,Userform
from .models import Student,Room,RoomAssign,Trainer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

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


def studentdetails(request):
    if request.method=="POST":
        form=StudentregisterForm(request.POST)
        uform=Userform(request.POST)
        
        if form.is_valid() and uform.is_valid():
            uname=uform.cleaned_data.get('username')
            pwd=uform.cleaned_data.get('password1')
            new_user=User.objects.create_user(username=uname,password=pwd)
            new_user.save()
            student=form.save(commit=False)
            student.user=new_user
            student.save()
            return redirect('home')
            
    
    
    form=StudentregisterForm()
    uform=Userform()
    context={'form':form,'uform':uform}
    return render(request,'studentdetails.html',context)
    


def roomassign(request):
    if request.method=='POST':
        form=RoomAssignForm(request.POST)
        if form.is_valid():
            months=form.cleaned_data.get('Duration')
            fees_obj=form.cleaned_data.get('fees_type')
            if fees_obj.fees_type=='One Time Payment':
                if form.cleaned_data.get('food_required')==True:
                    room=form.save(commit=False)
                    room.total_payment=months*2000+(months*4000)
                    room.save()
                    return redirect('home')
                else:
                    room=form.save(commit=False)
                    room.total_payment=months*4000
                    room.save()
                    return redirect('home')
            else:
                if form.cleaned_data.get('food_required')==True:
                    room=form.save(commit=False)
                    room.total_payment=months*2000+(months*4000)
                    room.save()
                    return redirect('home')
                else:
                    room=form.save(commit=False)
                    room.total_payment=months*4000
                    room.save()
                    return redirect('home')     


    else: 
        form=RoomAssignForm()
        return render(request,'roomassign.html',{'form':form})


def displaystudent(request):
    studentlist=Student.objects.all()
    return render(request,'managestudents.html',{'list':studentlist})

def updatestudent(request,pk):
    studentobj=Student.objects.get(id=pk)
    if request.method=="POST":
        form=StudentregisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/')
            
    
    form=StudentregisterForm(instance=studentobj)
    return render(request,'updatestudent.html',{'form':form})


def deletestudent(request,pk):
    studentobj=Student.objects.get(id=pk)
    studentobj.delete()
    return redirect('display')


def view_student_payment(request):
    context=[]
    student=Student.objects.get(user=request.user)
    
    room=RoomAssign.objects.get(student=student.id)
    amount=room.total_payment
    # context['amount']=amount
    print(amount)
    return render(request,'base.html',{'amount':amount})


def get_trainers(request):
    # Get branch_id and course_id from the AJAX request
    branch_id = request.GET.get('branch_id')
    course_id = request.GET.get('course_id')
    
    # Filter trainers by both branch and course
    trainers = Trainer.objects.filter(branch_id=branch_id, course_id=course_id).values('id', 'trainer_name')

    # Return the filtered list of trainers as a JSON response
    return JsonResponse({'trainers': list(trainers)})