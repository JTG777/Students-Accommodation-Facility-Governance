from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import RoomAssign,Payment,RecurringPayment
from datetime import timedelta

@receiver(post_save,sender=RoomAssign)
def create_payment(sender,created,instance,**kwargs):
    if created:
        if Payment.objects.filter(room_assigned=instance).exists():
            print("Payment already exists for this RoomAssign. Skipping creation.")
            return
        
        food_charge=instance.Duration*2000 if instance.food_required else 0
        print(food_charge)
        room_fee=instance.room.room_fee.fee_per_person
        print(room_fee)
        fees_type=instance.fees_type.fees_type
        print(fees_type)
        total_payment=food_charge+(room_fee*instance.Duration)
        pending_amount=total_payment
        due_date=instance.room_assigned_date


        Payment.objects.create(
            room_assigned=instance,
            is_paid=False,
            food_charge=food_charge,
            fees_type=fees_type,
            amount_paid=0,
            pending_amount=pending_amount,
            total_payment=total_payment,
            next_due_date=due_date if fees_type =='ONE TIME' else None
        )

@receiver(post_save,sender=Payment)
def create_recurring_payments(sender,created,instance,**kwargs):
    if created:
        if instance.fees_type=='RECURRING':
            duration=instance.room_assigned.Duration
            due_date=instance.room_assigned.room_assigned_date

            for i in range(0,duration):
                RecurringPayment.objects.create(
                    payment=instance,
                    amount_due=instance.total_payment/duration,
                    due_date=due_date,
                    is_paid=False
                )
                due_date+=timedelta(days=30)

            no_of_recurring=RecurringPayment.objects.filter(payment=instance).count()
            instance.recurring_installments=no_of_recurring
            instance.save()