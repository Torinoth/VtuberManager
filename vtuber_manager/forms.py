from django import forms

from .models import Talent


class TalentCreateForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'