from django.contrib import admin
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):       #admin_field_customization
                                    ##admin.ModelAdmin ke inherit kortaci.
                                            #ModelAdmin is a class

    class Meta:
        model = Listing     #listing apps er model ke new 1ti admin model a niya asci
                            #eikhana listing apps er model ke niya kajkorar jonno intentiate kortaci
                                                #model theke nicca field gulo

    list_display = ['id', 'title', 'address', 'city', 'price', 'photo_main', 'realtor','is_published']
    list_display_links = ['id', 'title',]
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'desc', 'address', 'city', 'price',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)  # link up with Admin
