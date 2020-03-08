from django.contrib import admin
from .models import AdvUser, SuperRubric, SubRubric, Bb, AdditionalImage
from .forms import SubRubricForm


# Register your models here.

@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('is_activated', 'send_messages',)


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


admin.site.register(SuperRubric, SuperRubricAdmin)



class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm

admin.site.register(SubRubric, SubRubricAdmin)

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at',)
    fields = (('rubric', 'author'), 'title', 'content', 'price', 'contacts', 'image', 'is_active')
    inlines = (AdditionalImageInline,)

