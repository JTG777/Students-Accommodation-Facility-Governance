from django.db import models
from django.contrib.auth.models import User

class Master(models.Model):

    isactive = models.BooleanField(default=True, verbose_name="Active")

    class Meta:
        abstract = True



# Create your models here.
class OneteamBranch(Master):
    branch_name=models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "OneTeam Branches"

    def __str__(self):
        return self.branch_name



class Course(models.Model):
    course_name=models.CharField(max_length=40)
    

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    trainer_name=models.CharField(max_length=40)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    branch=models.ForeignKey(OneteamBranch,on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.trainer_name}"
    




class Student(models.Model):
    GENDER=(("Male","Male"),("Female","Female"))

    student_name=models.CharField(max_length=40,null=True)
    student_dob=models.DateField(help_text="Write date of birth in yyyy-mm-dd format")
    student_no=models.BigIntegerField(unique=True,verbose_name='Mobile No.')
    # student_email_id=models.EmailField(unique=True,default=None)
    gender=models.CharField(max_length=6,choices=GENDER,default=None)
    guardian_name=models.CharField(max_length=40)
    guardian_no=models.BigIntegerField(unique=True)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    oneteam_branch_name=models.ForeignKey(OneteamBranch,on_delete=models.CASCADE, limit_choices_to={"isactive":True})
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    date_added=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)


    

    def __str__(self):
        return self.student_name



