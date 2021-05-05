from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomerUser(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    mobile= models.CharField(max_length=10, null=False)
    image = models.FileField(null=False)
    gender= models.CharField(max_length=15, null=False )
    type = models.CharField(max_length=15, null=False)
    def _str_(self):
        return self.user.username
