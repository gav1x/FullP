import os, sys, time
from colorama import Fore, Style
from random import choice
clean=('cls' if os.name == 'nt' else 'clear')
C= "\033[97;1m"
G = "\033[92;1m"
P = "\033[1;35m"
result=os.popen('figlet Gav1x').read()
def banner():
    cor = [Fore.RED]
    banner = r"""
====================
- By gav1x
- GitHub: https://github.com/gav1x
- Greetz: DevNoias - Mr Osama - Bugea1s - Fz1n - Tr4xb0y - V4p0r
===================="""
    n = 0
    for char in banner:
        sys.stdout.write(f"{choice(cor)}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        n +=1
        time.sleep(0.007)

def clear():
	os.system(clean)

def menu(ms0):
	clear();banner();print('\n'+result+ms0)
	return input(f'\n{C}===> {G}')

def error():
	text='Caractere(s) não reconhecido(s)';clear();banner();print(f'\n{C}====================\n[{P}Error!{C}] {text}\n====================');time.sleep(3)
	
def dialog1():
	clear();banner();print(result)
	return input(f'\n{C}===> {G}')

def dialog2(msg):
	clear();banner()
	return input(f'\n{C}====================\n{msg}\n====================\n{C}{G}Deseja fazer uma nova consulta?\n{C}[{G}1{C}] Sim\n[{G}2{C}] Nao\n===> {G}')
