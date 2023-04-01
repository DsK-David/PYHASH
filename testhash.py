import hashlib

# Obter a senha do usuário
senha = input("Digite sua senha: ")

# Ler o hash armazenado em um arquivo de texto
with open("senha.txt", "r") as file:
    hash_hex = file.read().strip()

# Criar um hash SHA256 da senha digitada
hash_obj = hashlib.sha256(senha.encode())

# Obter a representação hexadecimal do hash
hash_hex_input = hash_obj.hexdigest()
print(hash_hex_input)

# Comparar o hash digitado com o hash armazenado
if hash_hex_input == hash_hex:
    print("Senha correta!")
else:
    print("Senha incorreta!")
