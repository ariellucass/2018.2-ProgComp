tempo_viagem = input('Informe o tempo da viagem em horas')

velocidade_media = input('Informe a velocidade média em km/h')

distancia_percorrida = int(tempo_viagem) * int(velocidade_media)

litros_usados = distancia_percorrida / 12

print('Velocidade Média (km/h): ', velocidade_media)

print('Tempo da Viagem (horas): ', tempo_viagem)

print('Distância Percorrida (km): ', distancia_percorrida)

print('Consumo do Carro (litros): ', litros_usados)