#PROGRAMA CRIADO EM GRUPO PARA A MATÉRIA DE ALPG (ALGORITMOS E LÓGICA DE PROGRAMAÇÃO) MINISTRADA PELO PROFESSOR
#AUGUSTO MELO
#ALUNOS:
#ANDRÉ LUIZ
#JOSÉ HENRIQUE
#VITOR MELO

item = []
custo = []
total = []


def enumerar():
    print(f'\033[30:104m Itens da Lista \033[1:30m{nome}: \033[m')
    for v, i in enumerate(item):
        print(f'\033[1:100m {v + 1}. {i} R${custo[v]:.2f} \033[m')


nome = str(input('\033[1:30:46m Dê um nome à lista de compras: \033[m'))
while True:
    produto = str(input('Digite o produto [\033[1:31m"stop"\033[m para parar a lista]: ')).lower()
    if produto == 'stop':
        break
    valor = float(input('Valor: '))
    item.append(produto)
    custo.append(valor)
    enumerar()
while True:
    remover = str(input('Você quer "riscar" algum item da lista? [\033[1:32mS\033[m/\033[1:31mN\033[m]: ')).upper()
    if remover == 'S':
        dig = int(input('Digite o número do item: '))
        item.pop(dig - 1)
        total.append(custo[dig - 1])
        custo.pop(dig - 1)
        enumerar()
        if len(item) <= 0:
            print('\033[1:30:44mVOCÊ CONCLUIU TODOS OS ITENS!\033[m')
            vpago = sum(total)
            print(f'Valor total da lista \033[1:35m{nome}\033[m: \033[1:30:42mR${vpago:.2f}\033[m')
            break
    else:
        if len(item) > 0:
            enumerar()
            vfalta = sum(custo)
            print(f'Valor total que falta na lista \033[1:35m{nome}\033[m: \033[1:30:41mR${vfalta:.2f}\033[m')
        break