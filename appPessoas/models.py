from django.db import models

# Create your models here.
class Pessoa(models.Model):
    class Meta:
        db_table = "pessoa"

    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)


    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome, self.email)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome, self.email)

class Endereco(models.Model):
    class Meta:
        db_table = 'endereco'

    codigo = models.AutoField(primary_key=True)
    uf = models.CharField(max_length=5, null=False, default='')
    cidade = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=100, null=False)
    rua = models.CharField(max_length=100, null=False)
    cep = models.CharField(max_length=20, null=False)
    complemento = models.CharField(max_length=100, null=False)



    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        unique=True
    )


    def __str__(self):
        return '{} , {}, {}, {}, {}, {}'.format(
            self.codigo, self.cidade, self.bairro,
            self.rua, self.cep, self.complemento
        )

    def __repr__(self):
        return '{} , {}, {}, {}, {}, {}'.format(
            self.codigo, self.cidade, self.bairro,
            self.rua, self.cep, self.complemento
        )


    pass

class Telefone(models.Model):
    class Meta:
        db_table='telefone'

    class Tipo(models.IntegerChoices):
        TEL = 1, 'Residencial'
        CEL = 2, 'Celular'

    codigo = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=100, null=False)
    tipo = models.IntegerField(choices=Tipo.choices, default=1)

    @property
    def tipo_label(self):
        if self.tipo == 1:
            return 'Residencial'
        else:
            return 'Celular'


    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}, {}, {},'.format(self.codigo, self.tipo_label, self.numero)

    def __repr__(self):
        return '{}, {}, {},'.format(self.codigo,self.tipo_label, self.numero)

    pass




