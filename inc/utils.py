from base64 import b64decode


def split_string(string, split_string):
    """
    @summary:
    Separe une chaine de charactere en blocs d'une taille donnée

    @params:
    string: La chaine de characteres à séparer
    split_string: La taille des blocs

    @returns:
    Un iterable contenant les blocs
    """

    return [string[i:i+split_string] for i in range(0, len(string), split_string)]


def read_file(name):
    '''
    @summary:
    Lis le fichier {name}

    @params:
    Le chemin du fichier a chiffrer

    @returns:
    Une chaine de characteres correspondant contenu du fichier.
    '''

    f = open(name, 'r')
    file = f.read()
    f.close()
    return file


def write_file(name: str, file, needrename=False):
    """
    @summary:
    Écris le fichier {name} contenant {file}

    @params:
    name: le nom du fichier a écrire
    file: le contenu à écrire dans le fichier
    """
    if needrename:
        name = name
    elif name.startswith("enc_"):
        name = name[4:]
    else:
        name = "dec_" + name

    with open(name, 'w') as f:
        f.write(file)


def decode_key(name):
    """
    @summary:
    Décode une clé dans le fichier donné

    @params:
    name: Le nom du fichier

    @returns:
    Un tuple contenant les deux valeurs de la clé privée ou publique
    """

    with open(name, 'r') as f:
        f.readline()
        decoded_key = b64decode(f.readline())
        n, e = decoded_key.split("\n".encode('ascii'))
        return(int(e.decode('ascii'), 16), int(n.decode('ascii'), 16))
