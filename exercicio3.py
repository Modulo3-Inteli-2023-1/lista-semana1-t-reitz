#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def soma_dos_aninhados(lista):
    soma = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            soma += lista[i][j]
    
    return soma



# Teste a sua função aqui (caso ache necessário)

lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
print(soma_dos_aninhados(lista))









