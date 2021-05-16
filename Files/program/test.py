from pip._vendor.pkg_resources import require

cover = 'kdfgjmdkdfghfgh'
password = '123'
secret = 'hi'

StegCloak = require('stegcloak');

a = StegCloak.hide(secret, password, cover)
print(a)

b = StegCloak.reveal(a, password)
print(b)