from django.shortcuts import render
from baseapp.models import Student
from hostel.models import RoomAssign,Payment,RecurringPayment


# Create your views here.
def payment_dues(request):
    student = request.user.student

    # Get room assignment (handle if no room is assigned)
    room_assign = RoomAssign.objects.filter(student=student).first()
    recurring_payment_dues=[]
    onetime_payment_dues=[]

    if not room_assign:  # ✅ If no room is assigned, return empty list
        return render(request, 'payment_dues.html', {'payment_dues': []})

    # ✅ Check if room_assign exists before accessing `fees_type`
    if room_assign.fees_type and room_assign.fees_type.fees_type == 'RECURRING':
        due = RecurringPayment.objects.filter(payment__room_assigned=room_assign, is_paid=False).first()
        if due:
            recurring_payment_dues.append(due)
    else:
        onetime_payment_dues = Payment.objects.filter(room_assigned=room_assign, is_paid=False)

    context={'recurring_payment_dues':recurring_payment_dues,'onetime_payment_dues':onetime_payment_dues }
    return render(request, 'payment_dues.html', context)