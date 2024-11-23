from django.contrib import admin


from .models import Category
from .models import Diet

class  CatgoryAdmin(admin.ModelAdmin):
    list_display=("name",'description',"edit_button")
    search_fileds=("name","description")
    
    
    def edit_button(self,obj):
        return f'<a href="/admin/app/category/{obj.id}/change/">Edit</a>'
    
    edit_button.allow_tags=True
    edit_button.short_description="Edit_Category"
    
    list_filter=('name')
    
    actions=['delete_selected']
    
    def delete_selected(self,request,queryset):
        queryset.delete()
        self.message_user(request,'Categories successfully deleted')
    delete_selected.short_description="Delete selected categories"


class  DietAdmin(admin.ModelAdmin):
    list_display=("name",'description',"delete_button")
    
    
    def delete_button(self,obj):
        return f'<a href="/admin/app/category/{obj.id}/delete/">Delete</a>'
    
    delete_button.allow_tags=True
    delete_button.short_description="Delete_Diet"
    
    actions=['delete_selected']
    
    def delete_selected(self,request,queryset):
        queryset.delete()
        self.message_user(request,'Diet successfully deleted')
    delete_selected.short_description="Diet selected categories"



admin.site.register(Diet)
admin.site.register(Category)


# Register your models here.

