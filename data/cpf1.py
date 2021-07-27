import requests
from data import ui
Sair=False
while(Sair==False):
	def consultar():
		cep = int(ui.input_dialog1())
		r = requests.get(url='https://consulta-cep1.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/cep.php', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key': '0d66cf70c4msh8e71af69887c685p1a9b2fjsn8fc892e8b730','x-rapidapi-host': 'consulta-cep1.p.rapidapi.com'}, params={'consulta': cep})
		if len(cep)!=8:
			msg='CEP inválido'
		elif 'Por Favor' in r:
			msg='A consulta está funcionando normalmente, mas o CEP inserido não foi encontrado.'
		else:
			msg=r.replace('<br>', '\n').replace('<p>', '')
		op=int(ui.input_dialog2(msg))
		if op==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
