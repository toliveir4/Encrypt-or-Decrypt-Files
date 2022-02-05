import base64
import getpass
import hashlib
import optparse
import os

import pyminizip
from cryptography.fernet import Fernet


def encrypt():
    password = getpass.getpass('\033[01mPassword: ')

    # encrypt it
    hashed_key = hashlib.sha3_256(bytes(password, 'utf-8')).digest()
    key = base64.urlsafe_b64encode(hashed_key)

    f = Fernet(key)
    with open(inputfile, "rb") as file:
        # read the encrypted data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(inputfile, "wb") as file:
        file.write(encrypted_data)
    with open(outputfile, 'wb') as key_file:
        key_file.write(key)

    # creates a password-protected zip containing the file with the hashcode and deletes the original output file
    pyminizip.compress(outputfile, None, out_protected, password, 1)
    os.remove(outputfile)

    return print("\033[01m\033[92m\tSuccessfully encrypted\033[0m")


def decrypt():
    try:
        password = getpass.getpass('\033[01mPassword: ')
        pyminizip.uncompress(out_protected, password, None, 0)
    except Exception as error:
        print('\033[01m\033[91m\t[Error] %s\033[0m' % error)
        exit(0)

    with open(outputfile, 'rb') as key_file:
        key = key_file.read()
        f = Fernet(key)
    with open(inputfile, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    os.remove(outputfile)
    return print('\033[01m' + str(decrypted_data, 'utf-8') + '\033[0m')


if __name__ == '__main__':
    # =================Other Configuration================
    # Usages :
    usage = "usage: %prog [options] "
    # Version
    Version = "%prog 0.0.1"
    # ====================================================

    parser = optparse.OptionParser(usage=usage, version=Version)
    parser.add_option(
        '-i', '--input', type='string', dest='inputfile',
        help="File Input Path For Encryption", default=None)

    parser.add_option(
        '-o', '--output', type="string", dest='outputfile',
        help="File Output Path For Saving Encrypter Cipher", default=".")

    parser.add_option(
        '-e', '--encrypt', action='store_true', dest='encrypt',
        help="Encrypts the file", default=False)

    parser.add_option(
        '-d', '--decrypt', action='store_true', dest='decrypt',
        help="Decryptes the file", default=False)

    (options, args) = parser.parse_args()

    # Input Conditions Checkings
    if not options.inputfile or not os.path.isfile(options.inputfile):
        print("\033[01m\033[91m\t[Error] Please Specify Input File Path\033[0m")
        exit(0)
    if not options.outputfile or not os.path.isdir(options.outputfile):
        print("\033[01m\033[91m\t[Error] Please Specify Output Path\033[0m")
        exit(0)
    if not options.encrypt and not options.decrypt:
        print("\033[01m\033[91m\t[Error] Please Specify If You Want To Encrypt Or Decrypt a file\033[0m")
        exit(0)

    inputfile = options.inputfile
    outputfile = os.path.join(options.outputfile, os.path.basename(options.inputfile).split('.')[0] + '.bin')
    out_protected = os.path.join(options.outputfile, os.path.basename(options.inputfile).split('.')[0] + '.zip')

    if options.encrypt:
        encrypt()
    elif options.decrypt:
        decrypt()
