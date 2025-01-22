import socket

# Dicionário para armazenar os dados dos clientes
clientes = {}
cliente_id = 1

def cadastrar_cliente(nome, sexo, email, telefone, cep, numero):
    global cliente_id
    clientes[cliente_id] = {
        'Nome': nome, 
        'Sexo': sexo, 
        'Email': email, 
        'Telefone': telefone, 
        'CEP': cep, 
        'Numero': numero
    }
    cliente_id_atual = cliente_id 
    cliente_id += 1
    return cliente_id_atual
    
def ler_cliente(cliente_id):
    return clientes.get(cliente_id, None)

def atualizar_cliente(cliente_id, nome, sexo, email, telefone, cep, numero):
    if cliente_id in clientes:
        clientes[cliente_id] = {
        'Nome': nome.strip(), 
        'Sexo': sexo, 
        'Email': email.strip(), 
        'Telefone': telefone.strip(), 
        'CEP': cep.strip(), 
        'Numero': numero
        }
        return True
    else:
        return False

def excluir_cliente(cliente_id):
    if cliente_id in clientes:
        del clientes[cliente_id]
        return True
    else:
        return False

def main():
    # Configuração do servidor
    host = '127.0.0.1'
    port = 12345

    # Criação do socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Servidor pronto para conexão!")

    while True:
        # Aceita a conexão de um cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conexão de {client_address}")

        while True:
            # Recebe a mensagem do cliente
            data = client_socket.recv(1024).decode()
            if not data:
                break

            partes = data.split(',')

            comando = partes[0]

            # Processa o comando
            if comando == "CADASTRAR":
                nome = partes[1].strip()
                sexo = partes[2].strip()
                email = partes[3].strip()
                telefone = partes[4].strip()
                cep = partes[5].strip()
                numero = int(partes[6].strip())

                cliente_id = cadastrar_cliente(nome, sexo, email, telefone, cep, numero)
                response = f"Cliente cadastrado com sucesso! ID: {cliente_id}"
                client_socket.send(response.encode())

            elif comando == "ATUALIZAR":
                cliente_id = int(partes[1].strip())
                nome = partes[2].strip()
                sexo = partes[3].strip()
                email = partes[4].strip()
                telefone = partes[5].strip()
                cep = partes[6].strip()
                numero = int(partes[6].strip())


                resultado = atualizar_cliente(cliente_id, nome, sexo, email, telefone, cep, numero)
                response = 'Cliente atualizado com sucesso!' if resultado else 'Cliente não encontrado'
                client_socket.send(response.encode())

            elif comando == "LER":
                cliente_id = int(partes[1].strip())
                cliente = ler_cliente(cliente_id)
                response = str(cliente) if cliente else 'Cliente não encontrado'
                client_socket.send(response.encode())

            elif comando == "EXCLUIR":
                cliente_id = int(partes[1].strip())
                resultado = excluir_cliente(cliente_id)
                response = 'Cliente excluído com sucesso!' if resultado else 'Cliente não encontrado'
                client_socket.send(response.encode())

            else:
                response = 'Comando inválido!'
                client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    main()