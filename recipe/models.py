from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Instruction(models.Model):
    step = models.CharField(max_length=100)

    def __str__(self):
        return self.step

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)
    category = models.ForeignKey(
        Category, related_name="Recipes", on_delete=models.CASCADE
    )
    instruction = models.ForeignKey(
        Instruction, related_name="Instructions", on_delete=models.CASCADE, null=True
    )
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self
