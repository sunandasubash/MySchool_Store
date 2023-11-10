# forms.py

from django import forms

class student(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'),('Others','Others')])
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ChoiceField(choices=[('science', 'Science'),('commerce', 'Commerce'),('art', 'Art'),('history', 'History'),('medicine', 'Medicine')])
    courses = forms.ChoiceField(choices=[])  # This will be populated dynamically using JavaScript
    purpose = forms.ChoiceField(choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials = forms.MultipleChoiceField(choices=[('notebook', 'Note Book'), ('pen', 'Pen'),('chart','Chart paper'),('sketch','Marker and highlighter')], widget=forms.CheckboxSelectMultiple)
