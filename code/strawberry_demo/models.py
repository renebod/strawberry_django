from django.db import models
from django_choices_field import TextChoicesField

class FruitCategory(models.TextChoices):
    CITRUS = "citrus", "Citrus"
    BERRY = "berry", "Berry"

class Fruit(models.Model):
    """A tasty treat"""

    name = models.CharField(max_length=20, help_text="The name of the fruit variety")
    category = TextChoicesField(choices_enum=FruitCategory, help_text="The category of the fruit")
    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        related_name="fruits",
        blank=True,
        null=True,
        help_text="The color of this kind of fruit",
    )

class Color(models.Model):
    """The hue of your tasty treat"""

    name = models.CharField(
        max_length=20,
        help_text="The color name",
    )