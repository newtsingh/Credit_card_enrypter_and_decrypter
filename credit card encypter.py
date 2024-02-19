from cryptography.fernet import Fernet
import base64
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cc_number = input("Enter your credit card number to encrypt : ")


encrypted_cc_number = cipher_suite.encrypt(cc_number.encode())

decrypted_cc_number = cipher_suite.decrypt(encrypted_cc_number).decode()

print("Encrypted:", encrypted_cc_number)
print("Decrypted:", decrypted_cc_number)