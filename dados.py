import json
import os 
from datetime import datetime


ARQUIVO = 'progresso.json'
OBJETIVO =450

def carregar():
    if os.path.exists(ARQUIVO):
      with open(ARQUIVO,'r') as f:
         dados = json.load(f)
         return dados.get('guardados',0),dados.get('historico',[])
    return 0,[]


def salvar(guardados,historico):
   with open(ARQUIVO,'w') as f:
      json.dump({'guardados':guardados,'historico':historico},f)

def adicionar_20e(guardados,historico):
   if guardados < OBJETIVO:
      guardados +=1
      historico.append(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
      salvar(guardados,historico)

   return guardados,historico

def desfazer(guardados,historico):
   if guardados >0:
      guardados -=1
      historico.pop()
      salvar(guardados,historico)
    
   return guardados, historico

def resetar():
   salvar(0,[])
   return 0,[]
