import hashlib

def md5_hash(pwd):
    digest = hashlib.md5()
    digest.update(pwd.encode('utf-8'))
    return digest.hexdigest()