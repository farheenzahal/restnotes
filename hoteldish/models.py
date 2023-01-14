from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Dish(models.Model):
    name=models.CharField(max_length=25)
    category=models.CharField(max_length=25)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    review=models.CharField(max_length=100,null=True)
    review_date=models.DateField(auto_now_add=True)
    dish=models.ForeignKey(Dish,on_delete=models.CASCADE)