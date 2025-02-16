from django.shortcuts import get_object_or_404, render,redirect
from .models import RoomAssign
from .forms import RoomAssignForm
from baseapp.models import Student


# Create your views here.
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
    

def view_student_payment(request):
    context=[]
    student=Student.objects.get(user=request.user)
    
    room=RoomAssign.objects.get(student=student.id)
    amount=room.total_payment
    # context['amount']=amount
    print(amount)
    return render(request,'base.html',{'amount':amount})


def manage_roomassign(request):
    assigned_rooms_list=RoomAssign.objects.all()
    context={
        'assigned_rooms':assigned_rooms_list
    }
    return render(request,'manage_roomassign.html',context)

def delete_room_assign(request,room_assign_id):
    instance=get_object_or_404(RoomAssign,id=room_assign_id)
    print(instance.room.room_alloted)
    instance.room.room_alloted-=1
    instance.room.save()
    instance.delete()
    return redirect('home')


