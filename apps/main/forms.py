from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField, ModelMultipleChoiceField

from main.models import Pen, StoreConfig, Stores, Color


class ColorForm(forms.ModelForm):
    """Form for create color for pen."""

    color = CharField(
        widget=forms.TextInput(attrs={'type': 'color'})
    )

    class Meta:
        model = Color
        fields = '__all__'

    def clean(self):
        color_title = self.cleaned_data['color_title']
        if not color_title:
            raise ValidationError('fields must be not empty')

        
class PenForm(forms.ModelForm):
    """Pen Form."""

    ink_color = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Pen
        fields = '__all__'


class StoreConfigForm(forms.ModelForm):
    """Store Form."""

    class Meta:
        model = StoreConfig
        fields = '__all__'


class StoresForm(forms.ModelForm):
    """for pen store."""

    class Meta:
        model = Stores
        fields = '__all__'