import requests
from data import ui
# Api - https://github.com/p0isonBR/ConsultaCPF
def consultar():
	Sair=False
	while(Sair==False):
		cep = int(ui.input_dialog1())
		r = requests.get(url=f'https://viacep.com.br/ws/{cep}/json/')
		if len(cep)!=8:
			msg='CEP inválido'
		try:
			msg='''
CEP - {r["cep"]}
LOGRADOURO - {r['logradouro']}
COMPLEMENTO - {r['complemento']}
BAIRRO - {r['bairro']}
LOCALIDADE - {r['localidade']}
UF - {r['uf']}
IBGE - {r['ibge']}
GIA - {r['gia']}
DDD - {r['ddd']}
SIAFI - {r['siafi']}
'''
		except:
			msg='CEP não encontrado.'
		op=int(ui.input_dialog2(msg))
		if op==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
