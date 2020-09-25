from django.contrib import admin
from .models import Realtor

# Register your models here.


class RealtorAdmin(admin.ModelAdmin):       #admin_field_customization
                                        ##admin.ModelAdmin ke inherit kortaci.
                                            #ModelAdmin is a class

    class Meta:
        model = Realtor     #Realtor apps er model ke new 1ti admin model a niya asci
                            #eikhana Realtor apps er model ke niya kajkorar jonno intentiate kortaci
                                                #model theke nicca field gulo

    list_display = ['id','name', 'photo', 'email','phone']
    list_display_links = ['id']
    list_filter = ('name',)
    list_editable = ('name','email','phone',)
    search_fields = ('name', 'photo', 'email','phone','message','desc',)
    list_per_page = 25

admin.site.register(Realtor,RealtorAdmin)