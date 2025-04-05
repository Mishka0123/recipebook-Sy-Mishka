from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.timezone import now

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

User = get_user_model()

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes", null=True)
    created_on = models.DateTimeField(default=now)
    updated_on = models.DateTimeField(default=now)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    quantity = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)


class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')