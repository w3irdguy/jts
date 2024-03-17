#!usr/bin/env python3
r = "\033[0;49;91m"                                                  
g = "\033[0;49;92m"
y = "\033[0;49;93m"
b = "\033[0;49;94m"                                                  
p = "\033[0;49;95m"
b2 = "\033[0;49;96m"
d = "\033[2;37m"
w = "\033[0m"
espaco = ""
linhas = espaco + "_"*9
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}
import phonenumbers
import os
import json
import time
import math
import phonenumbers
import requests
import pprint
import http.client
import re, sys, textwrap, socket
from lxml.html import fromstring
from getpass import getpass
from shutil import which
os.system("clear")
def banner():
        print(f"""{r}
  888888 88888888888  .d8888b.
    "88b     888     d88P  Y88b
     888     888     Y88b.
     888     888      "Y888b.
     888     888         "Y88b.
     888     888           "888
     88P     888     Y88b  d88P
     888     888      "Y8888P"
   .d88p                      :-:  .:---=
  .d88p"                      @@@@@@@@@@@=
 888P"                       #@@@@@@@@@@@@
                            -@@@@@@@@@@@@@@

                           :+#@@@@@@@@@@@%*-          
                       +@@@@@@@@@@@@@@@@@@@@@@@#:      
                            :+*+:     .+**-         
                          :%+   +@-=-%#.  -@=        
                          ++     *@:*@.    :%         
                          :%+   +@: .%#.  -@=        
                            :+#+-     :=#*-        
        \033[m""")
def name():
	try:
		print(f"{b2} Ex: lucas\033[m")
		nome = input(f"{r} Digite o nome: {g} ")
		url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
		req = requests.get(url)
		info = req.json()
		nome = info[0]['nome']
		loc = info[0]['localidade']
		freq = info[0]['res'][8]['frequencia']
		mp = info[0]['res'][8]['periodo']
		print(f"{r} Nome Selecionado:{g} {nome}")
		print(f"{r} Localidade:{g} {loc}")
		print(f"{r} Maior Frequência:{g} {freq}")
		print(f"{r} Perído Da Maior Frequência:{g} {mp}")
		print("")
		nname1 = input(f"{r} Digite o 1° nome: {g} \033[m\033[m")
		nname2 = input(f"{r} Digite o 2° nome: {g} \033[m\033[m")
		nname3 = input(f"{r} Digite o 3° nome: {g} \033[m\033[m")
		nname5 = input(f"{r} Digite o 4° nome: {g} \033[m\033[m")
		os.system(f"xdg-open https://portaldatransparencia.gov.br/busca?termo={nname1}-{nname2}-{nname3}-{nname5}")
	except:
		nname1 = input(f"{r} Nome não encontrado!")
	
def social():
        try:
                username = input(f"{r} Digite o @: {g} \033[m\033[m")
                time.sleep(0.5)
                print("""
                200 - Encontrado 
                404 - Não Encontrado 
                403 - Acesso Negado
                """)
                print("")
                input(">Enter<")
                print(f"{r} Procurando Nome de usuário em 65 sites...\033[m")
                time.sleep(1)
                urllist = [
                     "https://facebook.com/{}",
                     "https://instagram.com/{}",
                     "https://twitter.com/{}",
                     "https://youtube.com/{}",
                     "https://vimeo.com/{}",
                     "https://github.com/{}",
                     "https://plus.google.com/{}",
                     "https://pinterest.com/{}",
                     "https://flickr.com/people/{}",
                     "https://vk.com/{}",
                     "https://about.me/{}",
                     "https://disqus.com/{}",
                     "https://bitbucket.org/{}",
                     "https://flipboard.com/@{}",
                     "https://medium.com/@{}",
                     "https://hackerone.com/{}",
                     "https://keybase.io/{}",
                     "https://buzzfeed.com/{}",
                     "https://slideshare.net/{}",
                     "https://mixcloud.com/{}",
                     "https://soundcloud.com/{}",
                     "https://badoo.com/en/{}",
                     "https://imgur.com/user/{}",
                     "https://open.spotify.com/user/{}",
                     "https://pastebin.com/u/{}",
                     "https://wattpad.com/user/{}",
                     "https://canva.com/{}",
                     "https://codecademy.com/{}",
                     "https://last.fm/user/{}",
                     "https://blip.fm/{}",
                     "https://dribbble.com/{}",
                     "https://en.gravatar.com/{}",
                     "https://foursquare.com/{}",
                     "https://creativemarket.com/{}",
                     "https://ello.co/{}",
                     "https://cash.me/{}",
                     "https://angel.co/{}",
                     "https://500px.com/{}",
                     "https://houzz.com/user/{}",
                     "https://tripadvisor.com/members/{}",
                     "https://kongregate.com/accounts/{}",
                     "https://{}.blogspot.com/",
                     "https://{}.tumblr.com/",
                     "https://{}.wordpress.com/",
                     "https://{}.devianart.com/",
                     "https://{}.slack.com/",
                     "https://{}.livejournal.com/",
                     "https://{}.newgrounds.com/",
                     "https://{}.hubpages.com",
                     "https://{}.contently.com", 
                     "https://steamcommunity.com/id/{}",
                     "https://www.wikipedia.org/wiki/User:{}",
                     "https://www.freelancer.com/u/{}",
                     "https://www.dailymotion.com/{}",
                     "https://www.etsy.com/shop/{}",
                     "https://www.scribd.com/{}",
                     "https://www.patreon.com/{}",
                     "https://www.behance.net/{}",
                     "https://www.goodreads.com/{}",
                     "https://www.gumroad.com/{}",
                     "https://www.instructables.com/member/{}",
                     "https://www.codementor.io/{}",
                     "https://www.reverbnation.com/{}",
                     "https://www.designspiration.net/{}",
                     "https://www.bandcamp.com/{}",
                     "https://www.colourlovers.com/love/{}",
                     "https://www.ifttt.com/p/{}",
                     "https://www.trakt.tv/users/{}",
                     "https://www.okcupid.com/profile/{}",
                     "https://www.trip.skyscanner.com/user/{}",
                     "http://www.zone-h.org/archive/notifier={}",
                ]
                print(w+linhas)
                for url in urllist:
                        try:
                              req = requests.get(url.format(username), headers=headers)
                              if req.status_code == 200: color = b2
                              elif req.status_code == 404: color = y
                              else: color = r
                              print(f"{espaco}{p}>>>{color}{req.status_code}{p}<<< {w}{url.format(username)}")
                        except requests.exceptions.Timeout: continue
                        except requests.exceptions.TooManyRedirects: continue
                        except requests.exceptions.ConnectionError: break
                        print(w+linhas)
        except:
                  print(f"{r} Erro Inesperado!\033[m")

