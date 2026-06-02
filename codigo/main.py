import math

from datetime import datetime

def gerador_id(contador):
    contador += 1
    return contador

def cadastrar_sat(id_do_sat):
    esc=True
    nome = input("Digite o nome do satélite ")
    distancia = float(input("Digite a altitude do satélite "))
    while esc:
        tipo_escolha=input('Digite o tipo de satélite\n'
                   '1- Geoestacionário\n'
                   '2- Média orbita\n'
                   '3- Baixa orbita\n'
                   'Tipo escolhido(1/2/3): ')
        match tipo_escolha:
            case '1':
                tipo='Geoestacionário'
                esc=False
            case '2':
                tipo='Média orbita'
                esc=False
            case '3':
                tipo='Baixa orbita'
                esc=False
            case _:
                print('Escolha entre tipo 1, 2 ou 3')
    momento_do_cadastro=datetime.now()
    dici = {id_do_sat: {"nome": nome, "distância": distancia, "tipo de satélite": tipo, "cadastrado em": momento_do_cadastro}}
    return dici

def calcular_diferenca_de_tempo(t_lancamento):
    tempo_total=(datetime.now() - t_lancamento).total_seconds()
    return tempo_total

def calcular_tempo_final(df):
    velocidade_robo=28000
    tempo_total = df / velocidade_robo
    horas = int(tempo_total)
    minutos = round((tempo_total - horas) * 60)
    return horas,minutos

def calcular_distancia(satelitex):
    match satelitex['tipo de satélite']:
        case 'Geoestacionário':
            distancia_final=satelitex['distância']
        case 'Média orbita':
            t=calcular_diferenca_de_tempo(satelitex['cadastrado em'])
            raio_terra=6371
            altitude=satelitex['distância']
            velocidade=4
            r=raio_terra+altitude
            theta=(velocidade*t)/r
            distancia_final=math.sqrt(r ** 2 + raio_terra ** 2 - 2 * r * raio_terra * math.cos(theta))
        case 'Baixa orbita':
            t = calcular_diferenca_de_tempo(satelitex['cadastrado em'])
            raio_terra = 6371
            altitude = satelitex['distância']
            velocidade = 7.8
            r = raio_terra + altitude
            theta = (velocidade * t) / r
            distancia_final = math.sqrt(r ** 2 + raio_terra ** 2 - 2 * r * raio_terra * math.cos(theta))

    return distancia_final

def status(dg):
    achar_id = input('Digite a id do satélite ').strip().upper()
    if achar_id not in dg:
        print('Satélite não encontrado')
    else:
        sat=dg[achar_id]
        print(f"Nome: {sat['nome']}\n"
              f"Altitude: {sat['distância']} km\n"
              f"Tipo: {sat['tipo de satélite']}")
        distancia_att=calcular_distancia(dg[achar_id])
        h,m=calcular_tempo_final(distancia_att)
        if h == 0:
            print(f"A chegada ao satélite {dg[achar_id]['nome']} será em menos de uma hora")
        elif m == 0:
            print(f"A chegada ao satélite {dg[achar_id]['nome']} será em cerca de {h} horas")
        else:
            print(f"A chegada ao satélite {dg[achar_id]['nome']} será em cerca de {h} horas e {m} minutos")

def relatorio(dg):
    for id_sat, total in dg.items():
        print(f' \n'
              f'{id_sat}')
        for chave, valor in total.items():
            print(f'  {chave}: {valor}')

def main():
    contador_id = 0
    dicionario_global = {}
    while True:
        print('Digite abaixo o número da função que deseja realizar:\n'
              '1- Cadastrar um satélite\n'
              '2- Ver situação atual de um satélite\n'
              '3- Ver relatório total\n'
              '0- Sair')
        escolha = (input('Opção escolhida: '))
        match escolha:
            case '1':
                contador_id=gerador_id(contador_id)
                id_satelite = 'ID'+str(contador_id)
                novo_cadastro = cadastrar_sat(id_satelite)
                dicionario_global.update(novo_cadastro)
                print(f'  Cadastro concluído! Sua id: {id_satelite}')
            case '2':
                status(dicionario_global)
            case '3':
                relatorio(dicionario_global)
            case '0':
                print('Agradecemos a preferência')
                break
            case _:
                print('Valor invalido')

print('Bem vindo ao Motor de Missão')
main()
