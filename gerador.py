from faker import Faker 
from datetime import datetime
from random import randint
 
fake = Faker(locale='pt-br')
 
for i in range(1,205): # considerando que não tem contato na agenda, se tiver aumente o valor do 1
    id = i
    nome = fake.first_name()
    sobrenome = fake.last_name()
    nome1 = nome.split()
    email = nome1[0].lower() + '@email.com'
    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    categoria_id = randint(1,3)
    telefone = fake.phone_number()
    descricao = fake.sentence()
 
    print(f"INSERT INTO contatos_contato (id, nome, sobrenome, telefone, email, data_criacao, descricao, categoria_id)" 
         f"VALUES ({id}, '{nome}', '{sobrenome}', '{telefone}', '{email}', '{data_criacao}', '{descricao}', {categoria_id});")
