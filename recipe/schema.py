import graphene
from graphene_django import DjangoObjectType

from recipe.models import Recipe, Category, Instruction

class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = ("id", "title", "notes", "category", "instruction", "description")
        
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "Recipes")

class InstructionType(DjangoObjectType):
    class Meta:
        model = Instruction
        fields = ("id", "step", "Instructions")

class Query(graphene.ObjectType):
    all_recipes = graphene.List(RecipeType)
    all_categories = graphene.List(CategoryType)
    all_instructions = graphene.List(InstructionType)

    def resolve_all_recipes(root, info):
        # We can easily optimize query count in the resolve method
        return Recipe.objects.all()

    def resolve_all_categories(root, info):
        # We can easily optimize query count in the resolve method
        return Category.objects.all()

    def resolve_all_instructions(root, info):
        # We can easily optimize query count in the resolve method
        return Instruction.objects.all()


schema = graphene.Schema(query=Query)