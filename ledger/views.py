from django.shortcuts import get_object_or_404, render
from .models import Recipe, Ingredient, RecipeIngredient

from django.contrib.auth.decorators import login_required

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def populate_database(request):

    tomato = Ingredient.objects.create(name="Tomato")
    onion = Ingredient.objects.create(name="Onion")
    pork = Ingredient.objects.create(name="Pork")
    water = Ingredient.objects.create(name="Water")
    sinigang_mix = Ingredient.objects.create(name="Sinigang Mix")
    
    garlic = Ingredient.objects.create(name="Garlic")
    vinegar = Ingredient.objects.create(name="Vinegar")
    salt = Ingredient.objects.create(name="Salt")
    black_pepper = Ingredient.objects.create(name="Whole Black Peppers")
    
    recipe1 = Recipe.objects.create(name="Recipe 1")
    recipe2 = Recipe.objects.create(name="Recipe 2")

    RecipeIngredient.objects.create(recipe=recipe1, ingredient=tomato, quantity="3 pcs")
    RecipeIngredient.objects.create(recipe=recipe1, ingredient=onion, quantity="1 pc")
    RecipeIngredient.objects.create(recipe=recipe1, ingredient=pork, quantity="1 kg")
    RecipeIngredient.objects.create(recipe=recipe1, ingredient=water, quantity="1 L")
    RecipeIngredient.objects.create(recipe=recipe1, ingredient=sinigang_mix, quantity="1 packet")

    RecipeIngredient.objects.create(recipe=recipe2, ingredient=garlic, quantity="1 head")
    RecipeIngredient.objects.create(recipe=recipe2, ingredient=onion, quantity="1 pc")
    RecipeIngredient.objects.create(recipe=recipe2, ingredient=vinegar, quantity="1/2 cup")
    RecipeIngredient.objects.create(recipe=recipe2, ingredient=water, quantity="1 cup")
    RecipeIngredient.objects.create(recipe=recipe2, ingredient=salt, quantity="1 tbsp")
    RecipeIngredient.objects.create(recipe=recipe2, ingredient=black_pepper, quantity="1 tbsp")
    RecipeIngredient.objects.create(recipe=recipe2, ingredient=pork, quantity="1 kg")

    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})