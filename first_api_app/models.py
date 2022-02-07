from django.db import models

# Create your models here.
class IndexModel(models.Model):
    id=models.CharField(primary_key=True,max_length=11,blank=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    url=models.CharField(max_length=50,blank=True,null=True)
    # url=models.CharField(max_length=50,blank=True,null=True)
    width=models.CharField(max_length=50,blank=True,null=True)
    height=models.CharField(max_length=50,blank=True,null=True)
    box_count=models.CharField(max_length=50,blank=True,null=True)
    # width=models.IntegerField(blank=True,null=True)
    # height=models.IntegerField(blank=True,null=True)
    # box_count=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name
