import socket


def entrada_numerica(mensagem, tamanho):
    while True:
        valor = input(mensagem)
        if len(valor) != tamanho or not valor.isdigit():
            print(f"Erro: Insira exatamente {tamanho} dígitos numéricos.")
        else:
            return valor

def main():
    # Configuração do cliente
    host = '127.0.0.1'  # Endereço do servidor
    port = 12345        # Porta do servidor

    # Criação do socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Cliente conectado ao servidor.")

    while True:
        print("Menu:")
        print("1. Cadastrar cliente")
        print("2. Ler cliente")
        print("3. Atualizar cliente")
        print("4. Excluir cliente")
        print("5. Sair")
     

        choice = input("Escolha uma opção: ")

        if choice == "1":
            nome = input("Nome do cliente: ").ljust(30)  # 30 caracteres para nome
            sexo = input("Sexo do cliente (f / m): ")[0].upper()  # 1 caractere para sexo
            email = input("E-mail do cliente: ").ljust(30)  # 30 caracteres para email
            telefone = entrada_numerica("Telefone do cliente (apenas números): ", 12)
            cep = entrada_numerica("CEP do cliente (apenas números): ", 8)
            numero = int(input("Número da residência: "))

             
            mensagem = f"CADASTRAR,{nome},{sexo},{email},{telefone},{cep},{numero}"
            client_socket.send(mensagem.encode('utf-8'))

            # Recebe a resposta do servidor
            response = client_socket.recv(1024).decode()
            print(response)

        elif choice == "2":
            cliente_id = input("Digite o ID do cliente a ser lido: ")

            # Envia a solicitação de leitura ao servidor
            message = f"LER,{cliente_id}"
            client_socket.send(message.encode())

            # Recebe e imprime a resposta do servidor
            response = client_socket.recv(1024).decode()
            print(response)

        elif choice == "3":
            cliente_id = input("Digite o ID do cliente a ser atualizado: ")
            nome = input("Nome do cliente: ").ljust(30)  # 30 caracteres para nome
            sexo = input("Sexo do cliente (f / m): ")[0].upper()  # 1 caractere para sexo
            email = input("E-mail do cliente: ").ljust(30)  # 30 caracteres para email
            telefone = entrada_numerica("Telefone do cliente (apenas números): ", 12)
            cep = entrada_numerica("CEP do cliente (apenas números): ", 8)
            numero = int(input("Número da residência: "))

            # Codifica os dados para enviar ao servidor
            mensagem = f"ATUALIZAR,{cliente_id},{nome},{sexo},{email},{telefone},{cep},{numero}"
            client_socket.send(mensagem.encode('utf-8'))

            # Recebe e imprime a resposta do servidor
            response = client_socket.recv(1024).decode()
            print(response)

        elif choice == "4":
            cliente_id = input("Digite o ID do cliente a ser excluído: ")

            # Envia a solicitação de exclusão ao servidor
            message = f"EXCLUIR,{cliente_id}"
            client_socket.send(message.encode())

            # Recebe e imprime a resposta do servidor
            response = client_socket.recv(1024).decode()
            print(response)

        elif choice == "5":
            # Encerra a conexão com o servidor
            client_socket.close()
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
