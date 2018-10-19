from django.db import models

# Create your models here.
class Disaster(models.Model):
    dis_id=models.AutoField(primary_key=True)
    dis_name=models.CharField(max_length=20,default='')
    dis_description=models.TextField(default='')
    dis_image=models.ImageField(upload_to='disaster-pic',blank=True)


    def __str__(self):
        return self.dis_name





