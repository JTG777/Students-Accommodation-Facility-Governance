from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(upload_to='profile_pics/',default='no_image.jpg',null=True,blank=True)

    def __str__(self):
        if self.user.is_staff or self.user.is_superuser:
            return self.user.username
        else:
            return self.user.student.student_name