def nmr():
        try:
                print(f"{b2} Ex: +558299XXXXXX\033[m")
                nmrbr = input(f"{r} Digite o número: {g} \033[m\033[m")
                from phonenumbers import geocoder
                from phonenumbers import carrier
                pm = phonenumbers.parse(f"{nmrbr}")
                op = carrier.name_for_number(pm, 'pt-br')
                es = geocoder.description_for_number(pm, 'pt-br')
                print(f"{r} Número: {g} {pm}\033[m")
                print(f"{r} Localidade: {g} {es}\033[m")
                print(f"{r} Operadora: {g} {op}\033[m")
        except:
                   print(f"{r} Telefone não encontrado :(\033[m")
def cep():
	os.system("bash cepsearch.sh")
def sites():
	try:
		while True:
			os.system("clear")
			banner()
			print(f"{r} <01> {y} Webmii")
			print(f"{r} <02> {y} Face Check")
			print(f"{r} <03> {y} Info Space")
			print(f"{r} <04> {y} Ip Lookup")
			print(f"{r} <05> {y} PeekYou")
			print(f"{r} <06> {y} KRAK")
			print("")
			print(f"{g} <00> {y} Exit")
			print("")
			resp = int(input(f"{r} Opção: {g}"))
			if(resp == 1):
				os.system("xdg-open https://webmii.com")
				continue
			elif(resp == 2):
				os.system("xdg-open https://facecheck.id")
				continue
			elif(resp == 3):
				os.system("xdg-open https://www.infospace.com/")
				continue
			elif(resp == 4):
				os.system("xdg-open https://www.iplocation.net/ip-lookup")
				continue
			elif(resp == 5):
				os.system("xdg-open https://www.peekyou.com/")
				continue
			elif(resp == 6):
				os.systemc("xdg-open https://www.krak.dk/")
				continue
			elif(resp == 0):
				os.system("python johnny.py")
				break
			else:
				print(f"{r} Arg. Inválido!")
				time.sleep(1)
				continue
	except (KeyboardInterrupt):
			print(f"{r} Dont leave me here alone!!!")
			
def cidade():
    print(f"{r} Ex: {y} sao paulo")
    cdd = input(f"{r} Digite a cidade:{y} ")
    llnow = cdd.replace(" ", "-")
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{llnow}"
    req = requests.get(url)
    arq = req.json()
    id = arq['id']
    sgestado = arq['microrregiao']['mesorregiao']['UF']['sigla']
    estado = arq['microrregiao']['mesorregiao']['UF']['nome']
    regiao = arq['microrregiao']['mesorregiao']['UF']['regiao']['nome']
    sgregiao = arq['microrregiao']['mesorregiao']['UF']['regiao']['sigla']
    loc = arq['microrregiao']['mesorregiao']['nome']
    cidade = arq['nome']
    print(f"{r} Cidade: {y} {cidade}")
    print(f"{r} ID: {y} {id}")
    print(f"{r} Sigla do Estado: {y} {sgestado}")
    print(f"{r} Estado: {y} {estado}")
    print(f"{r} Região: {y} {regiao}")
    print(f"{r} Sigla Da Região: {y} {sgregiao}")
    print(f"{r} Localização: {y} {loc}")

def menu():
        while True:
                        os.system("clear")
                        banner()
                        print("")
                        print(f"{r} <01> {y} Cons. Nome")
                        print(f"{r} <02> {y} Cons. Usuário")
                        print(f"{r} <03> {y} Cons. Número")
                        print(f"{r} <04> {y} Cons. CEP")
                        print(f"{r} <05> {y} Extra Sites >:)")
                        print(f"{r} <06> {y} Cons. Cidade IBGE")
                        print("")
                        print(f"{g} <00> {y} Exit")
                        print("")
                        resp = int(input(f"{w} Opção: {g} \033[m"))
                        if(resp == 1):
                                name()
                                input(f">Enter<")
                                continue
                        elif(resp == 6):
                            cidade()
                            input(">Enter<")
                            continue
                        elif(resp == 2):
                                social()
                                input(f">Enter<")                                                                                                                             
                                continue
                        elif(resp == 3):
                                nmr()
                                input(f">Enter<")
                                continue
                        elif(resp == 4):
                                cep()
                                break
                        elif(resp == 5):
                                sites()
                                break
                        elif(resp == 0):
                                print(f"{y} Programa encerrado.\033[m")
                                break
                        else:
                                print(f"{y} OPÇÃO 1NV4L1DA!!!!\033[m")
                                time.sleep(1)
                                continue
try:
	menu()
except (KeyboardInterrupt):
	print(f"{g} De uma conferida nos meus outros projetos!\033[m")
	os.system("sleep 1")
	os.system("xdg-open https://github.com/z4kc?tab=repositories")
