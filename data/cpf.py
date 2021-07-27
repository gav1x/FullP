import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cpf = ui.dialog1()
		r = requests.get(url='https://consulta-cpf2.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cpf.php', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key': '9353b1d886msh73e7a0771d6600dp14ec4cjsn883fd8b4cf13','x-rapidapi-host': 'consulta-cpf2.p.rapidapi.com'}, params={'consulta': cpf}).text
		if 'A Consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o CPF inserido não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n').replace('CPF', '\nCPF')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
