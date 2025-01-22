#Json do Body Apis

import random
import string

#Função gerar email random
def emailrandom():
    dominios = ["gmail.com", "yahoo.com", "outlook.com","empresa1.com","empresa2.com","empresa3.com","empresa4.com" ]
    nome = ''.join(random.choices(string.ascii_lowercase, k=8))
    dominio = random.choice(dominios)
    return f"{nome}@{dominio}"

#Função gerar nome random
def nomerandom():
    nomes = ["Yuri", "Ana", "João", "Maria", "Carlos", "Beatriz", "Pablo","Junio","Anderson"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Costa","Garcia"]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"


bodypost = {
"email": emailrandom(),
"nome": nomerandom()
}