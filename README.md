Motor de Missão Espacial
Descrição do Projeto
O Motor de Missão Espacial é uma aplicação desenvolvida em Python que simula o gerenciamento de
missões de suporte a satélites em órbita terrestre. O sistema representa uma empresa responsável por
enviar robôs de manutenção até satélites cadastrados em diferentes tipos de órbita.
O programa permite registrar satélites, consultar o status de uma missão e gerar relatórios completos
dos satélites cadastrados. Além disso, realiza cálculos de distância e estimativas de tempo de chegada
dos robôs de suporte considerando características específicas de cada tipo de órbita.

Problema da Missão
Empresas que operam satélites precisam monitorar constantemente seus equipamentos e planejar
missões de manutenção quando necessário.
Para simular esse cenário, o sistema deve:
Registrar satélites em órbita.
Identificar o tipo de órbita do satélite.
Calcular sua posição aproximada ao longo do tempo.
Estimar a distância entre a Terra e o satélite.
Calcular o tempo necessário para que um robô de suporte alcance o satélite.
Disponibilizar relatórios para acompanhamento das missões.
O projeto busca aplicar conceitos de programação estruturada, manipulação de dicionários, funções,
datas e cálculos matemáticos.

Funcionalidades
Cadastro de Satélites
Permite registrar um novo satélite informando:
Nome do satélite
Altitude (km)
Tipo de órbita
Tipos disponíveis:
Geoestacionário
Média Órbita (MEO)
Baixa Órbita (LEO)
Cada satélite recebe automaticamente um identificador único no formato:
•
•
•
•
•
•

•
•
•

1.
2.
3.

1

ID1 ID2 ID3 ...
Também é armazenado o momento exato do cadastro.

Consulta de Status
Através do ID do satélite é possível:
Consultar informações básicas.
Calcular sua distância atual estimada.
Estimar o tempo necessário para o robô alcançar o satélite.

Relatório Geral
Exibe todos os satélites cadastrados e seus respectivos dados:
ID
Nome
Altitude
Tipo de órbita
Data e hora de cadastro

Regras de Negócio
Satélites Geoestacionários
São considerados fixos em relação à Terra.
Distância utilizada:
distância = altitude informada

Satélites de Média Órbita
A posição é atualizada considerando:
Raio da Terra: 6371 km
Velocidade orbital: 4 km/s
A distância é calculada usando a Lei dos Cossenos.
•
•
•

•
•
•
•
•

•
•

2

Satélites de Baixa Órbita
A posição é atualizada considerando:
Raio da Terra: 6371 km
Velocidade orbital: 7,8 km/s
A distância também é calculada através da Lei dos Cossenos.

Tempo de Viagem do Robô
A simulação considera uma velocidade fixa do robô:
28000 km/h
O sistema converte automaticamente o resultado para:
Horas
Minutos

Estrutura dos Dados
O sistema utiliza um dicionário principal para armazenar todos os satélites.
Exemplo:

{
"ID1": {
"nome": "Hubble",
"distância": 540,
"tipo de satélite": "Baixa orbita",
"cadastrado em": datetime(...)
}
}
Campos

Campo Tipo Descrição
nome string Nome do satélite
distância float Altitude em quilômetros
tipo de satélite string Tipo da órbita
cadastrado em datetime Data e hora do cadastro

•
•

•
•

3

Fluxo de Execução
Ao iniciar o sistema, o usuário visualiza o menu:

1 - Cadastrar um satélite
2 - Ver situação atual de um satélite
3 - Ver relatório total
0 - Sair
Cadastro
Exemplo:

Digite o nome do satélite: Starlink-01
Digite a altitude do satélite: 550
Digite o tipo:
3
Resultado:

Cadastro concluído!
Sua id: ID1

Consulta
Exemplo:

Digite a id do satélite:
ID1
Resultado:

Nome: Starlink-01
Altitude: 550 km
Tipo: Baixa orbita
A chegada ao satélite Starlink-01 será em cerca de 1 hora e 15 minutos

Tecnologias Utilizadas
• Python 3

4

Biblioteca math
Biblioteca datetime

Estrutura das Funções
gerador_id()
Responsável por gerar identificadores únicos para cada satélite.
cadastrar_sat()
Realiza o cadastro dos satélites.
calcular_diferenca_de_tempo()
Calcula o tempo transcorrido desde o cadastro.
calcular_distancia()
Calcula a distância atual do satélite em relação à Terra.
calcular_tempo_final()
Calcula o tempo estimado de viagem do robô.
status()
Consulta o status de um satélite específico.
relatorio()
Exibe todos os satélites cadastrados.
main()
Controla o menu principal e o fluxo geral da aplicação.

Como Executar o Projeto
Pré-requisitos
Python 3.10 ou superior instalado.
Verificar instalação:

python --version
•
•

•

5

ou

python3 --version

Execução
Salve o código em um arquivo:
motor_missao.py
Abra um terminal na pasta do projeto.
Execute:

python motor_missao.py
ou

python3 motor_missao.py
Utilize o menu interativo para realizar as operações.

Objetivos Acadêmicos
Este projeto foi desenvolvido com o objetivo de praticar:
Estruturas condicionais ( match/case )
Funções
Dicionários
Manipulação de datas e horários
Cálculos matemáticos
Estruturas de repetição
Entrada e saída de dados
Organização modular de código

Autor
Trabalho desenvolvido para a disciplina de Programação em Python no curso de Engenharia de
Software.
