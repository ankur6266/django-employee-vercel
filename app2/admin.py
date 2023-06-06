from django.contrib import admin
from app2.models import MyModel  # Import MyModel explicitly

# Register your models here.
from .models import Employees  # Import other models explicitly
admin.site.register(Employees)

class MyModelAdmin(admin.ModelAdmin):
    # Other model admin configurations here...
    pass

admin.site.register(MyModel, MyModelAdmin)

admin.site.site_header = 'Sachin Singh Rathore '
