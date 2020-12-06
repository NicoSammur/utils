import random
import argparse

parser = argparse.ArgumentParser(description='dumb password gen')
parser.add_argument("--l", default=8, help="default password lenght = 8")


args = parser.parse_args()
l = int(args.l)

s = "abcdefghijklmnñopqrstuvwxyz0987654321=)(/&%$#!.;"
password = "".join(random.sample(s,l))
print(password)
