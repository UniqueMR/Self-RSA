from RSA import RSA
from process_data import load_txt

plain_txt = load_txt('./txt/input.txt')
rsa = RSA(m=plain_txt)
e = int(input('公钥e：'))
n = int(input('公钥n: '))
rsa.encrypt(e=e,n=n)
print(rsa.c)
