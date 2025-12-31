from django.contrib import admin
from .models import FeedBack

class FeedBackAdmin(admin.ModelAdmin): # Class for customize admin panel
    list_display = ['email', 'message', 'status']

    list_filter = ['status'] # Making filtering by status

    search_fields = ['email', 'message'] # Looking for matches in email field and message field

admin.site.register(FeedBack, FeedBackAdmin) # Adding FeedBack model to admin panel