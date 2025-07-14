#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jogo de Adivinhação - Script para Teste de Automação
Autor: Assistente IA
Descrição: Jogo interativo onde o usuário tenta adivinhar um número
"""

import random
import time
import os
import sys

class JogoAdivinhacao:
    def __init__(self):
        self.pontuacao = 0
        self.tentativas = 0
        
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_banner(self):
        """Exibe o banner do jogo"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    🎮 JOGO DA ADIVINHAÇÃO 🎮                ║
║                                                              ║
║  Tente adivinhar o número secreto entre 1 e 100!             ║
║  Você tem 5 tentativas. Boa sorte!                           ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def animacao_carregamento(self, duracao=2):
        """Exibe uma animação de carregamento"""
        print("🎲 Preparando o jogo", end="")
        for _ in range(duracao * 10):
            time.sleep(0.1)
            print(".", end="", flush=True)
        print("\n✅ Pronto! Vamos começar!\n")
    
    def validar_entrada(self, entrada):
        """Valida se a entrada é um número válido"""
        try:
            numero = int(entrada)
            return 1 <= numero <= 100, numero
        except ValueError:
            return False, None
    
    def dar_dica(self, tentativa, numero_secreto):
        """Fornece dicas baseadas na tentativa"""
        if tentativa < numero_secreto:
            if numero_secreto - tentativa <= 10:
                return "🔥 Quente! Tente um pouco mais alto!"
            elif numero_secreto - tentativa <= 25:
                return "🌡️ Morno! Vá um pouco mais alto!"
            else:
                return "❄️ Frio! Muito baixo!"
        else:
            if tentativa - numero_secreto <= 10:
                return "🔥 Quente! Tente um pouco mais baixo!"
            elif tentativa - numero_secreto <= 25:
                return "🌡️ Morno! Vá um pouco mais baixo!"
            else:
                return "❄️ Frio! Muito alto!"
    
    def calcular_pontuacao(self, tentativas_usadas):
        """Calcula a pontuação baseada nas tentativas"""
        pontuacao_base = 1000
        penalidade_por_tentativa = 50
        return max(100, pontuacao_base - (tentativas_usadas - 1) * penalidade_por_tentativa)
    
    def jogar_rodada(self):
        """Executa uma rodada do jogo"""
        numero_secreto = random.randint(1, 100)
        tentativas_usadas = 0
        max_tentativas = 5
        
        print(f"\n🎯 O número secreto foi escolhido!")
        print(f"📊 Você tem {max_tentativas} tentativas\n")
        
        while tentativas_usadas < max_tentativas:
            tentativas_restantes = max_tentativas - tentativas_usadas
            print(f"🎲 Tentativas restantes: {tentativas_restantes}")
            
            entrada = input("💭 Digite seu palpite (1-100): ").strip()
            
            if entrada.lower() in ['sair', 'exit', 'quit']:
                print("👋 Até logo!")
                return False
            
            valido, tentativa = self.validar_entrada(entrada)
            
            if not valido:
                print("❌ Por favor, digite um número entre 1 e 100!")
                continue
            
            tentativas_usadas += 1
            
            if tentativa == numero_secreto:
                pontuacao = self.calcular_pontuacao(tentativas_usadas)
                self.pontuacao += pontuacao
                
                print(f"\n🎉 PARABÉNS!")
                print(f"🎯 Você acertou em {tentativas_usadas} tentativas!")
                print(f"🏆 Pontuação desta rodada: {pontuacao}")
                print(f"💰 Pontuação total: {self.pontuacao}")
                
                return True
            
            else:
                dica = self.dar_dica(tentativa, numero_secreto)
                print(f"💡 {dica}")
                
                if tentativas_usadas == max_tentativas:
                    print(f"\n😔 Game Over! O número era {numero_secreto}")
                    return False
                
                print()  # Linha em branco para separar
        
        return False
    
    def menu_principal(self):
        """Exibe o menu principal do jogo"""
        while True:
            self.limpar_tela()
            self.mostrar_banner()
            
            print(f"💰 Pontuação Total: {self.pontuacao}")
            print("\n" + "=" * 50)
            print("📋 MENU PRINCIPAL:")
            print("1. 🎮 Jogar")
            print("2. ❌ Sair")
            print("=" * 50)
            
            opcao = input("🎯 Escolha uma opção (1-2): ").strip()
            
            if opcao == "1":
                self.jogar_rodada()
                input("\n⏸️  Pressione ENTER para continuar...")
            
            elif opcao == "2":
                print("👋 Obrigado por jogar! Até a próxima!")
                break
            
            else:
                print("❌ Opção inválida! Tente novamente.")
                time.sleep(1)
    
    def executar(self):
        """Método principal que executa o jogo"""
        try:
            self.limpar_tela()
            self.mostrar_banner()
            self.animacao_carregamento()
            self.menu_principal()
            
        except KeyboardInterrupt:
            print("\n\n👋 Jogo interrompido pelo usuário. Até logo!")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("🔧 Entre em contato com o suporte técnico.")

def main():
    """Função principal"""
    print("🚀 Iniciando Jogo da Adivinhação...")
    jogo = JogoAdivinhacao()
    jogo.executar()

if __name__ == "__main__":
    main()
