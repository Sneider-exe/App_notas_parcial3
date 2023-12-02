from django import forms
from .models import Usuario, Nota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class notaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            'titulo', 
            'nota'
        ]
        labels = {
            'titulo': 'Título de la Nota', 
            'nota': 'Nota'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            'nota': forms.TextInput(attrs={'class': 'form-control'})}
    def __init__(self, *args, **kwargs):
        super(notaForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}
            
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user