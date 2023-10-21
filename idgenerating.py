import secrets
import hashlib

def generate_secure_id(prefix=''):
    random_token = secrets.token_hex(16)
    combined_id = prefix + random_token
    return hashlib.sha256(combined_id.encode('utf-8')).hexdigest()

def generate_secure_user_id():
    return generate_secure_id('user')

def generate_secure_chat_id():
    return generate_secure_id('chat')

def find_id_by_name(name_to_find, data):
    for name_id, name in data.items():
        if name == name_to_find:
            return name_id
    return None