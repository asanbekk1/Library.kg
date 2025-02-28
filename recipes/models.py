from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание рецепта")

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название ингредиента")
    quantity = models.CharField(max_length=100, verbose_name="Количество")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.name} ({self.quantity})"