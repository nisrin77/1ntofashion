from django.db import models

# Create your models here.
class topt10(models.Model):
    head=models.CharField(max_length=200)
    text=models.TextField(null=True)
    img=models.ImageField(blank=True, upload_to="images/")
    url=models.URLField(null=True)
    def __str__(self):
        return self.head