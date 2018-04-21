from django import forms
from.import models

class CreateType(forms.ModelForm):
    class Meta:
        model = models.Type
        fields = ['userType']


class CreateIssued(forms.ModelForm):
    class Meta:
        model = models.Issued
        fields = ['IssueID','userName','ISBN','Return_date']

class CreateBook(forms.ModelForm):
    class Meta:
        model = models.book
        fields = ['ISBN','title','author','publisher','category','bookcount']
