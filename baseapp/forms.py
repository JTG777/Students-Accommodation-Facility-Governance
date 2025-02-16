from .models import Student,OneteamBranch,Course,Trainer
from django import forms


from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class StudentRegisterForm(forms.ModelForm):
    username=forms.CharField(max_length=50)
    password1=forms.CharField(widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    email=forms.EmailField(label='Student Email')

    class Meta:
        model=Student
        # fields='__all__'
        fields=[f.name for f in Student._meta.fields if f.name not in ['user','date_added','updated_at']]+['email','username','password1','password2',]
        labels={'student_dob':'Date of Birth','guardian_no':'Guardian Mobile no.',}
        widgets = {
            'gender': forms.RadioSelect(),
            'student_dob': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
}

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Preload all branches and courses in the dropdown
            self.fields['oneteam_branch_name'].queryset = OneteamBranch.objects.all()
            self.fields['course_name'].queryset = Course.objects.all()
            self.fields['trainer'].queryset = Trainer.objects.all()   

    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data['password1']
        password2=cleaned_data['password2']
        mobile_no=cleaned_data['student_no']
        if len(str(mobile_no))<10:
             raise forms.ValidationError("Mobile No needs to be 10 digit")
        
        if password1!=password2:
            raise ValidationError("Passwords do not match")
        return cleaned_data


    
        

    def save(self,commit=True):
        user=User.objects.create_user(
              username=self.cleaned_data['username'],
              password=self.cleaned_data['password1'],
              
              email=self.cleaned_data['email'],
              )
        
        student=super().save(commit=False)
        student.user=user

        if commit:
            student.save()
            user.save()
        return student



        