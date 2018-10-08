from .models import List, ListItem
from django.contrib import admin


class ListItemInline(admin.TabularInline):
	model = ListItem
	fields = ('text', )

	def has_add_permission(self, request):
		return False


class ListAdmin(admin.ModelAdmin):
	inlines = (ListItemInline, )
	# fields = ('__all__', )


admin.site.register(List, ListAdmin)