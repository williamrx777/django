def verificar_campo_vazio(campo, label):
    campo = campo.strip()
    if len(campo) <= 0:
        raise Exception('O campo %s não pode estar vazio' % label)
    return campo
    pass
