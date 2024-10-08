from django.contrib import admin
from .models import Notice, Person, CommitteeMember,Patron,Book


admin.site.register(Notice)
admin.site.register(Patron)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('person', 'year', 'designation', 'order')
    list_filter = ('year', 'designation')
    ordering = ('year', 'order')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('code','title', 'author', 'genre', 'language')
    list_filter = ('genre', 'language')
    ordering = ('title', 'language', 'genre')