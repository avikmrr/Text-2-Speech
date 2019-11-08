from django.contrib import admin

# Register your models here.
from .forms import TextSpeechForm
from .models import TextSpeech

class TextSpeechAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]
	form = TextSpeechForm



	
admin.site.register(TextSpeech, TextSpeechAdmin)