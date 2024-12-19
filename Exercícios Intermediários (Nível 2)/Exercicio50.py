#Valide um email simples.
import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    else:
        return False

email = "exemplo@dominio.com"
print(f"O email '{email}' é válido? {validar_email(email)}")
