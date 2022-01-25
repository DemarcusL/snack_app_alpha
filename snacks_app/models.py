from django.db import models 
from django.contrib.auth import get_user_model


# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=15)
    purchaser = models.CharField(max_length=15)
    description = models.CharField(default="Type Here", max_length=100)
# let's link with a foriegn key
    # reviewer = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)

