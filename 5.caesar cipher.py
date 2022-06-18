print('RITHIV.R-19MIC0113\n')
print('Caesar Cipher')

plaintext = input('Enter the plaintext:').lower()
ciphertext = ""
decryptedtext = ""

caser = {chr(97+k):k for k in range(26)}

print('\nEncryption:\n')
for i in plaintext:
    en = (caser[i]+3)%26
    ciphertext = ciphertext+chr(97+en)    
print("\tCiphertext:",ciphertext)
    

print('\nDecryption:\n')
for i in ciphertext:
    de = (caser[i]-3)%26
    decryptedtext = decryptedtext+chr(97+de)
print("\tDecrypted Plaintext:",decryptedtext)



