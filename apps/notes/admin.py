from django.contrib import admin
from .models import *
# Register your models here.

class NoteInline(admin.StackedInline):
	model = Note
	extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category']
	inlines = [NoteInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ['title','content','visibility','category','user']
	list_filter = ['category','user']

	fieldsets = [
		(None, {'fields': ['title','content','visibility']}),
		('#$*******$#', {'fields': ['category','tags']}),
	]

	actions = ['make_private']

	def make_private(self, request, queryset):
		queryset.update(visibility=0)
	make_private.short_description = "Mark selected notes as private"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['tag']
