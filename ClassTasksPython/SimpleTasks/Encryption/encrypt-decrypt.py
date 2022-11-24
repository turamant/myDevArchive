"""
Шифрование:
Исходные данные + фиктивные данные = ШИФРОВАНИЕ (XOR ^) --> Ключ1(фиктивные данные) и Ключ2(результат)

Дешифрование:
Ключ1(фиктивные данные) и Ключ2(результат) = ДЕ-ШИФРОВАНИЕ (XOR ^) --> Исходные данные

XOR математика:
A ^ B = C
C ^ A = B
C ^ B = A
"""
from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    string_bytes: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    string = string_bytes.decode()
    return string


if __name__ == '__main__':
    key1, key2 = encrypt("это ключ шифрования")
    result: str = decrypt(key1, key2)
    print("Фиктивный ключ: ", key1)
    print("Результат шифрования: ", key2)
    print(result)
