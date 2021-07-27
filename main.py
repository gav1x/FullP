import os, sys
def restart():
	python=sys.executable;os.excl(python, python, *sys.argv)
try:
	import colorama, requests
except:
	os.system('pip install -r requirements.txt');restart()
try:
	from data import ui, numero, cpf, nome, rg, email
except Exception as e:
	print('ARQUIVO CORROMPIDO! '+str(e));exit()
C= "\033[97;1m"
G = "\033[92;1m"
P = "\033[1;35m"
Sair=False
while(Sair==False):
	try:
		op=int(ui.menu(ms0=f'\n{C}[{G}1{C}] Numero\n{C}[{G}2{C}] CPF\n{C}[{G}3{C}] Nome\n{C}[{G}4{C}] RG\n{C}[{G}5{C}] EMAIL\n{C}\n[{P}0{C}] Sair'))
		if op==1:
			numero.consultar()
		elif op==2:
			cpf.consultar()
		elif op==3:
			nome.consultar()
		elif op==4:
			rg.consultar()
		elif op==5:
			email.consultar()
		elif op==0:
			ui.clear();Sair=True
	except:
		ui.error()
