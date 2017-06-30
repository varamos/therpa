from django.forms import ModelForm
from blog.models import *

class Form(ModelForm):
    class Meta:
        model = Submit
        fields=['Name', 'Date', 'PMID', 'Properties', 'Type', 'Effect_to_PrP', 'Effect_to_Diseases_progression', 'Materials', 'Information_of_Materials', 'Treatement', 'Binding_site', 'PubChem', 'email']
