from colorama import Fore
import os

tmp_file = 'temp.txt'

resp = ''
try:
    with open(tmp_file, 'r') as f:
        for line in f:
            resp = line
    
    os.remove(tmp_file)
except:
    pass

print('RESP: ',resp)

if resp == 'en':
    print('importado as listas em EN')
    from strings_en import *
    from dicionario_en import tipos
elif resp == 'pt-br':
    print('importado as listas em PT-BR')
    from strings_pt_br import *
    from dicionario_pt import *


def DadosPokemon(nome,peso,tipo1,tipo2, altura):
    print(string_006,nome)
    print(string_007,peso)
    print(string_008,tipo1)

    if tipo2 != None: 
        print(string_009,tipo2)

    print(string_010 + str(altura) + Fore.BLACK)

def tratamentoResultado(nome, peso,tipo1,tipo2, altura, chute_peso, 
chute_tipo1, chute_tipo2, chute_altura):

    print(Fore.BLUE + nome.upper(), end=':  ')

    if altura < chute_altura :
        print(Fore.RED + f"{string_010}: {chute_altura} " + u'\u2193', end=' -- ') #unicode icons: https://unicode-table.com/en/
    elif altura > chute_altura :
        print(Fore.RED + f"{string_010}: {chute_altura} " + u'\u2191', end=' -- ')
    else:
        print(Fore.GREEN + f"{string_010}: {chute_altura}", end=' -- ')

    if peso < chute_peso :
        print(Fore.RED + f"{string_007}: {chute_peso} " + u'\u2193' + Fore.BLACK, end=' -- ')
    elif peso > chute_peso :
        print(Fore.RED + f"{string_007}: {chute_peso} " + u'\u2191' + Fore.BLACK, end=' -- ')
    else:
        print(Fore.GREEN + f"{string_007}: {chute_peso}" + Fore.BLACK, end=' -- ')
    
    if tipo1 != chute_tipo1 :
        print(Fore.RED + f"{string_008}: {tipos[chute_tipo1]}", end='')
    else:
        print(Fore.GREEN + f"{string_008}: {tipos[chute_tipo1]}", end='')

    #print('DEBUG: Tipo2 - '+str(chute_tipo2))

    if chute_tipo2 != None:
        if tipo2 != None:
            if tipo2 != chute_tipo2 :
                print(Fore.RED + f" -- {string_009}: {tipos[chute_tipo2]}")
            else:
                print(Fore.GREEN + f" --{string_009}: {tipos[chute_tipo2]}")
        else:
            if tipo1 != chute_tipo2 :
                print(Fore.RED + f" -- {string_009}: {tipos[chute_tipo2]}")
            else:
                print(Fore.GREEN + f" -- {string_009}: {tipos[chute_tipo2]}")

def extrair_dados(r):
    # 3-tratamento /extração dos dados json
    # 	3a-(nome, peso, tipo,altura)
    # 	3b-(armazenar informações em variaveis.)
    nome = r.get("name")
    #print(nome)
    peso = r.get("weight")

    if len(r.get("types")) == 1:
        tipo1 = r.get("types")[0].get("type").get("name")
        tipo2 = None
    else:
        tipo1 = r.get("types")[0].get("type").get("name")
        tipo2 = r.get("types")[1].get("type").get("name")

    altura = r.get("height")

    return [nome, peso, tipo1, tipo2, altura]
