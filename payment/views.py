import json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import razorpay
from django.shortcuts import render,get_object_or_404
from django.conf import settings
from hostel.models import Payment,RecurringPayment
from django.contrib import messages


# Create your views here.
razorpay_client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))


def create_razorpay_order(request,payment_id,payment_type):
    if payment_type=='ONETIME':
        payment=get_object_or_404(Payment,id=payment_id)
        amount=int(payment.total_payment*100) #paisa
    elif payment_type=='RECURRING':
        payment=get_object_or_404(RecurringPayment,id=payment_id)
        amount=int(payment.amount_due*100)

    order_data={
        'amount':amount,
        'currency':'INR',
        'payment_capture':1
    }

    order= razorpay_client.order.create(order_data)

    if payment_type=='ONETIME':
        payment.razorpay_order_id=order['id']
        payment.save()

    else:
        payment.razorpay_order_id=order['id']
        payment.save()

    data={
        'order_id':order['id'],
        "status": "success",
        'amount':amount/100,     #convert to rupee
        'key':settings.RAZORPAY_KEY_ID,
        'payment_type':payment_type,
        'payment_id':payment_id,


    }
    print('im here')
    return JsonResponse(data)

    # return render(request,'payments/razorpay_payment.html',context)


def verify_payment(request):
    if request.method=='POST':
        
        data=json.loads(request.body)
        razorpay_order_id=data.get('razorpay_order_id')
        razorpay_payment_id=data.get('razorpay_payment_id')
        razorpay_signature=data.get('razorpay_signature')
        payment_id=data.get('payment_id')
        payment_type=data.get('payment_type')
        print('i was here')
        params_dict={
            'razorpay_order_id':razorpay_order_id,
            'razorpay_payment_id':razorpay_payment_id,
            'razorpay_signature':razorpay_signature,
        }
    try:
        razorpay_client.utility.verify_payment_signature(params_dict)

        if payment_type=='ONETIME':
            payment=get_object_or_404(Payment,id=payment_id)
            payment.is_paid=True
            payment.amount_paid=payment.total_payment
            payment.save()
            print('onetime')
        else:
            recurring_payment=get_object_or_404(RecurringPayment,id=payment_id)
            recurring_payment.is_paid=True
            recurring_payment.save()
            
            payment_instance=recurring_payment.payment
            payment_instance.amount_paid+=recurring_payment.amount_due
            payment_instance.save()
            print('recurring')


            if payment_instance.recurring_installments==payment_instance.recurringpayment_set.filter(is_paid=True).count():
                payment_instance.is_paid=True
                payment_instance.save()
        
        
        return JsonResponse({
            'status':'success',
            'message':'Your payment has been successful',
            'redirect_url':reverse('home')
        })

        # return render(request,'dashboard.html')
    except:
        messages.error(request,"Your Payment has been successful")
        return render(request,'dashboard.html')

    





