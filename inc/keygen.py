import random as r
from base64 import b64encode
from primesieve import primes
from inc.utils import write_file
# from time import time


def moduloInverse(a, m):
    # algo d'euclyde etendu
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def gcd(a, b):
    """
    @summary:
    Calcule le Plus Grand Commun Diviseur

    @params:
    a: le premier entier
    b: le deuxieme entier

    @returns:
    Le pgcd des entiers a et b
    """
    while a != 0:
        a, b = b % a, a
    return b


def randomRange(s):
    """
    @summary:
    Calcule une valeur au maximum inferieure d'un million a 10^s

    @params:
    La taille de la clé générée

    @returns:
    La valeur calculée
    """
    return r.randint(10**(s-1), (10**s)-10**6)


def writeKey(key: str, file: str, private: bool = False):
    # verifie si la clé est pub ou priv et l'ecris dans le fichier correspondant
    if private:
        write_file(
            file, f"---BEGIN {file} PRIVATE KEY---\n{key}\n---END {file} PRIVATE KEY---", True)
    else:
        write_file(
            f"{file}.pub", f"---BEGIN {file} PUBLIC KEY---\n{key}\n---END {file} PUBLIC KEY---", True)


def ed(p, q):
    """
    @summary:
    Calcule les valeur de e et de d

    @params:
    p et q

    @returns:
    un tuple contenant e et d
    """
    while 1:
        e = r.randrange(2**(32 - 1), 2**(32))
        if gcd(e, (p-1)*(q - 1)) == 1:
            break
    d = moduloInverse(e, (p-1)*(q-1))
    return (e, d)


def keygen(size, file=False):
    """
    @summary:
    Génere une clé rsa de la taille voulue dans le fichier ayant le nom souhaité

    @params:
    size: La taille de la clé
    file: Le nom du fichier à créer
    """

    size = int(size)
    if file == False:
        file = "monRSA"
    if size < 9:
        p = r.choice(primes(10**(size-1)))
        q = r.choice(primes(10**(size-1)))
        e = r.choice(primes(10**(size-1)))
    else:
        # choisis des nombre premiers aléatoire sur la range generée aléatoirement elle aussi
        ra = randomRange(size)
        p = r.choice(primes(ra, ra+10**6))
        ra = randomRange(size)
        q = r.choice(primes(ra, ra+10**6))
        ra = randomRange(size)
        e = r.choice(primes(ra, ra+10**6))

    n = p*q
    n2 = (p - 1) * (q - 1)
    e, d = ed(p, q)

    encoded_n = str(hex(n).removeprefix('0x'))
    encoded_e = str(hex(e).removeprefix('0x'))
    encoded_d = str(hex(d).removeprefix('0x'))

    pubkey = encoded_n + "\n" + encoded_e
    privkey = encoded_n + "\n" + encoded_d

    encoded_pub = b64encode(pubkey.encode('ascii'))
    encoded_priv = b64encode(privkey.encode('ascii'))

    writeKey(str(encoded_pub, "ascii"), file)
    writeKey(str(encoded_priv, "ascii"), file, True)


if __name__ == "__main__":
    keygen(10)
