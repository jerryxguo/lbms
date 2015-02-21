from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from import_export import fields

from books.models import Collection
from books.models import Class
from books.models import Student

import logging
logger = logging.getLogger(__name__)
#widget
class OneToManyForeignKeyWidget(widgets.Widget):
    def __init__(self, model, field='pk', *args, **kwargs):
        self.model = model
        self.field = field
        logger.debug('__init__: self.field =%s', self.field)
        super(OneToManyForeignKeyWidget, self).__init__(*args, **kwargs)

    def clean(self, value):
        
        if (value is None) or (not ',' in value):           
            return None
        values = value.split(',')
        
        dic  = dict(zip(self.field,values))    
            
        logger.debug('dic =%s', dic)
        return self.model.objects.get(**dic)
        
    def render(self, value):
    	if value is None:
            return ""
        return getattr(value, self.field[0])
        
        

# Register your models here.
class CollectionResource(resources.ModelResource):
    
    class Meta:
        model = Collection
        
    borrower = fields.Field(column_name='borrower', attribute='borrower', widget=OneToManyForeignKeyWidget(Student,['last_name','first_name']))   
    school_class = fields.Field(column_name='school_class', attribute='school_class', widget=widgets.ForeignKeyWidget(Class,'name'))  
    def dehydrate_borrower(self, Collection):        
        return unicode(Collection.borrower) if Collection.borrower else None
    
    def dehydrate_school_class(self, Collection):
        return unicode(Collection.school_class) if Collection.borrower else None

class CollectionAdmin(ImportExportModelAdmin):
    fieldsets = [
        ('Book Info',              {'fields': (('title','author'),('catalogue','level'))}), 
        #{'fields': ('title','author'),('catalogue','level')},         
        ('Borrow Status',               {'fields': (('school_class','borrower','available'),)}), 
        
    ]
    
    list_display = ('title', 'author', 'catalogue','level', 'available', 'school_class','borrower','creation_date','modified_date')
    list_filter = ['school_class','borrower','available','catalogue', 'level','creation_date','modified_date']
    search_fields = ['title','author',]
    
    resource_class = CollectionResource
    
    
   


class StudentInline(admin.TabularInline):
    model = Student
    extra = 10


class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Class Name',               {'fields': ['name']}),
    ]
    inlines = [StudentInline]
    
 
admin.site.register(Class,ClassAdmin)
admin.site.register(Collection,CollectionAdmin)


