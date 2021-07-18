import requests
import os
import time
from colorama import Fore


def banner():
    
    print(Fore.RED + '''
- By gav1x
- GitHub: https://github.com/Gav1x
- Greetz: DevNoias - Mr Osama - Bugea1s - Fz1n - Tr4xb0y - V4p0r''')

def limpar():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
def numero():

    limpar(); numero: str = (input('NUMERO ~> ')); limpar()
    url: str = 'https://consulta-numero.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/numero.php'
    params: str = {'consulta': numero}
    headers: str = {
    'x-rapidapi-key': 'a5c0d365camshf9426e6fe320fabp1aaeb0jsnb37aee595857',
    'x-rapidapi-host': 'consulta-numero.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    code: int = req.status_code
    if code == 200:
        print(req.text)
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()

def cpf():

    limpar(); cpf: str = (input('DIGITE O CPF SEM PONTOS ~> ')); limpar()
    if len(cpf) != 11:
        print('[!] CPF INVALIDO'); time.sleep(1); limpar()
        buscar()
        
    url: str = 'https://consulta-cpf2.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cpf.php'
    params: str = {'consulta': cpf}
    headers: str = {
    'x-rapidapi-key': 'a5c0d365camshf9426e6fe320fabp1aaeb0jsnb37aee595857',
    'x-rapidapi-host': 'consulta-cpf2.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    code: int = req.status_code
    if code == 200:
        print(req.text)
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()
        
def nome():

    limpar(); nome: str = (input('NOME ~> ')); limpar()
    url: str = 'https://consulta-nome1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/nome.php' 
    params: str = {'consulta': nome}
    headers: str = {
    'x-rapidapi-key': 'a5c0d365camshf9426e6fe320fabp1aaeb0jsnb37aee595857',
    'x-rapidapi-host': 'consulta-nome1.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    code: int = req.status_code
    if code == 200:
        print(req.text)
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()

def p_cep():

    limpar(); cep: str = (input('DIGITE O CEP SEM PONTOS ~> ')); limpar()
    if len(cep) != 8:
        print('[!] CEP INVALIDO'); time.sleep(1); limpar()
        buscar()
    
    url: str = 'https://consulta-cep1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cep.php'
    params: str = {'consulta': cep}
    headers: str = {
    'x-rapidapi-key': 'a5c0d365camshf9426e6fe320fabp1aaeb0jsnb37aee595857',
    'x-rapidapi-host': 'consulta-cep1.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    code: int = req.status_code
    if code == 200:
        print(req.text)
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()
        
def cep():

    limpar(); cep: str = (input('DIGITE O CEP SEM PONTOS ~> ')); limpar()
    if len(cep) != 8:
        print('[!] CEP INVALIDO'); time.sleep(1); limpar()
        buscar()
    
    url: str = 'https://viacep.com.br/ws/{}/json/'.format(cep)     
    req: str = requests.get(url=url)
    
    data = req.json()
    if 'erro' not in data:
        print('\n[CEP] {}'.format(data["cep"]))
        print('[LOGRADOURO] {}'.format(data['logradouro']))
        print('[COMPLEMENTO] {}'.format(data['complemento']))
        print('[BAIRRO] {}'.format(data['bairro']))
        print('[LOCALIDADE] {}'.format(data['localidade']))
        print('[UF] {}'.format(data['uf']))
        print('[IBGE] {}'.format(data['ibge']))
        print('[GIA] {}'.format(data['gia']))
        print('[DDD] {}'.format(data['ddd']))
        print('[SIAFI] {}'.format(data['siafi']))

    else:
        print('[!] CEP NAO ENCONTRADO'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()

def rg():

    limpar(); rg: str = (input('DIGITE O RG SEM PONTOS ~> ')); limpar()
    url: str = 'https://consulta-rg.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/rg.php'
    params: str = {'consulta': rg}
    headers: str = {
    'x-rapidapi-key': 'a5c0d365camshf9426e6fe320fabp1aaeb0jsnb37aee595857',
    'x-rapidapi-host': 'consulta-rg.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    code: int = req.status_code
    if code == 200:
        print(req.text)
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()
        
def email():

    limpar(); email: str = (input('EMAIL ~> ')); limpar()
    url: str = 'https://consulta-e-mail.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/email.php'
    params: str = {'consulta': email}
    headers: str = {
    'x-rapidapi-key': 'a5c0d365camshf9426e6fe320fabp1aaeb0jsnb37aee595857',
    'x-rapidapi-host': 'consulta-e-mail.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    code: int = req.status_code
    if code == 200:
        print(req.text)
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()
        
def cnpj():

    limpar(); cnpj: str = (input('DIGITE O CNPJ SEM PONTOS ~> ')); limpar()
    url: str = 'https://consulta-cnpj-gratis.p.rapidapi.com/companies/{}'.format(cnpj)
    params: str = {'consulta': cnpj}
    headers: str = {
    'x-rapidapi-key': '574b13cadbmsh76d5927b45dc8cep17d937jsn0eb56f2d5a5c',
    'x-rapidapi-host': 'consulta-cnpj-gratis.p.rapidapi.com'
    }     
    req: str = requests.get(url=url, headers=headers, params=params)
    
    data = req.json()
    if 'error' not in data:
        print(Fore.GREEN + '\n[+] nome: {}'.format(data['name']))
        print('[+] apelido: {}'.format(data['alias']))
        print('[+] cnpj: {}'.format(data['tax_id']))
        print('[+] modelo federal: {}'.format(data['type']))
        print('[+] fundado: {}'.format(data['founded']))
        print('[+] tamanho: {}'.format(data['size']))
        print('[+] capital: {}'.format(data['capital']))
        print('[+] email: {}'.format(data['email']))
        print('[+] telefone: {}'.format(data['phone']))
        print('[+] telefone alternativo: {}'.format(data['phone_alt']))
        print('[+] entidade federal: {}\n'.format(data['federal_entity']))
        
    else:
        print('[!] API OFFLINE'); time.sleep(1); limpar()
        buscar()
        
        
    nova_consulta: int = input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> ') 
    if nova_consulta == '1':
        buscar()    
    
    else:
        limpar(); print('Saindo....'); time.sleep(1); limpar()
        exit()
  
def buscar():

    ##CORES
    white = "\033[97;1m"
    green = "\033[92;1m"
    magenta = "\033[1;35m"

    limpar(); banner()
    
    option: int = input(f'\n{white}[1] {green}NUMERO\n{white}[2] {green}CPF\n{white}[3] {green}NOME\n{white}[4] {green}PESSOAS CEP\n{white}[5] {green}CEP \n{white}[6] {green}RG\n{white}[7] {green}EMAIL\n{white}[8] {green}CNPJ\n\n{magenta}~> ')
    if option == '1':
        numero()
    
    elif option == '2':
        cpf()
        
    elif option == '3':
        nome()

    elif option == '4':
        p_cep()
        
    elif option == '5':
        cep()

    elif option == '6':
        rg()
        
    elif option == '7':
        email()
        
    elif option == '8':
        cnpj()
            
    else:
        limpar(); print('[!] OPCAO INVALIDA'); time.sleep(1); limpar()
        buscar()
       
if __name__ == '__main__':
    buscar()
