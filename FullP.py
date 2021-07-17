import requests
import time
import os 
from colorama import Fore

ciano = "\033[1;36m"
white = "\033[97;1m"
green = "\033[92;1m"
magenta = "\033[1;35m"


def menu():
     
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''{ciano}
- By gav1x
- GitHub: https://github.com/Gav1x
- Greetz: DevNoias - Mr Osama - Bugea1s - Fz1n - Tr4xb0y - V4p0r''')
    
    time.sleep(1.20)
    os.system('cls' if os.name == 'nt' else 'clear')
    option = int(input(f'''
==============================================================================================
Though I walk in the valley of the shadow of death, I will not fear evil, for you are with me.
==============================================================================================

{white}[1] {green}NUMERO\n{white}[2] {green}CPF\n{white}[3] {green}NOME\n{white}[4] {green}PESSOAS CEP\n{white}[5] {green}CEP \n{white}[6] {green}RG\n{white}[7] {green}EMAIL\n\n{magenta}~> '''))
        
    if option == 1:
                
        def numero():
            os.system('cls' if os.name == 'nt' else 'clear')
            numero = input(f'{green}NUMER0 ~> ').strip() 
            os.system('cls' if os.name == 'nt' else 'clear')                
            url = 'https://consulta-numero.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/numero.php'
            params = {'consulta': numero}
            headers = {
                'x-rapidapi-key': '4813835f7cmshff925461946c935p1dec10jsnc4b78a886ea0',
                'x-rapidapi-host': 'consulta-numero.p.rapidapi.com'
            }                
            req = requests.get(url=url, headers=headers, params=params)
            code = req.status_code
            if code == 200:    
                print(req.text)                    
            else:
                    print(Fore.RED + '[!] API OFFLINE')               
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()      
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()        
        if __name__ == '__main__':
            numero()
            
    elif option == 2:    
        def cpf():               
            os.system('cls' if os.name == 'nt' else 'clear')               
            cpf = input(f'{green}DIGITE O CPF SEM PONTOS ~> ').strip()
            if len(cpf) != 11:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + '[!] CPF INVALIDO')
                time.sleep(1)
                menu()
            os.system('cls' if os.name == 'nt' else 'clear')   
            url = 'https://consulta-cpf2.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cpf.php'               
            headers =  {
            'x-rapidapi-key': '4813835f7cmshff925461946c935p1dec10jsnc4b78a886ea0',
            'x-rapidapi-host': 'consulta-cpf2.p.rapidapi.com'
            }                
            params = {'consulta': cpf}                
            req = requests.get(url=url, headers=headers, params=params)
            code = req.status_code
            if code == 200:
                print(req.text)
            else:
                print(Fore.RED + '[!] API OFFLINE')                
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()               
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()               
        if __name__ == '__main__':
            cpf()
                
    elif option == 3:
            
        def nome():        
            os.system('cls' if os.name == 'nt' else 'clear')  
            nome = input(f'{green}NOME ~> ').strip()
            os.system('cls' if os.name == 'nt' else 'clear')  
            url = 'https://consulta-nome1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/nome.php'    
            headers =  {
                'x-rapidapi-key': '4813835f7cmshff925461946c935p1dec10jsnc4b78a886ea0',
                'x-rapidapi-host': 'consulta-nome1.p.rapidapi.com'
            }    
            params = {'consulta': nome}    
            req = requests.get(url=url, headers=headers, params=params)
            code = req.status_code
            if code == 200:
                print(req.text)       
            else:
                print(Fore.RED + '[!] API OFFLINE')   
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()   
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()   
        if __name__ == '__main__':
                nome()
                
    elif option == 4:
            
        def cep():      
            os.system('cls' if os.name == 'nt' else 'clear')  
            cep = input(f'{green}DIGITE O CEP SEM PONTOS ~> ').strip()
            if len(cep) != 8:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + '[!] CEP INVALIDO')
                time.sleep(1)
                menu()              
            os.system('cls' if os.name == 'nt' else 'clear')
            url = 'https://consulta-cep1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cep.php'
            headers =  {
                'x-rapidapi-key': '4813835f7cmshff925461946c935p1dec10jsnc4b78a886ea0',
                'x-rapidapi-host': 'consulta-cep1.p.rapidapi.com'
            }
            params = {'consulta': cep}
            req = requests.get(url=url, headers=headers, params=params)
            code = req.status_code
            if code == 200:
                print(req.text)
            else:
                print(Fore.RED + '[!] API OFFLINE')
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
        if __name__ == '__main__':
            cep()
                
    elif option == 5:
        
        def _cep():
            os.system('cls' if os.name == 'nt' else 'clear')
            cep = input(f'{green}DIGITE O CEP SEM PONTOS ~> ').strip()
            if len(cep) != 8:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + '[!] CEP INVALIDO')
                time.sleep(1)
                menu()
            os.system('cls' if os.name == 'nt' else 'clear')
            url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
            req = requests.get(url=url)
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
                print(Fore.RED + '[!] CEP NÃO ENCONTRADO')
                time.sleep(1)
                menu()
                
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
        if __name__ == '__main__':
            _cep()

    elif option == 6:
                
        def rg():
            os.system('cls' if os.name == 'nt' else 'clear')
            rg = input(f'{green}RG ~> ').strip()
            os.system('cls' if os.name == 'nt' else 'clear')
            url = 'https://consulta-rg.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/rg.php'
            params = {'consulta': rg}
            headers = {
                'x-rapidapi-key': '4813835f7cmshff925461946c935p1dec10jsnc4b78a886ea0',
                'x-rapidapi-host': 'consulta-rg.p.rapidapi.com'
            }
            req = requests.get(url=url, headers=headers, params=params)
            code = req.status_code
            if code == 200:    
                print(req.text)
            else:
                    print(Fore.RED + '[!] API OFFLINE')
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
        if __name__ == '__main__':
            rg()
            
    elif option == 7:
                
        def email():
            os.system('cls' if os.name == 'nt' else 'clear')
            email = input(f'{green}EMAIL ~> ').strip()
            os.system('cls' if os.name == 'nt' else 'clear')
            url = 'https://consulta-e-mail.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/email.php'
            params = {'consulta': email}
            headers = {
                'x-rapidapi-key': '4813835f7cmshff925461946c935p1dec10jsnc4b78a886ea0',
                'x-rapidapi-host': 'consulta-e-mail.p.rapidapi.com'
            }
            req = requests.get(url=url, headers=headers, params=params)
            code = req.status_code
            if code == 200:    
                print(req.text)
            else:
                    print(Fore.RED + '[!] API OFFLINE')
            ret = int(input('\n[?] DESEJA REALIZAR OUTRA CONSULTA?\n\n1 > SIM\n2 > NÃO\n\n~> '))
            if ret == 1:
                menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Saindo....')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
        if __name__ == '__main__':
            email()
            
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + '[!] Opção inválida')
                
if __name__ == '__main__':
    menu()