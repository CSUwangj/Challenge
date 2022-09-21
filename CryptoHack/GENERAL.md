# GENERAL

## Encoding

### ASCII

``` python_repl
>>> bytes([99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125])
b'crypto{ASCII_pr1nt4bl3}'
```

### Hex

``` python_repl
>>> bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
b'crypto{You_will_be_working_with_hex_strings_a_lot}'
```

### Base64

``` python_repl
>>> import base64; base64.b64encode(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"))
b'crypto/Base+64+Encoding+is+Web+Safe/'
```

### Bytes and Big Integers


``` python_repl
>>> from Crypto.Util.number import *; long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
```

### Encoding Challenge

just decode 100 messages

[solution](./GENERAL/Encoding_Challenge.py)

## XOR

### XOR Starter

``` python_repl
>>> from pwn import xor; xor("label", 13)
~/.local/lib/python3.8/site-packages/pwnlib/util/fiddling.py:325: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  strs = [packing.flat(s, word_size = 8, sign = False, endianness = 'little') for s in args]
b'aloha'
```

###  XOR Properties

(FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ (KEY2 ^ KEY3) ^ KEY1 == FLAG

``` python_repl
>>> from Crypto.Util.number import *; long_to_bytes(0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313)
b'crypto{x0r_i5_ass0c1at1v3}'
```

### Favourite byte

just brute force, check [solution](./GENERAL/Favourite_byte.py)

``` bash
➜ python3 GENERAL/Favourite_byte.py
b'{jahlwc(`)(G)-GuaG~,n(mj)/+Gza/}e'
b'}lgnjqe.f/.A/+AsgAx*h.kl/)-A|g){c'
b'crypto{0x10_15_my_f4v0ur173_by7e}'
b'et\x7fvri}6~76Y73Yk\x7fY`2p6st715Yd\x7f1c{'
b'j{py}fr9q89V8<VdpVo=\x7f9|{8>:Vkp>lt'
b'hyr{\x7fdp;s:;T:>TfrTm?};~y:<8Tir<nv'
b'n\x7ft}ybv=u<=R<8R`tRk9{=x\x7f<:>Rot:hp'
b'l}v\x7f{`t?w>?P>:PbvPi;y?z}>8<Pmv8jr'
b"+:18<'3x0yx\x17y}\x17%1\x17.|>x=:y\x7f{\x17*1\x7f-5"
b")83:>%1z2{z\x15{\x7f\x15'3\x15,~<z?8{}y\x15(3}/7"
b'/>5<8#7|4}|\x13}y\x13!5\x13*x:|9>}{\x7f\x13.5{)1'
b'-<7>:!5~6\x7f~\x11\x7f{\x11#7\x11(z8~;<\x7fy}\x11,7y+3'
```
### You either know, XOR you don't

flag is begin with `crypto{`, so try it:

``` python_repl
>>> long_to_bytes(bytes_to_long(b"crypto{") ^ 0x0e0b213f26041e)
b'myXORke'
```
so try `myXORkey`

``` python_repl
>>> xor(long_to_bytes(0x0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104), b'myXORkey')
b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
```

###  Lemur XOR

just xor two image, check my [solution](./GENERAL/Lemur_XOR.py)

## MATHEMATICS

### Greatest Common Divisor

``` python_repl
>>> from Crypto.Util.number import *; GCD(66528,52920) 
1512
```

### Extended GCD

``` python_repl
>>> from gmpy2 import gcdext; gcdext(26513,32321)
(mpz(1), mpz(10245), mpz(-8404))
```

### Modular Arithmetic 1

``` python_repl
>>> 11 % 6
5
>>> 8146798528947 % 17
4
```

### Modular Arithmetic 2

one

### Modular Inverting

3 * 9 == 27 = 1 MOD 13

## DATA FORMATS

### Privacy-Enhanced Mail?

``` python_repl
>>> from Crypto.PublicKey import RSA; RSA.importKey(open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "rb").read()).d
15682700288056331364787171045819973654991149949197959929860861228180021707316851924456205543665565810892674190059831330231436970914474774562714945620519144389785158908994181951348846017432506464163564960993784254153395406799101314760033445065193429592512349952020982932218524462341002102063435489318813316464511621736943938440710470694912336237680219746204595128959161800595216366237538296447335375818871952520026993102148328897083547184286493241191505953601668858941129790966909236941127851370202421135897091086763569884760099112291072056970636380417349019579768748054760104838790424708988260443926906673795975104689
```

### CERTainly not

``` python_repl
>>> from cryptography import x509; x509.load_der_x509_certificate(open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb").read()).public_key().public_numbers().n 
22825373692019530804306212864609512775374171823993708516509897631547513634635856375624003737068034549047677999310941837454378829351398302382629658264078775456838626207507725494030600516872852306191255492926495965536379271875310457319107936020730050476235278671528265817571433919561175665096171189758406136453987966255236963782666066962654678464950075923060327358691356632908606498231755963567382339010985222623205586923466405809217426670333410014429905146941652293366212903733630083016398810887356019977409467374742266276267137547021576874204809506045914964491063393800499167416471949021995447722415959979785959569497
```

### SSH Keys

first convert public key to pem format using ssh-keygen

``` bash
$ ssh-keygen -f test.pub -e -m pem
-----BEGIN RSA PUBLIC KEY-----
MIIBigKCAYEArTy6m2vhhbwx3RVbNVb3ZOenCqqsOXHaJpbtN+OuulLKBSKpIoPB
+ZDbDXn0qWkf4lOxtGSgolkUbgG07Lhzfgs+dul4UL84CkwZExmF3Rf1nRv+v7pq
Lt2dPsCb02YLxJnhHJb4rQaz2ZM4QCtTOcqYDUeKfLHCaZU4Ekm/OApKrpfw4/0o
fn8KOrFN0t4/dqnNuwVRgoaUIhsI47reApB2rs0AP4CggSIi8s6BXCxB4YzgThBK
5760T1giACYQC5MFdq1Gw+INSFmu0CNqt5wdJ5Z4z5448Gke06R+IMtjUiGDQ3Qt
T2fK3gWhZxk14M4UNrdETgTW/mQ4B/BcvikxvoBGpKbttG0agfOjTen6wyzpGfcd
8N9rSbaqqyUwC8uDotzFtFzzutVAU9d91TagGzWBhNoMfplwVTns27GOOgv1dn5s
QSSSmP0hTbPMDlThysKkR9BiOVbBtWGQpV936pPBgyWERGqMqC9xykLdVHv2Vu05
T0WMwKCAetgtAgMBAAE=
-----END RSA PUBLIC KEY-----
```

then we have the nail, use the hammer

``` python_repl
>>> from Crypto.PublicKey import RSA; RSA.importKey("""-----BEGIN RSA PUBLIC KEY-----
... MIIBigKCAYEArTy6m2vhhbwx3RVbNVb3ZOenCqqsOXHaJpbtN+OuulLKBSKpIoPB
... +ZDbDXn0qWkf4lOxtGSgolkUbgG07Lhzfgs+dul4UL84CkwZExmF3Rf1nRv+v7pq
... Lt2dPsCb02YLxJnhHJb4rQaz2ZM4QCtTOcqYDUeKfLHCaZU4Ekm/OApKrpfw4/0o
... fn8KOrFN0t4/dqnNuwVRgoaUIhsI47reApB2rs0AP4CggSIi8s6BXCxB4YzgThBK
... 5760T1giACYQC5MFdq1Gw+INSFmu0CNqt5wdJ5Z4z5448Gke06R+IMtjUiGDQ3Qt
... T2fK3gWhZxk14M4UNrdETgTW/mQ4B/BcvikxvoBGpKbttG0agfOjTen6wyzpGfcd
... 8N9rSbaqqyUwC8uDotzFtFzzutVAU9d91TagGzWBhNoMfplwVTns27GOOgv1dn5s
... QSSSmP0hTbPMDlThysKkR9BiOVbBtWGQpV936pPBgyWERGqMqC9xykLdVHv2Vu05
... T0WMwKCAetgtAgMBAAE=
... -----END RSA PUBLIC KEY-----
... """).public_key().n
3931406272922523448436194599820093016241472658151801552845094518579507815990600459669259603645261532927611152984942840889898756532060894857045175300145765800633499005451738872081381267004069865557395638550041114206143085403607234109293286336393552756893984605214352988705258638979454736514997314223669075900783806715398880310695945945147755132919037973889075191785977797861557228678159538882153544717797100401096435062359474129755625453831882490603560134477043235433202708948615234536984715872113343812760102812323180391544496030163653046931414723851374554873036582282389904838597668286543337426581680817796038711228401443244655162199302352017964997866677317161014083116730535875521286631858102768961098851209400973899393964931605067856005410998631842673030901078008408649613538143799959803685041566964514489809211962984534322348394428010908984318940411698961150731204316670646676976361958828528229837610795843145048243492909
```

### Transparency

just go to <https://crt.sh/?q=cryptohack.org> then get the flag

BTW, I can check the public key by

``` bash
$ openssl rsa -inform pem -pubin -in transparency_afff0345c6f99bf80eab5895458d8eab.pem -noout -text
RSA Public-Key: (2048 bit)
Modulus:
    00:b9:88:f4:ea:6e:6a:e0:cf:12:b0:44:30:29:7f:
    b9:34:fb:36:97:20:76:93:b8:1e:67:0e:2b:3f:af:
    1e:51:99:aa:38:37:aa:c4:38:ef:e6:69:4b:63:69:
    f3:fd:12:6c:3d:d9:2c:e0:9f:b2:e6:df:7a:28:0c:
    a8:dd:2e:60:98:3a:84:38:c1:bb:26:0a:09:f4:a5:
    3e:e0:73:d0:17:33:fd:0b:c1:b2:fa:18:ac:0a:17:
    68:f5:e1:7a:51:e5:86:4e:2a:1a:cc:50:c8:75:15:
    0a:fa:06:66:f3:57:35:88:f1:21:38:12:18:bb:70:
    9a:bb:7d:8b:46:db:fe:2f:db:f3:aa:b7:b4:3a:59:
    5f:ee:87:87:a9:c6:dc:30:12:0a:2f:a3:29:b0:93:
    06:fa:77:89:3e:72:02:23:7e:81:65:91:0c:bb:ab:
    fa:7f:cc:c8:2a:e0:7b:55:41:c0:6c:37:50:ea:db:
    01:cc:ba:57:cf:b5:cf:05:47:8a:3d:ad:45:93:c7:
    76:d8:42:3d:f6:97:87:c1:6b:74:46:e2:4f:d1:0b:
    09:9e:c6:b8:a2:3e:82:ea:51:3e:73:9f:af:54:76:
    ba:8d:5b:19:92:99:76:3e:e5:d9:d3:96:ba:f7:13:
    91:67:8a:2a:fa:7c:33:2b:c3:bf:4a:dd:61:6c:d0:
    57:b1
```

then found which certificate has the same public key as this key file, and the answer is <https://crt.sh/?id=3347792120>. Don't know why there is so many certificate for this subdomain.

but subdomain is too straight to stuck me from getting the flag.
