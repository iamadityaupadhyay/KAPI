from django import forms
from .models import *

class AdharImagesAdminForm(forms.ModelForm):
    class Meta:
        model = AdharImages
        fields = '__all__'

    class Media:
        js = ('js/image_preview.js',)