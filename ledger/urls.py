from django.urls import path
from .views import recipe_list, recipe_detail, populate_database, add_recipe, add_recipe_image
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('populate/',populate_database,name = 'populate_database'),
    
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('recipe/add/', add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/add_image/', add_recipe_image, name='add_recipe_image')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

