#  Se achar necessario, faça import de outras bibliotecas




# Crie a função que será avaliada no exercício aqui

def multiplas_operacoes(var_a, var_b):
    soma = var_a + var_b
    subtracao = var_a - var_b
    multiplicacao = var_a * var_b
    if var_b != 0:
        divisao = var_a / var_b
    else:
        divisao = 0
        
    return(soma, subtracao, multiplicacao, divisao)


# Teste a sua função aqui (caso ache necessário)

print(multiplas_operacoes(3, 4))









