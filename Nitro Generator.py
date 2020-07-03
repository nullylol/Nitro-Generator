import colorama, random, string, ctypes 
from colorama import Fore, init, Style

init(convert=True, autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW(f'[Nitro Code Generator] by Ascii Services | https://discord.gg/gCHJSZa')

amount = int(input('Amount Of Codes: '))

def Nitro():
    code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    gift = f'https://discord.gift/{code}'

    with open('nitro.txt', 'a+') as f:
        f.write(f'{gift}\n')

for i in range(amount):
    Nitro()

print(f'Generated {amount} codes!')
input()