import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Student(models.Model):
    school_class = models.ForeignKey(Class,blank=True, null=True);
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Year = models.IntegerField(default=0)
    def __unicode__(self):
        return self.last_name + ','+ self.first_name
    
class Collection(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    catalogue = models.CharField(max_length=20)
    level = models.IntegerField(default=5)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    modified_date = models.DateTimeField(default =timezone.now(), blank=True)
    def __unicode__(self):
        return self.title
    available = models.BooleanField(default = True)
    school_class = models.ForeignKey(Class,blank=True, null=True);
    borrower = ChainedForeignKey(Student,chained_field="school_class",chained_model_field="school_class",  show_all=False, auto_choose=True, blank=True, null=True);
    def clean(self):
        if not self.available and (self.borrower==None or self.school_class==None):
            raise ValidationError('borrower\'s name and class are required')
        
        if self.available and self.borrower!=None:
            self.borrower = None
            self.schoolClass = None
    def save(self):
        if self.id:
            self.modified_date = timezone.now()
        else:
            self.creation_date = timezone.now()
        super(Collection,self).save()

