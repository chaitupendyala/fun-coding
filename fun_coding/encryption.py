from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Chaitanya")
print "Cypher text: " + cipher_text
plain_text = cipher_suite.decrypt(cipher_text)
