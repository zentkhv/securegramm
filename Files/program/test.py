import main_GOST

message = '123'
print('message: ' + message)

encryption = main_GOST.encrypt(message)
print("encryption: " + encryption)

decryption = main_GOST.decrypt(encryption)
print('decryption: ' + decryption)
for i in decryption:
    print(i)

if message == decryption:
    print('1')
else:
    print('0')
