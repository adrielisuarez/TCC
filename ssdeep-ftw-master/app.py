import os
from ssftw import SSFTW

# Caminho para o executável do ssdeep
ssdeep = SSFTW(r"C:\Users\Usuario\Desktop\ssdeep-2.14.1\ssdeep.exe")

def comparar_arquivos(arquivo1, arquivo2):
    print("=" * 50)
    print(f"Comparação SSDEEP entre: {arquivo1}  x  {arquivo2}")
    print("=" * 50)

    # Verificar se os arquivos existem
    if not os.path.exists(arquivo1):
        print(f"[ERRO] Arquivo não encontrado: {arquivo1}")
        return
    if not os.path.exists(arquivo2):
        print(f"[ERRO] Arquivo não encontrado: {arquivo2}")
        return

    # Gerar hashes
    hash1 = ssdeep.hash_from_file(arquivo1)
    hash2 = ssdeep.hash_from_file(arquivo2)

    if not hash1:
        print(f"[ERRO] Não foi possível gerar hash para {arquivo1}")
        return
    if not hash2:
        print(f"[ERRO] Não foi possível gerar hash para {arquivo2}")
        return

    # Exibir hashes
    print(f"Hash SSDEEP de {arquivo1}: {hash1}")
    print(f"Hash SSDEEP de {arquivo2}: {hash2}")

    # Comparar
    similarity = ssdeep.compare(hash1, hash2)
    print(f"\nSimilaridade SSDEEP: {similarity}%")

if __name__ == "__main__":
    # Lista de comparações