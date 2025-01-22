# Teste Automatizado de API

Este projeto realiza testes automatizados para APIs RESTful, cobrindo cenários de **GET**, **POST** e **DELETE**. Foi desenvolvido em Python com o objetivo de verificar o comportamento e a integridade das APIs.

## Estrutura do Projeto

O projeto está organizado em três arquivos principais:

- **`routes.py`**: Contém as URLs das APIs para GET, POST e DELETE.
- **`body.py`**: Contém o corpo da requisição em formato JSON utilizado nos testes POST.
- **`main.py`**: Contém as funções que executam os cenários de teste.

Além disso, há uma função personalizada que gera nomes e e-mails aleatórios para os testes POST, garantindo dados dinâmicos em cada execução.

---

## Funcionalidades

1. **GET**:
   - Faz uma requisição GET à API.
   - Verifica o status code e imprime a resposta JSON retornada.

2. **POST**:
   - Envia dados para a API utilizando o corpo definido em `body.py`.
   - Utiliza a função de geração de e-mails e nomes aleatórios para criar dados dinâmicos.
   - Verifica se o status code está dentro dos padrões esperados (200 ou 201).

3. **DELETE**:
   - Realiza um GET inicial para obter a lista de usuários.
   - Identifica o último usuário da lista e realiza a deleção baseada no ID.
   - Verifica se o status code indica sucesso (200, 201 ou 204).
---
![Texto alternativo](https://github.com/YuriG95/Testes_Automatizados_API/blob/main/testes%20automatizado%20python.jpg)

---


## Dependências

As bibliotecas utilizadas neste projeto são:

```bash
requests
```

### Gerar o `requirements.txt`

Para criar um arquivo `requirements.txt` para seu projeto:

```bash
pip freeze > requirements.txt
```

---

## Como Executar

1. **Clone o Repositório:**

   ```
   git clone https://github.com/YuriG95/Testes_Automatizados_API 
   
   

2. Instale as Dependências:

```
pip install -r requirements.txt

```

3. **Configure o Projeto:**
   - Verifique e atualize os valores em `routes.py` e `body.py` de acordo com sua API.

4. **Execute os Testes:**

 ```  python -m testes.main ```
 
   

---

## Exemplo de Saída

```plaintext
Teste passou. Resposta da API > [{'email': 'yuri@gmail.com', 'id': 2, 'nome': 'Yuri'}]
Status Code: 200
Teste 1 - GET passou

Teste passou. Resposta da API > {'message': 'Usuário adicionado com sucesso!'}
Status Code: 201
Teste 2 - POST passou

Usuário com ID 5 deletado com sucesso!
Teste 3 - DELETE passou
Sucesso 3/3 testes passaram!
```

---

## Melhoria Implementada

### Geração de Dados Aleatórios
Foi adicionada uma função para gerar nomes e e-mails aleatórios nos testes POST. Isso evita colisão de dados e garante a validação de cenários com informações dinâmicas.

Exemplo:

```python
import random
import string

def generate_random_email():
    domain = random.choice(["empresa1.com", "empresa2.com", "empresa3.com"])
    local = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{local}@{domain}"

def generate_random_name():
    nomes = ["Ana", "Carlos", "Maria", "Beatriz", "Yuri"]
    sobrenomes = ["Silva", "Souza", "Oliveira", "Garcia"]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"
```

Essas funções são chamadas no `body.py` para preencher dinamicamente os dados do POST.

---

## Próximos Passos que irei adicionar

1. Adicionar cobertura para outros métodos HTTP como PUT e PATCH.
2. Incluir autenticação nos testes
3. Criar relatórios automáticos para os resultados dos testes.
4. Integrar com pipelines CI/CD.

---

## Contribuição

Fique à vontade para abrir issues ou pull requests para melhorias neste projeto!

