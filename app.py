import pyfiglet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', help='text')
parser.add_argument('-f', '--font', help='font')

text = 'This is sample text'

args = parser.parse_args()
if args.text:
    text = args.text

if args.font:
    result = pyfiglet.figlet_format(text, font=args.font)
else:
    result = pyfiglet.figlet_format(text)
print(result)
