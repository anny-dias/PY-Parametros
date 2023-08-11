# PARÂMETRO DEFAULT

def calcular_media(matematica: float, fisica: float=0, quimica: float=0):
    print(f'Matematica: {matematica}')
    print(f'Fisica: {fisica}')
    print(f'Quimica: {quimica}')
    media = (matematica + fisica + quimica) / 3
    return media

m = float(input('Matematica: '))
q = float(input('Quimica: '))
f = float(input('Fisica: '))


print(f'Media: {calcular_media(10, 8, 6)}')
print(f'Media: {calcular_media(10, 8)}')
print(f'Media: {calcular_media(10)}')

# PARÂMETROS POSICIONAIS E PARÂMETROS NOMEADOS

# POSICIONAIS (RESPEITAM A ORDEM DOS VALORES)
print(f'Media: {calcular_media(10, 8, 6)}')
print(f'Media: {calcular_media(10, 8)}')
print(f'Media: {calcular_media(10)}')

# NOMEADOS (NÃO PRECISAM RESPEITAR A MESMA ORDEM)
print(f'Media: {calcular_media(quimica=10, matematica=8, fisica=6)}')
print(f'Media: {calcular_media(10, 8)}')
print(f'Media: {calcular_media(10)}')

# POSICIONAIS SEMPRE ANTES DE NOMEADOS 
print(f'Media: {calcular_media(10, quimica=10, fisica=6)}')
print(f'Media: {calcular_media(10, 8)}')
print(f'Media: {calcular_media(10)}')