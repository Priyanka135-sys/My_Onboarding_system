from django import forms
from onboarding_track.models import Employee

class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'First Name','class':'forms-control'}))
    last_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name','class':'forms-control'}))

    email=forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Email','class':'forms-control'}))
    department=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Name of Department','class':'forms-control'}))
    start_date=forms.DateField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Date of Joining','class':'forms-control'}))
    is_onboarded=forms.BooleanField(required=False,widget=forms.widgets.TextInput(attrs={'placeholder':'Joined/Not Joined','class':'forms-control'}))
    class Meta:
        model=Employee
        exclude=("user",)