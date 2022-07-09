from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import BookInstance
import datetime

class RenewBookModelForm(ModelForm):

    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = {'due_back': 'Renewal date', }

    def clean_due_back(self): #clean_nombre del field
       data = self.cleaned_data['due_back']

       #Check date is not in past.
       if data < datetime.date.today():
           raise ValidationError('Invalid date - renewal in past')

       #Check date is in range librarian allowed to change (+4 weeks)
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError('Invalid date - renewal more than 4 weeks ahead')
       # Remember to always return the cleaned data.
       return data
