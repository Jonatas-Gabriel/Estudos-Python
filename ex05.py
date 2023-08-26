distancia_percorrida = int(input('Digite a distancia percorrida (KM): '))
combustivel_gasto = float(input('Total de combustivel gasto: '))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f'O consumo médio do carro é: {consumo_medio:.3f} km/l')
