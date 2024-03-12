############################################# IMPORTS #######################################################################
from hashlib import md5, sha1, sha224, sha256, sha384, sha512


############################################# METHODS #######################################################################
def codified_password(pwd, file, mode='a+'):
    print('*************************************************************************************************************\n')
    print(f'[*] The password is: {pwd}\n')
    with open(f'{file}.txt', mode) as passFile:
        passFile.write('*************************************************************************************************************\n')
        passFile.write(f'[*] The password is: {pwd}\n')
        
        md5_pass = md5(pwd.encode('utf-8')).hexdigest()
        print(f'[*] MD5 password is: {md5_pass}\n')
        passFile.write(f'[*] MD5 password is: {md5_pass}\n')

        sha1_pass = sha1(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-1 password is: {sha1_pass}\n')
        passFile.write(f'[*] SHA-1 password is: {sha1_pass}\n')

        sha224_pass = sha224(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-224 password is: {sha1_pass}\n')
        passFile.write(f'[*] SHA-224 password is: {sha224_pass}\n')

        sha256_pass = sha256(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-256 password is: {sha1_pass}\n')
        passFile.write(f'[*] SHA-256 password is: {sha256_pass}\n')

        sha384_pass = sha384(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-384 password is: {sha384_pass}\n')
        passFile.write(f'[*] SHA-384 password is: {sha384_pass}\n')

        sha512_pass = sha512(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-512 password is: {sha512_pass}\n')
        passFile.write(f'[*] SHA-512 password is: {sha512_pass}\n')

        passFile.close()


def run():
    menu = '1'
    
    while menu == '1' or menu == '2':
        menu = input('1. Codified password\n'
                     '2. Codified 100.000 familiar passwords\n'
                     '(Other). Exit\n'
                     'Enter your option: ')
        if menu == '1':
            pwd = input('Enter your password: ')
            file = input('Enter the file name: ')
            codified_password(pwd.strip(), file)

        elif menu == '2':
            passwords = open('familiar passwords.txt', 'r')
            file = input('Enter the file name: ')
            for pwd in passwords.readlines():
                codified_password(pwd.strip(), file)
        else:
            break


############################################## MAIN #######################################################################
if __name__ == '__main__':
    run()