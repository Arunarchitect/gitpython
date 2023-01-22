from django import forms    

class FinderForm(forms.Form):
    site_area = forms.FloatField()
    builtup_area = forms.FloatField()
    
