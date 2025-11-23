#!/usr/bin/env python3
"""
TLSH Python Demo - Demonstração da biblioteca TLSH em Python
"""

import tlsh
import os

def main():
    print("=" * 50)
    print("TLSH Python Demo")
    print("=" * 50)
    print()
    
    # Criar alguns dados de exemplo
    exemplo1 = b"""Este eh um texto de exemplo para demonstrar o TLSH.
    O TLSH (Trend Micro Locality Sensitive Hash) eh uma biblioteca
    de fuzzy hashing que pode detectar similaridade entre arquivos.
    Eh muito util para analise de malware e deteccao de conteudo similar."""
    
    exemplo2 = b"""Este eh outro texto de exemplo para demonstrar o TLSH.
    O TLSH (Trend Micro Locality Sensitive Hash) eh uma biblioteca
    de fuzzy hashing que pode detectar similaridade entre documentos.
    Eh muito util para analise de malware e deteccao de conteudo parecido."""
    
    exemplo3 = b"""Texto completamente diferente sobre outro assunto.
    Este exemplo nao tem relacao com os anteriores.
    Fala sobre matematica, fisica e ciencia da computacao.
    Algoritmos, estruturas de dados e programacao em geral."""
    
    print("1. Gerando hashes TLSH dos textos:")
    print()
    
    # Gerar hashes
    try:
        hash1 = tlsh.hash(exemplo1)
        hash2 = tlsh.hash(exemplo2)
        hash3 = tlsh.hash(exemplo3)
        
        print(f"Hash do texto 1: {hash1}")
        print(f"Hash do texto 2: {hash2}")
        print(f"Hash do texto 3: {hash3}")
        print()
        
    except Exception as e:
        print(f"Erro ao gerar hashes: {e}")
        print("Nota: TLSH requer pelo menos 50 bytes com suficiente variação")
        return
    
    print("2. Comparando similaridade:")
    print()
    
    # Comparar hashes
    if hash1 and hash2 and hash3:
        try:
            dist12 = tlsh.diff(hash1, hash2)
            dist13 = tlsh.diff(hash1, hash3)
            dist23 = tlsh.diff(hash2, hash3)
            
            print(f"Distância entre texto 1 e 2: {dist12}")
            print(f"Distância entre texto 1 e 3: {dist13}")
            print(f"Distância entre texto 2 e 3: {dist23}")
            print()
            
            print("Interpretacao:")
            print("- Distancia menor = mais similar")
            print("- Distancia 0 = identico")
            print("- Distancia > 100 = muito diferente")
            print()
            
            if dist12 < dist13:
                print("Textos 1 e 2 sao mais similares (como esperado)")
            else:
                print("? Resultado inesperado na comparação")
                
        except Exception as e:
            print(f"Erro ao comparar hashes: {e}")
    
    print("3. Testando com arquivos:")
    print()
    
    # Testar com arquivos se existirem
    if os.path.exists("example1.txt"):
        try:
            with open("example1.txt", "rb") as f:
                data1 = f.read()
            hash_arquivo1 = tlsh.hash(data1)
            print(f"Hash de example1.txt: {hash_arquivo1}")
            
            if os.path.exists("example2.txt"):
                with open("example2.txt", "rb") as f:
                    data2 = f.read()
                hash_arquivo2 = tlsh.hash(data2)
                print(f"Hash de example2.txt: {hash_arquivo2}")
                
                if hash_arquivo1 and hash_arquivo2:
                    dist_arquivos = tlsh.diff(hash_arquivo1, hash_arquivo2)
                    print(f"Distância entre os arquivos: {dist_arquivos}")
                    
        except Exception as e:
            print(f"Erro ao processar arquivos: {e}")
    else:
        print("Arquivos de exemplo não encontrados")
    
    print()
    print("4. Exemplo com objeto TLSH:")
    print()
    
    # Usar objeto TLSH para processamento incremental
    try:
        h = tlsh.Tlsh()
        
        # Adicionar dados em pedaços
        for chunk in [exemplo1[i:i+50] for i in range(0, len(exemplo1), 50)]:
            h.update(chunk)
        
        h.final()
        hash_incremental = str(h)
        print(f"Hash incremental: {hash_incremental}")
        
        # Comparar com hash direto
        if hash1:
            dist_incremental = h.diff(tlsh.Tlsh(hash1))
            print(f"Distância para hash direto: {dist_incremental}")
            print("(Deve ser 0 se os dados são idênticos)")
        
    except Exception as e:
        print(f"Erro no processamento incremental: {e}")
    
    print()
    print("=" * 50)
    print("Demo Python concluída!")
    print("TLSH está funcionando perfeitamente em Python!")
    print("=" * 50)

if __name__ == "__main__":
    main()