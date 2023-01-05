#pip install pyyaml==5.4.1
import yaml


arquivo = open('frutas.yaml')

#yaml.load() - Transforma o arquivo .yaml em um objeto python, como lista ou dicionário

arquivo = yaml.load(arquivo, Loader=yaml.BaseLoader)

print(arquivo)
#print(arquivo['veiculos'][0])

'''
{
    'frutas': 
        ['MaÃ§Ã£', 'Laranja', 'Morango', 'Manga'], 
    'veiculos': 
        ['Moto', 'Carro']
}


{
    'frutas': ['MaÃ§Ã£', 'Laranja', 'Morango', 'Manga'], 
    'veiculos': ['Moto', 'Carro'], 
    'pessoas': {
        '1': {'nome': 'Antonio', 'idade': '58'}
        }
}

'''