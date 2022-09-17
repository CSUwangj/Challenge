from pwn import * # pip install pwntools
import json
from base64 import b64decode
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

decoders = {
    "base64": lambda x: b64decode(x).decode(),
    "hex": lambda x: bytes.fromhex(x).decode(),
    "rot13": lambda x: codecs.decode(x, 'rot_13'),
    "bigint": lambda x: long_to_bytes(int(x, 16)).decode(),
    "utf-8": lambda x: bytes(x).decode(),
}

for _ in range(100):
    received = json_recv()
    json_send({ "decoded": decoders[received["type"]](received["encoded"]) })

r.interactive()
