import math

def calcular_entropia(senha, tamanho_alfabeto):
    """
    Calcula a entropia de uma senha dada o tamanho do alfabeto.
    senha: string ou lista de palavras
    tamanho_alfabeto: número de símbolos possíveis (ex.: 26, 62, 95, 2048)
    """
    comprimento = len(senha) if isinstance(senha, str) else len(senha.split())
    bits_por_caractere = math.log2(tamanho_alfabeto)
    entropia_total = comprimento * bits_por_caractere
    return entropia_total

def classificar_forca(entropia):
    if entropia >= 256:
        return "Nível AES-256 (muito forte)"
    elif entropia >= 192:
        return "Nível AES-192 (forte)"
    elif entropia >= 128:
        return "Nível AES-128 (bom)"
    else:
        return "Abaixo de AES-128 (fraco)"

def main():
    print("=== Calculadora de Entropia de Senhas / Pass Phrases ===")
    senha = input("Digite a senha ou frase: ").strip()
    print("\nEscolha o tipo de conjunto de caracteres usado:")
    print("1 - Apenas letras minúsculas (26)")
    print("2 - Minúsculas + Maiúsculas + Dígitos (62)")
    print("3 - ASCII imprimível (~95 símbolos)")
    print("4 - Palavras de dicionário Diceware (~2048 palavras)")
    
    opcao = input("Opção: ").strip()
    
    if opcao == "1":
        alfabeto = 26
    elif opcao == "2":
        alfabeto = 62
    elif opcao == "3":
        alfabeto = 95
    elif opcao == "4":
        alfabeto = 2048
    else:
        print("Opção inválida.")
        return
    
    entropia = calcular_entropia(senha, alfabeto)
    print(f"\nEntropia estimada: {entropia:.2f} bits")
    print("Classificação:", classificar_forca(entropia))

if __name__ == "__main__":
    main()
