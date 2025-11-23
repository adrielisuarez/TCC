import os
from sys import exit
import subprocess
from tempfile import mkstemp
from re import findall as regex_findall 

# Atualize aqui com o caminho correto do seu ssdeep.exe
SSDEEP_PATH = "C:\\Users\\Aluno\\Desktop\\ssdeep-2.14.1\\ssdeep.exe"
SSDEEP_HEADERS = "ssdeep,1.1--blocksize:hash:hash,filename\n"

class SSFTW:
    """Mini wrapper ssdeep para Windows."""
    def __init__(self, path_to_ssdeep=SSDEEP_PATH):
        self.ssdeep_exe = path_to_ssdeep
        if not os.path.exists(self.ssdeep_exe):
            print("[-] Exiting. ssdeep executable not found.")
            exit(1)

    def hash(self, data=""):
        try:
            fd, tmpfile = mkstemp()
            with open(tmpfile, "w") as tmp:
                tmp.write(data)
            return self.hash_from_file(tmpfile)
        except Exception as e:
            print(f"[-] Some error: {str(e)}")
            return None
        finally:
            os.close(fd)
            os.remove(tmpfile)
    
    def hash_from_file(self, filepath):
        filepath = os.path.abspath(filepath)
        if os.path.exists(filepath):
            if not os.path.isfile(filepath):
                print(f"[-] {filepath} is not a file.")
                return None
            
            cmd = [self.ssdeep_exe, "-s", "-c", filepath]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = process.communicate()
            status = process.returncode
        
            if status == 0:
                return self.parse_output(output.decode(), mode="hash")
            else:
                print(err.decode())
        else:
            print(f"[-] {filepath} does not exist.")
        return None

    def compare(self, hash1, hash2):
        try:
            files = []
            for i, hsh in enumerate([hash1, hash2]):
                d = {}
                d["fd"], d["file"] = mkstemp()
                files.append(d)
                with open(d["file"], "w") as tmp:
                    tmp.write(SSDEEP_HEADERS)
                    tmp.write(f'{hsh},"temp{i}"\n')

            ratio = self.compare_files(files[0]["file"], files[1]["file"], hashfile=True)
            if ratio is None:
                return 0  # retorna 0 se não conseguir calcular
            return ratio

        except Exception as e:
            print(f"[-] Some error. {str(e)}")
            return 0
        finally:
            for f in files:
                os.close(f["fd"])
                os.remove(f["file"])

    def compare_files(self, file1, file2, hashfile=True):
        file1 = os.path.abspath(file1)
        file2 = os.path.abspath(file2)

        if hashfile:
            cmd = [self.ssdeep_exe, "-s", "-x", file1, file2]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, err = process.communicate()
            status = process.returncode

            if status == 0:
                output_str = output.decode('utf-8', errors='ignore')
                return self.parse_output(output_str, mode="ratio")
            else:
                err_str = err.decode('utf-8', errors='ignore')
                print(f"[-] Error in compare_files: {err_str}")
        return 0

    def parse_output(self, data, mode="hash"):
        result = None
        lines = [line for line in data.splitlines() if line]
        if mode == "hash" and lines:
            result = lines[-1].split(",")[0]
            return result
        elif mode == "ratio" and lines:
            matches = regex_findall(r"\((\d{1,3})", lines[0])
            if matches:
                result = int(matches[0])
            else:
                result = 0
        return result


if __name__ == "__main__":
    print("[+] Use this as a module.")
