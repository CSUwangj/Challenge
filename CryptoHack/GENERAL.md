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
