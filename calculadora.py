def somar(a, b):
    return a + b
 
 
def subtrair(a, b):
    return a - b
 
 
def multiplicar(a, b):
    return a * b
 
 
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida. Escolha outro valor.")
    return a / b
 
 
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")
 
 
def exibir_menu():
    print("\n=== Calculadora ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
 
 
def main():
    operacoes = {
        "1": ("Soma", somar),
        "2": ("Subtração", subtrair),
        "3": ("Multiplicação", multiplicar),
        "4": ("Divisão", dividir),
    }
 
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-5): ").strip()
 
        if escolha == "5":
            print("Encerrando a calculadora. Até mais!")
            break
 
        if escolha not in operacoes:
            print("Opção inválida. Tente novamente.")
            continue
 
        nome_operacao, funcao = operacoes[escolha]
        a = obter_numero("Digite o primeiro número: ")
        b = obter_numero("Digite o segundo número: ")
 
        try:
            resultado = funcao(a, b)
            print(f"{nome_operacao}: {a} e {b} => Resultado: {resultado}")
        except ValueError as erro:
            print(f"Erro: {erro}")
 
 
if __name__ == "__main__":
    main()