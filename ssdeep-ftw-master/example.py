from ssftw import SSFTW

ssdeep = SSFTW("C:\\Users\\Aluno\\Desktop\\ssdeep-2.14.1\\ssdeep.exe")

print("[+] Computing hashes from 2 files.")
hash1 = ssdeep.hash_from_file("C:\\Users\\Aluno\\Desktop\\lorem.txt")
hash2 = ssdeep.hash_from_file("C:\\Users\\Aluno\\Desktop\\lorem mod.txt")
print(f"Hash 1: {hash1}\nHash 2: {hash2}")

print(f"Ratio: {ssdeep.compare(hash1, hash2)}")

print("--" * 30)

"""print("[+] Computing hashes from 2 strings.")
hash1 = ssdeep.hash("Some long string, man.")
hash2 = ssdeep.hash("Similar long string, man!")
print(f"Hash 1: {hash1}\nHash 2: {hash2}")

print(f"Ratio: {ssdeep.compare(hash1, hash2)}")"""
