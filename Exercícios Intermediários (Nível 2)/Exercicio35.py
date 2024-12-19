# Implemente uma função que valide email.

def val_email(email):
    if '@' not in email:
        return False
    
    partes = email.split('@')
    if len(partes) > 2:
        return False
    if len(partes[0])==0:
        return False
    if len(partes[1])==0:
        return False
    if '.' not in partes[1]:
        return False
    
    servidor = partes[1].split('.')
    if len(servidor[0])==0:
        return False
    if len(partes[1])==0:
        return False
    
print(val_email('teste'))

