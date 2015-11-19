import pyaes
import os

# 128 bit random key
key_128 = os.urandom(16)
iv = "InitializationVe"

def AES_ECB(key, filename):
	ciphertext = ""
	encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationECB(key))
	for line in file(filename):
	    ciphertext += encrypter.feed(line)
	# Make a final call to flush any remaining bytes and add padding
	ciphertext += encrypter.feed()
	print repr(ciphertext)
	decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationECB(key))
	decrypted = decrypter.feed(ciphertext)
	# Again, make a final call to flush any remaining bytes and strip padding
	decrypted += decrypter.feed()
	print file(filename).read() == decrypted

def AES_CBC(key, iv, filename):
	ciphertext = ""
	# We can encrypt one line at a time, regardles of length
	encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
	for line in file(filename):
		ciphertext += encrypter.feed(line)
	# Make a final call to flush any remaining bytes and add paddin
	ciphertext += encrypter.feed()
	print repr(ciphertext)
	# We can decrypt the cipher text in chunks (here we split it in half)
	decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key, iv))
	decrypted = decrypter.feed(ciphertext)
	# Again, make a final call to flush any remaining bytes and strip padding
	decrypted += decrypter.feed()
	print file(filename).read() == decrypted


	'\x9d\xe4\xd6\xb3z\xd8\xf6@G\x07\x1b\x18\xdf%L]\x9d\xe4\xd6\xb3z\xd8\xf6@G\x07\x1b\x18\xdf%L]\x9d\xe4\xd6\xb3z\xd8\xf6@G\x07\x1b\x18\xdf%L]\x9d\xe4\xd6\xb3z\xd8\xf6@G\x07\x1b\x18\xdf%L]\x0e-|\xd7%\x8d0\xf0\x9a\xb0\x98\xa4h\xd3\x8c\x06\x95\xe8\x90\xd0\xecN\xe4\xa1\xa8\x94\x07\x9f\xac\x1a\x10k'