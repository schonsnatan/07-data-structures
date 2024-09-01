# 1. Calcular Média de Valores em uma Lista
# 2. Filtrar Dados Acima de um Limite
# 3. Contar Valores Únicos em uma Lista
# 4. Converter Celsius para Fahrenheit em uma Lista
# 5. Calcular Desvio Padrão de uma Lista
# 6. Encontrar Valores Ausentes em uma Sequência

thisset = ["apple", "banana", "cherry"]
thisset2 = ["apple", "banana", "cherry", "mango"]

resultado = set(thisset2) - set(thisset)
print(resultado)

print("\nExercicio 1: \n")
def calculate_mean(lista: list) -> float:
    soma = sum(lista)
    media = soma/len(lista)
    return media

lista_num = [1,2,3,4,20]
print(calculate_mean(lista_num))

print("\nExercicio 2: \n")

def filter_values(limit_num: float, values: list) -> list:
    filtered_values = []
    for i in values:
        if i > limit_num:
            filtered_values.append(i)
    return filtered_values

limit = 10.5
lista_2 = [2,5,6,7,10,15,20,25]
print(filter_values(limit,lista_2))

print("\nExercicio 3: \n")

def count_unique(lista_num: list) -> list:
    return len(set(lista_num))

print(count_unique([1,1,2,3,3,3,3,5]))

print("\nExercicio 4: \n")

def celsius_to_fahrenheit(celcius: list) -> list:
    fahrenheit = []
    for i in celcius:
        num = i*(9/5)+32
        fahrenheit.append(num)
    return fahrenheit

print(celsius_to_fahrenheit([25,14.6,17.2,42.6]))

print("\nExercicio 5: \n")

def desvio_padrao(lista_media: list) -> float:
    media = sum(lista_media) / len(lista_media)
    variancia = sum((x-media) ** 2 for x in lista_media) / len(lista_media)
    return variancia ** 0.5

print(desvio_padrao([1,1,1,1,1,1,1,2]))

print("\nExercicio 6: \n")

def find_missing(values: list) -> list:
    minimo = min(values)
    maximo = max(values)
    values_compare = set(range(minimo,maximo+1))
    return list(values_compare-set(values))

print(find_missing([1,4,6,7,8,12]))