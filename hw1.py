from Crypto.PublicKey import RSA
import base64
import sys,os,signal
import binascii
from Crypto.Cipher import PKCS1_v1_5

pubkey = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIh16Sa3YCppifETNml6gKa/Cy
56AT/hxNJMx6zQmQuYvjEIBAbB4EnW346ewy1yRRVDBKVYrJTHbmw2nIHbQGP5QU
8GDbRogM05RCkorSZjB03L8Zhpp1u7hi8/dhPnKbQnrCHrI+S5EAu4OK3yw/nh76
KlBOb/G1+py02ESHWwIDAQAB
-----END PUBLIC KEY-----'''

cipher = 'mPWM4kial8Cp1AuygSB8Cw/dUX7FEKGZi5JEzN/Gc8EVY5N5F6IXU1eW4HiT7rzpkl42lVKMfclMdEruWd1cACE3pSM5YyX/rW06GwlFXwCf59RnlUBPBngTfe3lv5bs0q6S0Sk7Sx81hyaPcSJqEP8xJuBYANEVYyx5eKk2RGs='

n = 140816102882370072753963128960517081965880280303822400235001309160195926187868730723645674960568062473761002103307583098926327676818048971808675637139699318767264291797993510624508457914745131902730458707154587694229291440822570657047495880598540768909211668263294445392516077874925310419418057302897080960859
e = 65537

def str2num(s):
    return int(s.encode('hex'), 16)

def num2str(n):
    d = ('%x' % n)
    if len(d) % 2 == 1:
        d = '0' + d
    return d.decode('hex')


def main():

    rsaobj = RSA.importKey(pubkey)
    #rsaobj = PKCS1_v1_5.new(rsaobj)
    #re = rsaobj.encrypt(r)
    #print("\t[+] The ciphertext is: {}\n".format(c))
    #n,e = rsaobj.n, rsaobj.e
    p = 2
    re = pow(p,e,n)
    c = str2num(base64.b64decode(cipher))
    zzz = (c * re) % n
    #print zzz
    zzz = base64.b64encode(num2str(zzz))
    #print zzz

    decrypt = 'jJiCjvamYL7yYOq+yGC+1tze7r7o0Ga+xtDeasrcvsZi4NBm5L5o6OjCxtZC+g=='

    plaintext = ( str2num(base64.b64decode(decrypt)) / p ) % n

    print num2str(plaintext)


if __name__ == '__main__' :
    main()



