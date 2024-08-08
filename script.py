import re #Para trabalhar com expressões regulares
import tkinter as tk #Interface Gráfica

def corrigir_cnpj(cnpj):
    #Remove todos os caracteres indesejados
    cnpj_limpo = re.sub(r'\D', '', cnpj)

    #Verifica se o CNPJ tem 14 dígitos
    if len(cnpj_limpo) != 14:
        return "CNPJ inválido!"
    
    #Formata o CNPJ corretamente
    cnpj_formatado = f"{cnpj_limpo[:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:14]}"

    return cnpj_formatado

def corrigir_cnpj_e_mostrar():
    cnpj_incorreto = entry_incorreto.get()
    cnpj_correto = corrigir_cnpj(cnpj_incorreto)
    entry_correto.delete(0, tk.END)
    entry_correto.insert(0, cnpj_correto)

#Criação da janela principal
root = tk.Tk()
root.title("CNPJ Formatter")

# Define o tamanho da janela (largura x altura)
root.geometry("250x150")

# Impede o redimensionamento da janela
root.resizable(False, False)

# Adicionar ícone ao programa
root.iconbitmap("/cnpj.ico")

# Label e Entry para entrada do CNPJ incorreto
label_incorreto = tk.Label(root, text="Digite o CNPJ incorreto:")
label_incorreto.pack(pady=10)
entry_incorreto = tk.Entry(root)
entry_incorreto.pack(pady=5)

# Entry para mostrar o CNPJ corrigido
entry_correto = tk.Entry(root)
entry_correto.pack(pady=10)

# Botão para corrigir o CNPJ
button = tk.Button(root, text="Corrigir CNPJ", command=corrigir_cnpj_e_mostrar)
button.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()