import argparse

def argument_parser():
    parser = argparse.ArgumentParser(prog='RSA Algorithm',description='Implementation of RSA algorithm')
    parser.add_argument('-p','--p',type=int, default=17)
    parser.add_argument('-q','--q',type=int, default=13)
    return parser.parse_args()


