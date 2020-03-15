from django import forms
from .models import AssetClass
from .models import Allocation


class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['name',
                  'aa_1',
                  'aa_2',
                  'aa_3',
                  'aa_4',
                  'aa_5',
                  'aa_6',
                  'aa_7',
                  'aa_8',
                  'aa_9',
                  'aa_10'
         ]