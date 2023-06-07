from django import forms

class CadastroForm(forms.Form):

    nome = forms.CharField(max_length=100, label='Nome ',
                           widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                           required=False)
    email = forms.CharField(max_length=100, label='Email ',
                            widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                            required=False)

    cidade = forms.CharField(max_length=100, label='Cidade ',
                             widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                             required=False)
    uf = forms.CharField(max_length=5, label='UF ',
                         widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                         required=False)
    bairro = forms.CharField(max_length=100, label='Bairro ',
                             widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                             required=False)
    rua = forms.CharField(max_length=100, label='Rua ',
                          widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                          required=False)
    cep = forms.CharField(max_length=20, label='Cep ',
                          widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                          required=False)
    complemento = forms.CharField(max_length=100, label='Complemento ',
                                  widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                                  required=False)

    numero1 = forms.CharField(max_length=100, label='Residencial ',
                              widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                              required=False)
    numero2 = forms.CharField(max_length=100, label='Celular ',
                              widget= forms.TextInput(attrs= {'class' :  'form-control'}),
                              required=False)


    pass
