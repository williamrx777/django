from django.shortcuts import render, loader
from django.http import HttpResponse
from .forms import CadastroForm
from .models import *
from .util import *
import pycep_correios

def home(request):
    template = loader.get_template('appPessoas/home.html')
    return HttpResponse( template.render())
    pass

def cadastro(request):
    form = CadastroForm()
    return render(request, 'appPessoas/cadastro.html', {'form' :  form})
    pass

def lista(request):
    pessoas = []
    for pessoa in Pessoa.objects.all():
        pessoa.telefones = Telefone.objects.filter(pessoa = pessoa).all()
        pessoas.append(pessoa)


    return render(request, 'appPessoas/lista.html', {'pessoas' :  pessoas})
    pass


def cadastrar(request):
    try:
        if request.method == 'POST':
            form = CadastroForm(request.POST)
            if form.is_valid():
                if 'cadastrar' in request.POST:

                    pessoa = Pessoa()
                    endereco = Endereco()
                    telefone1 = Telefone()
                    telefone2 = Telefone()

                    pessoa.nome = verificar_campo_vazio(form.cleaned_data['nome'], 'nome')
                    pessoa.email = verificar_campo_vazio(form.cleaned_data['email'], 'email')
                    endereco.uf = verificar_campo_vazio(form.cleaned_data['uf'], 'estado')
                    endereco.cidade = verificar_campo_vazio(form.cleaned_data['cidade'], 'cidade')
                    endereco.bairro = verificar_campo_vazio(form.cleaned_data['bairro'], 'bairro')
                    endereco.rua = verificar_campo_vazio(form.cleaned_data['rua'], 'rua')
                    endereco.cep = verificar_campo_vazio(form.cleaned_data['cep'], 'cep')
                    endereco.complemento = form.cleaned_data['complemento']
                    if len(endereco.complemento) <= 0:
                        endereco.complemento = "SEM COMPLEMENTO"

                    telefone1.numero = verificar_campo_vazio(form.cleaned_data['numero1'], 'Telefone Residencial')
                    telefone1.tipo = 1
                    telefone2.numero = verificar_campo_vazio(form.cleaned_data['numero2'], 'Telefone Celular')
                    telefone2.tipo = 2

                    # Gravando os objetos no banco de dados
                    pessoa.save()
                    endereco.pessoa = pessoa
                    endereco.save()

                    telefone1.pessoa = pessoa
                    telefone1.save()
                    telefone2.pessoa = pessoa
                    telefone2.save()

                    msg = 'Pessoa cadastrada com sucesso.'
                    return render(request, 'appPessoas/cadastro.html', {'form' :  CadastroForm(),
                                                                        'msg' :  msg})
                elif 'pesquisar' in request.POST:
                    cep = form.cleaned_data['cep']
                    cep = verificar_campo_vazio(cep, 'cep')
                    if len(cep) == 8:
                        endereco = pycep_correios.consultar_cep(cep)
                        form = CadastroForm(
                            initial= {
                                'nome' :  form.cleaned_data['nome'],
                                'email' :  form.cleaned_data['email'],
                                'cep' :  cep,
                                'uf' :  endereco['uf'],
                                'rua' : endereco['end'],
                                'bairro' :  endereco['bairro'],
                                'cidade' :  endereco['cidade']

                            }
                        )
                        msg = 'Carregamento de CEP solicitado'
                        return render(request, 'appPessoas/cadastro.html', {'form': form,
                                                                            'msg': msg})


                    else:
                        raise Exception('Erro o cep deve conter exatamento 8 caracteres.')



        else:
            raise Exception('MethodError, Use post para formulários.')

    except Exception as ex:
        msg = ex.args
        return render(request, 'appPessoas/cadastro.html', {'form' :  CadastroForm(),
                                                            'msg' :   msg})


    pass














