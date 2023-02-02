from django import forms

from main.models import Pen, Store, Stores


class PenForm(forms.ModelForm):
    """Pen Form."""

    class Meta:
        model = Pen
        fields = '__all__'


class StoreForm(forms.ModelForm):
    """Store Form."""

    class Meta:
        model = Store
        fields = '__all__'


class StoresForm(forms.ModelForm):
    """for pen store."""

    class Meta:
        model = Stores
        fields = '__all__'