from django import forms
# importing attribute to add them to form
from testapp.models import Prodcuts,User_details

class Products_Form(forms.ModelForm):

    class Meta:
        model=Prodcuts
        fields='__all__'

class Detail_Form(forms.ModelForm):
   class Meta:
        model=User_details
        fields='__all__'