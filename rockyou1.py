# Lee el diccionario original como un archivo binario
with open("rock.txt", "rb") as file:
    original_passwords = file.read().splitlines()

# Decodifica las contraseñas y filtra/modifica
original_passwords = [password.decode("utf-8", errors="ignore") for password in original_passwords]
modified_passwords = [password.capitalize() + "0" for password in original_passwords if password and not password[0].isdigit()]

# Guarda las contraseñas modificadas en un nuevo archivo
with open("rockyou_mod.dic", "w") as file:
    for password in modified_passwords:
        file.write(password + "\n")

# Imprime la cantidad de contraseñas en el nuevo diccionario
print(f"Se han modificado y guardado {len(modified_passwords)} contraseñas en 'rockyou_mod.dic'.")


