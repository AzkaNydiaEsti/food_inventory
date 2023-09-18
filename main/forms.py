from django.forms import ModelForm
from main.models import Barang

class ItemForm(ModelForm):
    class Meta:
        model = Barang
        fields = ["name", "quality", "type", "description", "amount"]