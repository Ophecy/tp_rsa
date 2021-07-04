import argparse
from inc import keygen, encrypt, decrypt

parser = argparse.ArgumentParser(description="Parsing args...")
parser.add_argument("command", choices=["keygen", "crypt", "decrypt"])
try:
    args, unknown = parser.parse_known_args()
except:
    parser.print_help()
    exit(0)

if args.command == "keygen":
    parser.add_argument("-f", "--file",
                        dest="file",
                        default="monRSA")
    parser.add_argument("-s", "--size",
                        dest="size",
                        default=10)
    args = parser.parse_args()

    keygen.keygen(args.size, args.file)

elif args.command == "crypt":
    parser.add_argument("-k", "--key",
                        dest="key",
                        required=True)
    parser.add_argument("-t", "--text",
                        dest="text",
                        default="")
    parser.add_argument("-i",
                        "--file",
                        dest="file",
                        default="")
    parser.add_argument("-o", "--output",
                        dest="output",
                        default="")
    args = parser.parse_args()
    encrypt.encrypt(args.file, args.key)

elif args.command == "decrypt":
    parser.add_argument("-k", "--key",
                        dest="key",
                        required=True)
    parser.add_argument("-t", "--text",
                        dest="text",
                        default="")
    parser.add_argument("-i", "--file",
                        dest="file",
                        default="")
    parser.add_argument("-o", "--output",
                        dest="output",
                        default=False)
    args = parser.parse_args()
    decrypt.decrypt(args.key, args.file, args.output)
else:
    print("Invalid parameter, exiting...")
    exit(1)
