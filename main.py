import os
import sys

if __name__ == "__main__":
    nomeArquivoEntrada = ""
    if len(sys.argv) == 2:
        nomeArquivoEntrada = sys.argv[1]
    else:
        print("Número inválido de argumentos. Informe o arquivo de entrada")
        sys.exit()
    
    ## Roda o analisador léxico
    os.system("python3 analisador-lexico/main.py "+nomeArquivoEntrada)
    os.system("mv analisador-lexico/fluxoDeTokens analisador-sintatico")
    os.system("mv analisador-lexico/tabelaDeSimbolos analisador-sintatico")
    os.system("mv analisador-lexico/tabelaDeTokens analisador-sintatico")
    os.system("python3 analisador-sintatico/analisadorSintatico.py")
