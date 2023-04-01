import hashlib

# Obter a senha do usuário
senha = input("Digite sua senha: ")

# Criar um hash SHA256 da senha
hash_obj = hashlib.sha256(senha.encode())

# Obter a representação hexadecimal do hash
hash_hex = hash_obj.hexdigest()
print(hash_hex)

# Salvar o hash em um arquivo de texto
with open("senha.txt", "w") as file:
    file.write(hash_hex)
