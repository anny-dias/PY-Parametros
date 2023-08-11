''' Escreva uma função chamada mostrar_informacoes que aceite três parâmetros 
nomeados: nome, idade e cidade. A função deve imprimir uma mensagem 
formatada com essas informações. '''

def mostrar_informacoes(nome, idade, cidade):
    print(f'O seu nome é {nome}, sua idade é de {idade} anos e sua cidade é {cidade}')

mostrar_informacoes(nome="Maria", idade=20, cidade="São Paulo")

#OU

n = input('Nome: ')
i = int(input('Idade: '))
c = input('Cidade: ')

mostrar_informacoes(nome=n, idade=i, cidade=c)
