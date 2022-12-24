from RSA import RSA
from process_data import load_txt,to_str,load_img,display_img
from arg_parse import argument_parser

args = argument_parser()

plain_txt = load_txt('./txt/input.txt')
plain_img = load_img('./img/number.jpg')


rsa_txt = RSA(p=args.p,q=args.q,m=plain_txt)
rsa_txt.encrypt()
rsa_txt.decrypt()

rsa_img = RSA(p=args.p,q=args.q,m=plain_img)
rsa_img.encrypt()
rsa_img.decrypt()

print('initial text:')
print(to_str(rsa_txt.m))
print('encrypted text:')
print(to_str(rsa_txt.c))
print('decrypted text:')
print(to_str(rsa_txt.m_dcrpt))

display_img(rsa_img.m,'initial img')
display_img(rsa_img.c,'encrypted img')
display_img(rsa_img.m_dcrpt,'decrypted img')


print('finished!')