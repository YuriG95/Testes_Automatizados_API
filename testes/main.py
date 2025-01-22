import requests
from routes import urlget,urlpost,urldelet
from body import bodypost

#Teste automtizado Api Get
def test_api_status_get():
    url= urlget
    try:
        response =requests.get(url,timeout=5)
        if response.status_code ==200: 
             print(f"Teste passou. Resposta da Api > {response.json()} \nstatus code : {response.status_code}")
        else:
             print(f"ERRO, Teste não passou. Resposta da api > {response.json()} \nstatus code : {response.status_code}")    
        return response
    except requests.exceptions.ConnectionError:
        print("ERRO: Não foi possível conectar à API. Verifique se a API está em execução e acessível.")
    except requests.exceptions.TimeoutError:    
        print("ERRO: A requisição para a API excedeu o tempo limite.")
    except Exception as e:
        print(f"Erro inesperado : {e}")

#Teste automtizado Api Post
def test_api_status_post():
    url= urlpost
    try:
        responsepost = requests.post(url,json=bodypost,timeout=5)
        if responsepost.status_code ==200 or responsepost.status_code ==201:
            print(f"Teste passou. Resposta da Api > {responsepost.json()} \nstatus code : {responsepost.status_code}")
        else:
            print(f"ERRO, Teste não passou. Resposta da api > {responsepost.json()} \nstatus code : {responsepost.status_code}")
        return responsepost
    
    except requests.exceptions.ConnectionError:
        print("ERRO: Não foi possível conectar à API. Verifique se a API está em execução e acessível.")
    except requests.exceptions.TimeoutError:    
        print("ERRO: A requisição para a API excedeu o tempo limite.")
    except Exception as e:
        print(f"Erro inesperado : {e}")    

#Teste automtizado Api Delet
def test_api_status_delet():
    #Fazer um get e obter os dados Json dos Usuarios adiconados
    get_url = urlget
    response_get = requests.get(get_url)
    
    if response_get.status_code ==200:
        usuarios = response_get.json()
        #Verificar usuarios retornados pelo get
        if usuarios :
            print("Usuários disponíveis: ", usuarios)
            ultimo_usuario = usuarios [-1]
            id_usuario = ultimo_usuario.get("id")
            print(f"ID do último usuário: {id_usuario}")
             
            #Fazer a request de delet
            if id_usuario:
                delete_url = f"{urldelet}{id_usuario}"
                print(f"URL de deleção: {delete_url}")
                response_delete = requests.delete(delete_url)

                if response_delete.status_code in [200, 204]:
                    print(f"Usuário com ID {id_usuario} deletado com sucesso!")
                    return response_delete
                else:
                 print(f"Falha ao deletar o usuário com ID {id_usuario}. Status Code: {response_delete.status_code}")
                 print("Erro:", response_delete.text)
                 return response_delete
            else:
             print("Não foi possível obter o ID do último usuário.")
        else:
          print("Nenhum usuário encontrado na lista.")
    else:
        print("Falha ao obter a lista de usuários. Status Code:", response_get.status_code)
        print("Erro:", response_get.text)



response_get = test_api_status_get()
if response_get.status_code == 200:
    print("Teste 1 - GET passou")

    response_post = test_api_status_post()
    if response_post and response_post.status_code in [200,201]:
        print("Teste 2 - POST passou")

        response_delete = test_api_status_delet()
        if response_delete and response_delete.status_code in [200,201,204]:
            print("Teste 3 - DELETE passou")
            print("Sucesso 3/3 testes passaram!")
        else:
            print("Teste 3 - DELETE falhou")
    else:
        print("Teste 2 - POST falhou")
else:
    print("Teste 1 - GET falhou")         