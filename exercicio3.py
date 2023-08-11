''' Defina uma função chamada soma que aceite dois parâmetros numéricos (a e b) e 
retorne a soma desses números. Utilize anotações de tipos para indicar que os 
parâmetros e o retorno são do tipo float.'''

def soma(a: float, b:float) -> float:
    return a + b

a = float(input('Valor do A: '))
b = float(input('Valor do B: '))

print(soma(a, b))

