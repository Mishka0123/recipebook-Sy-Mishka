from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe, Ingredient, RecipeIngredient

from django.contrib.auth.decorators import login_required

from .forms import RecipeForm, RecipeImageForm

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


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


def add_recipe(request):
    if(request.method == 'POST'):
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    
    return render(request, 'add_recipe.html', {'form': form})


def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    
    if(request.method == 'POST'):
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
        
    else:
        form = RecipeImageForm()

    return render(request, 'add_recipe_image.html', {'form': form, 'recipe': recipe})

