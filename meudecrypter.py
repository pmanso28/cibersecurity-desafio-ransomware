import os
import pyaes

#abrir o arquivo criptografado

file_name = "meuteste.txt.encriptado"
file = open(file_name,'rb')
file_data = file.read()
file.close()

## definir a chave de criptografia

key = b'meutesteransomwa'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

### remover criptografado

os.remove(file_name)

#### criar um novo arquivo descriptografado

new_file = 'meuteste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
