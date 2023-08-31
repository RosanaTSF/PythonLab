class Banco:
    LIMITE_SAQUES_POR_DIA = 3 
    LIMITE_SAQUE = 500  # Constantes.

    def __init__(self):
        self.saldo = 0  
        self.saques_feitos = 0  # Inicializa o contador de saques.
        self.operacoes = []  # Lista para armazenar as operações realizadas.
    
    def deposito(self, valor):
        self.saldo += valor  
        self.operacoes.append(f"Deposito de R${valor:.2f}")  # Adiciona a operação no(append=final da list).
        print(f"Deposito realizado. Novo saldo: R${self.saldo:.2f}")
    
    def saque(self, valor):
        
        if self.saques_feitos < self.LIMITE_SAQUES_POR_DIA and valor <= self.LIMITE_SAQUE and valor <= self.saldo:
            self.saldo -= valor  # Subtrai do saldo.
            self.saques_feitos += 1  # Incrementa o contador de saques.
            self.operacoes.append(f"Saque de R${valor:.2f}")  # Adiciona a operação à lista.
            print(f"Saque realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            if self.saques_feitos >= self.LIMITE_SAQUES_POR_DIA:
                print("Limite maximo de saques por dia ja foi atingido. Volte amanha!")
            elif valor > self.LIMITE_SAQUE:
                print(f"Valor maximo de saque: R${self.LIMITE_SAQUE:.2f}.")
            else:
                print("Saldo insuficiente.")
    
    def extrato(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("Extrato:")
        for operacao in self.operacoes:
            print(operacao)  # Exibe as operações realizadas.

    def reiniciar_dia(self):
        self.saques_feitos = 0  #Zera o contador de saques.
        self.operacoes = []  #Reinicia a lista de operações.
        print("Novo dia! Saques reiniciados.")

def exibir_menu():
    print("\n1. Deposito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Reiniciar dia")
    print("5. Sair")

def main():
    banco = Banco()  #Cria uma instância da classe Banco.

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor a depositar: "))
            banco.deposito(valor_deposito)
        elif opcao == 2:
            valor_saque = float(input("Digite o valor a sacar: "))
            banco.saque(valor_saque)
        elif opcao == 3:
            banco.extrato()
        elif opcao == 4:
            banco.reiniciar_dia()
        elif opcao == 5:
            print("Fim.")
            break
        else:
            print("Opção invalida. Escolha uma opcao valida.")

if __name__ == "__main__":
    main()  # Inicia a função principal se o script for executado diretamente.



