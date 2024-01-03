import hashlib

def check_username(username):

    return True


def check_password(password):

    return True


def check_email(email):
    
    return True

def password_to_hash(password):
    encoded_password = password.encode()

    sha256_hash = hashlib.sha256()

    sha256_hash.update(encoded_password)

    return sha256_hash.hexdigest()
