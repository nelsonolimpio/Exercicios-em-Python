'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.'''

times = (' ','Grêmio','Palmeiras','Santos','Corinthians','Atlético Mineiro','Cruzeiro','Internacional','São Paulo','Flamengo','Fluminense','Atlético Paranaense',
'Botafogo','Vasco da Gama','Coritiba','Ponte Preta','Figueirense','Sport','Goiás','Chapecoense','Vitória')
print('~'*100)
print(f'Os 5 primeiros colocados:')
print(times[1:6])
print('~'*100)
print(f'Os últimos 4 colocados da tabela são:')
print(times[17:21])
print('~'*100)
print(f'Lista com os times em ordem alfabética:')
print(sorted(times[1:20]))
print('~'*100)
print(f'O time Chapecoense está na posição:')
print(times.index('Chapecoense'))