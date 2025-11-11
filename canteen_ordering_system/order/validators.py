import re


def validate_cpf(cpf):
    """
    Valida um CPF brasileiro.
    Aceita formatos: 12345678901 ou 123.456.789-01
    Retorna: (é_válido, mensagem_erro)
    """
    # Remove caracteres especiais
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False, "CPF deve conter 11 dígitos"
    
    # Verifica se não é uma sequência repetida (ex: 11111111111)
    if cpf == cpf[0] * 11:
        return False, "CPF inválido (sequência repetida)"
    
    # Verifica o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[9]) != digito1:
        return False, "CPF inválido (primeiro dígito verificador)"
    
    # Verifica o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[10]) != digito2:
        return False, "CPF inválido (segundo dígito verificador)"
    
    return True, "CPF válido"


def validate_phone(phone):
    """
    Valida um telefone brasileiro.
    Aceita formatos: 
    - (11) 98765-4321
    - (11) 3456-7890
    - 11987654321
    - 1134567890
    Retorna: (é_válido, mensagem_erro)
    """
    # Remove caracteres especiais
    phone = re.sub(r'\D', '', phone)
    
    # Verifica se tem 10 ou 11 dígitos
    if len(phone) not in (10, 11):
        return False, "Telefone deve ter 10 ou 11 dígitos (com DDD)"
    
    # Verifica se começa com 0 (inválido)
    if phone[0] == '0':
        return False, "Telefone inválido"
    
    # Verifica o DDD (primeiros 2 dígitos)
    ddd = int(phone[:2])
    valid_ddds = list(range(11, 100))  # DDDs válidos no Brasil
    
    if ddd not in valid_ddds:
        return False, f"DDD {ddd} inválido"
    
    # Verifica se é celular (9º dígito = 9) ou fixo
    if len(phone) == 11:
        # Celular
        if phone[2] != '9':
            return False, "Celular deve ter 9 como terceiro dígito"
    
    return True, "Telefone válido"


def format_cpf(cpf):
    """Formata CPF para o padrão XXX.XXX.XXX-XX"""
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf


def format_phone(phone):
    """Formata telefone brasileiro para (XX) XXXXX-XXXX ou (XX) XXXX-XXXX"""
    phone = re.sub(r'\D', '', phone)
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    elif len(phone) == 10:
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
    return phone
