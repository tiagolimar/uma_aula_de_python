a = 10
b = 'um texto'
c = 12.1
d = [0,1,2,3]
e = (0,1,2,3)

f = {
    'nome' : 'Tiago',
    'idade' : 29,
    'altura' : 167,
}

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# Função entrar_na_balada

# Essa função recebe uma valor inteiro que representa a idade da pessoa e ela retorna uma mensagem permitindo ou não a entrada da pessoa na balada

def entrar_na_balada():
    idade = int(input("Qual a sua idade? "))

    if (idade >= 18):
        print("Você pode entrar na balada!")
    else:
        print("Você não pode entrar na balada!")

# entrar_na_balada()

# Crie uma função que recebe um número inteiro e printa na tela todos os números ímpares menores do que esse número

def imprime_impares():
    num = int(input("Digite um número: "))

    for item in range(num):
        if (item%2 == 1):
            print(item)

# imprime_impares()


# string methods e list methods

idade = 29
nome = 'Tiago Lima Sousa'
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
lista_de_nomes = nome.split()
nome_formatado = ' - '.join(lista_de_nomes)
tamanho_nome_formatado = len(nome_formatado)

print(nomeMaiusculo)
print(nomeMinusculo)
print(lista_de_nomes)
print(nome_formatado)
print(tamanho_nome_formatado)

# strip, concatenação, soma entre número e string, Fstring

# Fstring

# print(f'Olá meu nome completo é {nome}, tenho {idade} anos.')
listaA = [0,1,2]
listaB = [0,1,2]
listaC = listaA + listaB

print(listaC)

#list compreehension
#