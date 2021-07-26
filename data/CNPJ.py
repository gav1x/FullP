import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cnpj = ui.dialog1()
		r=requests.get(url=f'https://consulta-cnpj-gratis.p.rapidapi.com/companies/{cnpj}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key':'574b13cadbmsh76d5927b45dc8cep17d937jsn0eb56f2d5a5c','x-rapidapi-host': 'consulta-cnpj-gratis.p.rapidapi.com'},params={'consulta': cnpj})
		if 'A consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o CNPJ inserido não foi encontrado.'
		else:
			msg=f'''
Nome - {r['name']}
Apelido - {r['alias']}
CNPJ - {r['tax_id']}
Modelo Federal - {r['type']}
Fundado - {r['founded']}
Tamanho - {r['size']}
Capital -{r['capital']
Email - {r['email']}
Telefone - {r['phone']}
Telefone Alternativo - {r['phone_alt']}
Entidade Federal - {r['federal_entity']
			'''
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
