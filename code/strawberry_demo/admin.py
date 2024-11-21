from django.contrib import admin
from .models import Fruit, Color

admin.site.site_header = "SSC-ICT Strawberry GraphQL Demo"
admin.site.site_title = "SSC-ICT Strawberry GraphQL"
admin.site.index_title = "Welkom bij de SSC-ICT Strawberry GraphQL Demo"
admin.site.register(Fruit)
admin.site.register(Color)
