from django.db import models

class Categories(models.Model):
    catid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class SubCategories(models.Model):
    subcatid=models.AutoField(primary_key=True)
    catid=models.ForeignKey(Categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


