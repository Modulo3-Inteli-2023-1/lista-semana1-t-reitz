#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def cumulativo(lista):
    for i in range(len(lista)):
        if i != 0:
            lista[i] += lista[i-1]
    
    return lista



# Teste a sua função aqui (caso ache necessário)


print(cumulativo([2, 3, 4, 5]))








