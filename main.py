import os
from datetime import datetime

def calcular_tempo_em_meses(creation_time):
    data_criacao = datetime.fromtimestamp(creation_time) # Tempo em segundos
    data_atual = datetime.now()

    anos = data_atual.year - data_criacao.year
    meses = data_atual.month - data_criacao.month
    return anos * 12 + meses

caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads") # C:\Users\Rafael M\Downloads
print(caminho_downloads)

caminho_documentos = os.path.join(os.path.expanduser("~"), "Documents") # C:\User\seu_nome\Documents

PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS = os.path.join(caminho_documentos, "ARQUIVOS_CRIADOS_MAIS_DE_UM_MES") # C:\User\seu_nome\Documents\ARQUIVOS_CRIADOS_A_UM_MES_OU_MAIS

try:
    os.mkdir(PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS)
    print(f"A pasta {PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS} foi criada")
except FileExistsError:
    print(f"A pasta {PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS} já existe")

todos_arquivos_diretorio_download = os.listdir(caminho_downloads)

for item in todos_arquivos_diretorio_download:
    caminho_arquivo = os.path.join(caminho_downloads, item) # C:\User\seu_nome\Downloads\arquivo

    if os.path.isfile(caminho_arquivo):
        tempo_criacao = os.path.getctime(caminho_arquivo) 
        meses_arquivo = calcular_tempo_em_meses(tempo_criacao)
        print(f"Arquivo: {item} - Tempo desde criação: {meses_arquivo} meses")

        if meses_arquivo > 1: # Mover o arquivo para a pasta em documentos
            destino = os.path.join(PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS, item)
            os.rename(caminho_arquivo, destino)
            print(f"Arquivo {item} movido para {PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS}")

    elif os.path.isdir(caminho_arquivo):
        tempo_criacao = os.path.getctime(caminho_arquivo)
        meses_arquivo = calcular_tempo_em_meses(tempo_criacao)
        print(f"Pasta: {item} - Tempo desde criação: {meses_arquivo} meses")
        

        if meses_arquivo > 1: # Mover a pasta para a pasta em documentos
            destino = os.path.join(PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS, item)
            os.rename(caminho_arquivo, destino)
            print(f"Pasta {item} movida para {PASTA_DOS_ARQUIVOS_A_SEREM_MOVIDOS}")