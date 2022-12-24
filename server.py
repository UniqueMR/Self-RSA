from RSA import RSA
import os
from process_data import to_str

p = int(input('请输入一个质数：'))
q = int(input('请输入另一个质数：'))

rsa = RSA(p=p,q=q)

print('请把下面这两个数值告诉加密方：')
print(rsa.e)
print(rsa.n)
os.system('pause')

print('请将加密方传给你的数字记下来')
cipher_texts = []
cipher_text = []
os.system('pause')
while True:
    key = input('请逐一输入数字（按q结束输入）：')
    if key == 'q':
        cipher_texts.append(cipher_text)
        break
    else:
        cipher_text.append(int(key))

rsa.decrypt(c=cipher_texts)
print(to_str(rsa.m_dcrpt))



