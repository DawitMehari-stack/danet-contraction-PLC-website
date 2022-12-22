from django.contrib import admin
from .models import Content, Client, Owner, ContentType, Project, ProjectImage

# Register your models here.
"""class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "content_title", "content_description")
"""
"""class ConImgAdmin(admin.ModelAdmin):
    filter_horizontal = ("img_title", "image_url", "img_owner")"""

"""class PersonAdmin(admin.ModelAdmin):
    filter_horizontal = ("first","middle")   """ 

"""class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project","description", "client")   """  

#admin.site.register(ProjectImage)
admin.site.register(Project)
admin.site.register(Content)
admin.site.register(ContentType)
admin.site.register(Client)
admin.site.register(Owner)
admin.site.register(ProjectImage)

