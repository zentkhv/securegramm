from GOST import GOST
import my_utils

gost = GOST()

f = open('last_password_gost.txt')
data_pass = str(f.readlines()[0])
if data_pass == ' ':
    data_pass = ''
f.close()

f = open('last_password_gost.txt', 'w')
f.close()


key, salt = my_utils.pbkdf2(data_pass, "")


def encrypt(msg):
    gost.set_message(my_utils.string_to_bytes(msg))
    gost.set_key(key)
    gost.set_operation_mode(gost.CFB)
    # print("Msg: ", msg)
    # print("Key: ", my_utils.leading_zeros_hex(key))
    # print("Salt: ", salt)
    ciphertext = my_utils.leading_zeros_hex(gost.encrypt())
    # print("IV: ", my_utils.leading_zeros_hex(gost.get_iv()))

    # print("Encrypted: ", ciphertext)
    return ciphertext


def decrypt(ciphertext):
    gost2 = GOST()
    key2 = my_utils.pbkdf2(data_pass, salt)[0]
    gost2.set_key(key2)
    iv2 = my_utils.leading_zeros_hex(gost.get_iv())
    gost2.set_iv(my_utils.hex_to_bin_mult_64(iv2))
    gost2.set_encrypted_msg(my_utils.hex_to_bin_mult_64(ciphertext))
    gost2.set_operation_mode(gost2.CFB)

    return my_utils.bytes_to_string(gost2.decrypt())