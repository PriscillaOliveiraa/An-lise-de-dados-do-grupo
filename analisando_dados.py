'''Passo 1 - Adicionar as informações:
    idade; sexo.
    Passo 2 - Verificar a idade'''
total18 = totalf20 = totalh = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    #Verificando a idade.
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade <20:
        totalf20 += 1
    resposta = ' '
    while resposta not in 'S/N':
        resposta = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totalh} homens cadastrados')
print(f'E temos {totalf20} mulheres com menos de 20 anos')
