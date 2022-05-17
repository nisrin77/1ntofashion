from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class show(models.Model):
    img=models.ImageField(blank=True, upload_to="images/")
    url=models.URLField(max_length=300, null=True)