
from django import forms
from .models import Checkout, Pago, Municipio, Barrio

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        # Incluimos los tres campos geográficos
        fields = ['departamento', 'municipio', 'barrio', 'direccion']
        widgets = {
            'departamento': forms.Select(attrs={'class': 'form-select', 'id': 'id_departamento'}),
            'municipio': forms.Select(attrs={'class': 'form-select', 'id': 'id_municipio'}),
            'barrio': forms.Select(attrs={'class': 'form-select', 'id': 'id_barrio'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Inicialmente vaciamos las opciones para evitar cargar toda la base de datos
        self.fields['municipio'].queryset = Municipio.objects.none()
        self.fields['barrio'].queryset = Barrio.objects.none()

        # Lógica para re-poblar los municipios si ya se seleccionó un departamento (ej. al fallar la validación)
        if 'departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        
        # Lógica para re-poblar los barrios si ya se seleccionó un municipio
        if 'municipio' in self.data:
            try:
                municipio_id = int(self.data.get('municipio'))
                self.fields['barrio'].queryset = Barrio.objects.filter(municipio_id=municipio_id).order_by('nombre')
            except (ValueError, TypeError):
                pass



class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['metodo_pago']
        widgets = {
            'metodo_pago': forms.Select(attrs={'class': 'form-select'})
        }
