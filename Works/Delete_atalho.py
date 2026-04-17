import os


def excluir_atalho(nome_atalho):
    # Nome do arquivo .lnk
    atalho = nome_atalho if nome_atalho.endswith('.lnk') else nome_atalho + '.lnk'

    # Caminhos possíveis da área de trabalho
    desktop_usuario = os.path.join(os.path.expanduser("~"), "Desktop")
    desktop_publico = r"C:\Users\Public\Desktop"

    caminhos = [
        os.path.join(desktop_usuario, atalho),
        os.path.join(desktop_publico, atalho)
    ]

    encontrado = False
    
    for caminho in caminhos:
        if os.path.exists(caminho):
            os.remove(caminho)
            print(f"Atalho removido: {caminho}")
            encontrado = True

    if not encontrado:
        print("Atalho não encontrado em nenhum local.")

# Exemplo de uso:
excluir_atalho("Notepad++")  # sem .lnk ou com .lnk, funciona dos dois jeitos