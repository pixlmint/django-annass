from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from .models import BlogEntry


# Register your models here.


class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    exclude = ('date_posted', )
    list_display = ('title', 'date_posted', 'active')


admin.site.register(BlogEntry, YourModelAdmin)
