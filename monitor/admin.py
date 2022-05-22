from django.contrib import admin
from .models import WebPage, Failure
from semantic_admin import SemanticModelAdmin, SemanticStackedInline, SemanticTabularInline

class ExampleStackedInline(SemanticStackedInline):
    pass

class ExampleTabularInline(SemanticTabularInline):
    pass

class ExampleAdmin(SemanticModelAdmin):
    inlines = (ExampleStackedInline, ExampleTabularInline)
# Register your models here.
from semantic_admin.filters import SemanticFilterSet

# class DemoFilter(SemanticFilterSet):
#     class Meta:
#         model = Demo
#         fields = ("demo_field",)

# class DemoAdmin(SemanticModelAdmin):
#     filter_class = DemoFilter


admin.site.register(WebPage)
admin.site.register(Failure)