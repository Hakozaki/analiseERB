import re

def encrypt(phone_num):
    ENCRYPT_NUMBER = 6
    ENCRYPT_SYMBOL = "X"
    encrypted = []
    counter = 0

    for ch in phone_num[::-1]:
        if counter == ENCRYPT_NUMBER:
            encrypted.append(ch)
            continue

        try:
            int(ch)
            counter += 1
            encrypted.append(ENCRYPT_SYMBOL)
        except ValueError:
            encrypted.append(ch)

    return "".join(encrypted[::-1])

def soma_um(match):
    numero = match.group()    
    novo_numero = ''.join("9" if int(digito) == 9 else str(int(digito) + 1) for digito in numero)
    return novo_numero

def fake_num(telefone):
    return re.sub(r'\d{3}(?=\D|$)', soma_um, telefone)