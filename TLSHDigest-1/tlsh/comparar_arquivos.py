import tlsh
import os


def calcular_porcentagem_similaridade(distancia, limite=200):
    """Transforma a distância TLSH em porcentagem de similaridade"""
    if distancia < 0:
        return 0
    if distancia >= limite:
        return 0
    return round(100 * (1 - (distancia / limite)), 2)


def comparar_arquivos(arquivo1, arquivo2):
    print("=" * 50)
    print("Comparação TLSH entre Arquivos")
    print("=" * 50)
    print()

    # Verificar se os arquivos existem
    if not os.path.exists(arquivo1):
        print(f"Erro: Arquivo {arquivo1} não encontrado!")
        return

    if not os.path.exists(arquivo2):
        print(f"Erro: Arquivo {arquivo2} não encontrado!")
        return

    try:
        # Ler os arquivos
        print(f"Carregando {arquivo1}...")
        with open(arquivo1, 'rb') as f:
            dados1 = f.read()

        print(f"Carregando {arquivo2}...")
        with open(arquivo2, 'rb') as f:
            dados2 = f.read()

        print(f"Tamanho de {arquivo1}: {len(dados1)} bytes")
        print(f"Tamanho de {arquivo2}: {len(dados2)} bytes")
        print()

        # Gerar hashes TLSH
        print("Gerando hashes TLSH...")
        hash1 = tlsh.hash(dados1)
        hash2 = tlsh.hash(dados2)

        if not hash1:
            print(f"Erro: Não foi possível gerar hash para {arquivo1}")
            return
        if not hash2:
            print(f"Erro: Não foi possível gerar hash para {arquivo2}")
            return

        print(f"Hash TLSH de {arquivo1}: {hash1}")
        print(f"Hash TLSH de {arquivo2}: {hash2}")
        print()

        # Comparar os hashes
        distancia = tlsh.diff(hash1, hash2)
        similaridade = calcular_porcentagem_similaridade(distancia)

        print("=" * 50)
        print("RESULTADO DA COMPARAÇÃO")
        print("=" * 50)
        print(f"Distância TLSH entre os arquivos: {distancia}")
        print(f"Similaridade estimada: {similaridade}%")
        print()

        # Interpretar
        if similaridade == 100:
            print(
                "🟢 IDÊNTICOS: Os arquivos são iguais ou extremamente similares"
            )
        elif similaridade >= 75:
            print("🟢 MUITO SIMILARES")
        elif similaridade >= 50:
            print("🟡 SIMILARES")
        elif similaridade >= 25:
            print("🟠 POUCO SIMILARES")
        else:
            print("🔴 DIFERENTES")

    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")


if __name__ == "__main__":
    # Comparar os arquivos
    comparar_arquivos("audio1.mp3", "audio1-5.mp3")
    comparar_arquivos("audio2.mp3", "audio2-5.mp3")
    comparar_arquivos("audio3.mp3", "audio3-5.mp3")
    comparar_arquivos("audio4.mp3", "audio4-5.mp3")
    comparar_arquivos("audio5.mp3", "audio5-5.mp3")
    comparar_arquivos("audio6.mp3", "audio6-5.mp3")
    comparar_arquivos("audio7.mp3", "audio7-5.mp3")
    comparar_arquivos("audio8.mp3", "audio8-5.mp3")
    comparar_arquivos("audio9.mp3", "audio9-5.mp3")
    comparar_arquivos("audio10.mp3", "audio10-5.mp3")
    comparar_arquivos("audio1.mp3", "audio1-10.mp3")
    comparar_arquivos("audio2.mp3", "audio2-10.mp3")
    comparar_arquivos("audio3.mp3", "audio3-10.mp3")
    comparar_arquivos("audio4.mp3", "audio4-10.mp3")
    comparar_arquivos("audio5.mp3", "audio5-10.mp3")
    comparar_arquivos("audio6.mp3", "audio6-10.mp3")
    comparar_arquivos("audio7.mp3", "audio7-10.mp3")
    comparar_arquivos("audio8.mp3", "audio8-10.mp3")
    comparar_arquivos("audio9.mp3", "audio9-10.mp3")
    comparar_arquivos("audio10.mp3", "audio10-10.mp3")
    comparar_arquivos("audio1.mp3", "audio1-20.mp3")
    comparar_arquivos("audio2.mp3", "audio2-20.mp3")
    comparar_arquivos("audio3.mp3", "audio3-20.mp3")
    comparar_arquivos("audio4.mp3", "audio4-20.mp3")
    comparar_arquivos("audio5.mp3", "audio5-20.mp3")
    comparar_arquivos("audio6.mp3", "audio6-20.mp3")
    comparar_arquivos("audio7.mp3", "audio7-20.mp3")
    comparar_arquivos("audio8.mp3", "audio8-20.mp3")
    comparar_arquivos("audio9.mp3", "audio9-20.mp3")
    comparar_arquivos("audio10.mp3", "audio10-20.mp3")
    comparar_arquivos("audio1.mp3", "audio1-40.mp3")
    comparar_arquivos("audio2.mp3", "audio2-40.mp3")
    comparar_arquivos("audio3.mp3", "audio3-40.mp3")
    comparar_arquivos("audio4.mp3", "audio4-40.mp3")
    comparar_arquivos("audio5.mp3", "audio5-40.mp3")
    comparar_arquivos("audio6.mp3", "audio6-40.mp3")
    comparar_arquivos("audio7.mp3", "audio7-40.mp3")
    comparar_arquivos("audio8.mp3", "audio8-40.mp3")
    comparar_arquivos("audio9.mp3", "audio9-40.mp3")
    comparar_arquivos("audio10.mp3", "audio10-40.mp3")
    comparar_arquivos("audio1.mp3", "audio1-50.mp3")
    comparar_arquivos("audio2.mp3", "audio2-50.mp3")
    comparar_arquivos("audio3.mp3", "audio3-50.mp3")
    comparar_arquivos("audio4.mp3", "audio4-50.mp3")
    comparar_arquivos("audio5.mp3", "audio5-50.mp3")
    comparar_arquivos("audio6.mp3", "audio6-50.mp3")
    comparar_arquivos("audio7.mp3", "audio7-50.mp3")
    comparar_arquivos("audio8.mp3", "audio8-50.mp3")
    comparar_arquivos("audio9.mp3", "audio9-50.mp3")
    comparar_arquivos("audio10.mp3", "audio10-50.mp3")
    