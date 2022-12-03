from django import forms

class FormularioEmpleados(forms.Form):

    PLATOS=(
        (1,'Nombre'),
        (2,'Apellido'),
        (3,'Identificacion')
    )

    Nombre=forms.CharField(
        required=True,
        max_length=5,
        label='Nombre Empleado: ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    Apellido=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    Identificacion=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    