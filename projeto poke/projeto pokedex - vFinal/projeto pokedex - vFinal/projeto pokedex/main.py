import random
import requests
from colorama import Fore
import os

tmp_file = 'temp.txt'

try:
    os.remove(tmp_file)
except FileNotFoundError:
    print('')

print('1. Inglês')
print('2. Português')

while True:
    resp = input('Idioma/Language? ')

    if resp == '1':
        from strings_en import *
        arquivo = open(tmp_file, 'x')
        arquivo.write('en')
        arquivo.close()
        break

    elif resp == '2':
        from strings_pt_br import *
        arquivo = open(tmp_file, 'x')
        arquivo.write('pt-br')
        arquivo.close()
        break
    else:
        print("Digite um idioma valido!/Please enter a valid language!")

#Esse import só pode ser chamado depois que o arquivo já existe
from funcoes import *

# 1-sortear um numero de 1-151
numero = random.randrange(1, 151)

# 2-request informações do pokemon sorteado https://pokeapi.co/api/v2/pokemon/{id ou nome}/
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(numero)
r = requests.get(url)
# print(r.status_code)
r = r.json()
# print(r)

#Descompactação de lista
#https://www.alura.com.br/artigos/entendendo-o-desempacotamento-no-python
nome, peso, tipo1, tipo2, altura = extrair_dados(r)

tentativas = 0 
while True:
    tentativas = tentativas + 1
    if tentativas > 10 :
        print(Fore.BLACK + f"{string_002}")
        DadosPokemon(nome, peso, tipo1, tipo2, altura)
        exit()

    # 4-input do usuario, chute com nome do pokemon.
    while True:
        chute = input(Fore.BLACK + f"\n{string_001}").lower().strip()
        if chute != '':
            break
        

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(chute)
    r = requests.get(url)
    #print(r.text)

    while True:
        if r.text == "Not Found":
            print(f"{string_003}")
            print (f"{string_004}")
            while True:
                chute = input(Fore.BLACK + f"{string_001}").lower().strip()
                if chute != '':
                    break

        else:break
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(chute)
        r = requests.get(url)

    r= r.json()
    # print(r)

    # 3-tratamento /extração dos dados json
    # 	3a-(nome, peso, tipo,altura)
    # 	3b-(armazenar informações em variaveis.)
    chute_nome = r.get("name")
    chute_peso = r.get("weight")
    if len(r.get("types")) == 1:
        chute_tipo1 = r.get("types")[0].get("type").get("name")
        chute_tipo2 = None
    else:
        chute_tipo1 = r.get("types")[0].get("type").get("name")
        chute_tipo2 = r.get("types")[1].get("type").get("name")

    chute_altura = r.get("height") 

    # 5- verificar se pokemon digitado e igual ao pokemon sorteado.
    # 	5a-(verdadeiro- print mensagem de sucesso.fim)
    if nome == chute_nome:
        print(Fore.GREEN + f"{string_005}")
        dados = DadosPokemon(nome, peso, tipo1, tipo2, altura)
        exit()
    else: 
        # 6- Caso for falso:
        # 	-comparar as informações entre ambos.
        # 	-solicitar nova -tentativa.
        # 7- Repetir o passo 6 até o resposta ser correta ou exceder o numero de tentativas.
        print(f"{string_004}")
        Resultado = tratamentoResultado(chute_nome, peso,tipo1,tipo2, altura, chute_peso, chute_tipo1, chute_tipo2, chute_altura)

