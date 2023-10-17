import binascii
import hashlib

def hash(salt, passwd):
    sx = binascii.unhexlify(salt)
    pb = passwd.encode("utf-8")
    md5sum = hashlib.md5(sx + pb).digest()
    return hashlib.sha1(sx + md5sum + pb).hexdigest()
hash('a1b2c3d4', 'salad')