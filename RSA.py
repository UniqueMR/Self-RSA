import random

class RSA():
    def __init__(self, p=None, q=None, m=None) -> None:
        #获取输入的两个质数p，q和等待加密的明文m
        self.p = p 
        self.q = q
        self.m = m
        if p != None and q != None:
            self.generate_key() #完成公钥和私钥的初始化

    def generate_key(self):
        self.n = self.p * self.q
        phi = (self.p - 1)*(self.q - 1)

        while True:
            self.e = random.randrange(1, phi) #在1~phi的范围内随机选择一个e
            g = self.gcd(self.e, phi)
            self.d = self.mod_inverse(self.e, phi) #依据当前的e，通过模转置的方法生成私钥d
            
            #检验是否满足equiv条件
            if g == 1 and self.e != self.d:
                break

        print('Finished generating key...')

    #RSA加密
    def encrypt(self,e=None,n=None):
        if e != None and n != None:
            self.e = e
            self.n = n
        self.c = [[pow(c, self.e, self.n) for c in l] for l in self.m]
        print('Finished generating ciphertext...')
        return self.c

    #RSA解密
    def decrypt(self,c=None):
        if c != None:
            self.c = c
        self.m_dcrpt = [[pow(c,self.d,self.n) for c in l] for l in self.c]

    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def mod_inverse(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return -1
