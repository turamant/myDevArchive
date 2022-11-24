import hashlib
import base64
import hmac

digest_maker = hmac.new(b'b24423420ad559aa6d55d552e08d261366e504f7',
                        b'',
                        hashlib.md5)

with open('enum-1.py', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)
print('1d0d962ebb3c3aa75b5fcebe9125020c')
print()