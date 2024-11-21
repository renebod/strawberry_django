import strawberry_django
from strawberry import auto

from . import models

@strawberry_django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    category: auto
    color: "Color"  # Strawberry will understand that this refers to the "Color" type that's defined below

@strawberry_django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: list[Fruit] # This tells strawberry about the ForeignKey to the Fruit model and how to represent the Fruit instances on that relation