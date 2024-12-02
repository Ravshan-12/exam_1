from django.shortcuts import render, redirect
from .models import Meal


def meal_list(request):
        name = request.GET.get('name')
        ingredients = request.GET.get('ingredients')
        price = request.GET.get('price')
        meal_type = request.GET.get('type')
        cuisine = request.GET.get('cuisine')

        if name and ingredients and price and meal_type and cuisine:
            Meal.objects.create(
                name=name,
                ingredients=ingredients,
                price=price,
                type=meal_type,
                cuisine=cuisine
            )
        meals = Meal.objects.all()
        ctx = {'meals': meals}
        return render(request, 'meals/meal-list.html', ctx)

