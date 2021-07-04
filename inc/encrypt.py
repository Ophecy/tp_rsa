from inc.utils import *


def encrypt(path, pub_key="monRSA.pub"):
    """
    @summary:
    Chiffre le fichier donné avec la clé donnée

    @params:
    pub_key: Le chemin de la clé publique pour chiffrer
    path: Le chemin vers le fichier
    """
    # lecture du fichier
    n_text = read_file(path)

    # lecture de la clé
    e, n = decode_key(pub_key)

    # initialisation
    x = []
    m = 0
    print(n_text)
    for i in n_text:
        m = ord(i)
        (m**e) % n
    print(x)
    write_file(path, ''.join(map(str, x)))


if __name__ == "__main__":
    encrypt("lorem.txt", "monRSA")
