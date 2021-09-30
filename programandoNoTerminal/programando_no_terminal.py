name = input("File name: ") # pergunta o nome do arquivo já com a extensão
print() # pula a linha
while True: # é rodado até ser interrompido por um break
    with open(name, "a") as arquivo: # abre o arquivo (ou cria) com o nome e acrescenta coisas nele, e isso será chamado de arquivo
        code = input() # está pronto para você digitar
        if code == "end": # se o que eu digitei for igual a end
            break # interrompe o while True
        else: # se eu não digitar end
            arquivo.write(str(code) + "\n") # adiciona o que eu digitei no arquivo e pula uma linha
