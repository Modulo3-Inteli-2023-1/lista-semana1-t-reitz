#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def tem_duplicados(lista):
    unique_nums = []
    for i in range(len(lista)):
        if lista[i] not in unique_nums:
            unique_nums.append(lista[i])
    if len(unique_nums) == len(lista):
        return False
    else:
        return True


# Teste a sua função aqui (caso ache necessário)

print(tem_duplicados([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))








