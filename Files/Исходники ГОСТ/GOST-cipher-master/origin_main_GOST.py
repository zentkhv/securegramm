from GOST import GOST
import my_utils
import time

gost = GOST()
msg = "AUE na RUKAVEAUE na RUKAVEAUE na RUKAVEAUE na RUKAVE"
key, salt = my_utils.pbkdf2("Hallelujah", "")
t1 = time.time()
gost.set_message(my_utils.string_to_bytes(msg))
gost.set_key(key)
gost.set_operation_mode(gost.CFB)
print("Msg: ", msg)
print("Key: ", my_utils.leading_zeros_hex(key))
print("Salt: ", salt)
ciphertext = my_utils.leading_zeros_hex(gost.encrypt())
print("IV: ", my_utils.leading_zeros_hex(gost.get_iv()))

print("Encrypted: ", ciphertext)

#deciphered = gost.decrypt(gost.CBC)
#print("Decrypted: ", my_utils.bytes_to_string(deciphered))
t2 = time.time()
print("Elapsed time (s): ", t2 - t1)

#Decrypt the ciphertext obtained before using a new GOST object
gost2 = GOST()
key2 = my_utils.pbkdf2("Hallelujah", salt)[0]
gost2.set_key(key2)
iv2 = my_utils.leading_zeros_hex(gost.get_iv())
gost2.set_iv(my_utils.hex_to_bin_mult_64(iv2))
gost2.set_encrypted_msg(my_utils.hex_to_bin_mult_64(ciphertext))
gost2.set_operation_mode(gost2.CFB)

print("Decrypted from scratch: ", my_utils.bytes_to_string(gost2.decrypt()))