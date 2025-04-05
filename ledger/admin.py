from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

from .models import Recipe, RecipeImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline]


admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Recipe, RecipeAdmin)
