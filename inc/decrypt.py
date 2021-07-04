from inc.utils import *


def decrypt(priv_key, path, output=False):
    """
    @summary:
    Dehiffre le fichier donné avec la clé donnée

    @params:
    priv_key: Le chemin de la clé privée pour chiffrer
    path: Le chemin vers le fichier
    """

    # lecture de la clé
    d, n = decode_key(priv_key)

    # lecture du fichier
    c_text = read_file(path)

    # découpage du fichier
    txt = split_string(c_text, len(str(n)))

    # initialisation
    x = ''
    m = 0
    for i in txt:
        m = (int(i) ** d) % n
        c = chr(m)
        x += c
    if output:
        write_file(output, ''.join(x), True)
    else:
        write_file(output, ''.join(x))


if __name__ == "__main__":
    d_file = decrypt(decode_key('monRSA'), "enc_lorem.txt")
