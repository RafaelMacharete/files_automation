import os
from datetime import datetime

caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads") # C:\Users\seu_nome\Downloads
caminho_documentos = os.path.join(os.path.expanduser("~"), "Documents") # C:\User\seu_nome\Documents

nova_pasta = os.path.join(caminho_documentos, "ARQUIVOS_CRIADOS_A_UM_MES_OU_MAIS") # C:\User\seu_nome\Documents\ARQUIVOS_CRIADOS_A_UM_MES_OU_MAIS

def calcular_tempo_em_meses(creation_time):
    data_criacao = datetime.fromtimestamp(creation_time) #Tempo em segundos
    data_atual = datetime.now()

    anos = data_atual.year - data_criacao.year
    meses = data_atual.month - data_criacao.month
    return anos * 12 + meses

try:
    os.mkdir(nova_pasta)
    print(f"Pasta criada: {nova_pasta}")
except FileExistsError:
    print(f"Pasta já existe: {nova_pasta}")

items = os.listdir(caminho_downloads)

for item in items:
    caminho_arquivo = os.path.join(caminho_downloads, item) # C:\User\seu_nome\Downloads\arquivo

    if os.path.isfile(caminho_arquivo):
        tempo_criacao = os.path.getctime(caminho_arquivo) 
        meses = calcular_tempo_em_meses(tempo_criacao)
        # print(f"Arquivo: {item} - Tempo desde criação: {meses} meses")

        if meses >= 1:
            destino = os.path.join(nova_pasta, item)
            os.rename(caminho_arquivo, destino)
            # print(f"Arquivo {item} movido para {nova_pasta}")

    elif os.path.isdir(caminho_arquivo):
        tempo_criacao = os.path.getctime(caminho_arquivo)
        meses = calcular_tempo_em_meses(tempo_criacao)
        # print(f"Pasta: {item} - Tempo desde criação: {meses} meses")
        

        if meses > 1:
            destino = os.path.join(nova_pasta, item)
            os.rename(caminho_arquivo, destino)
            # print(f"Pasta {item} movida para {nova_pasta}")