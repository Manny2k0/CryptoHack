from pwn import *
import json
import sys

def initialize_connection():
    if len(sys.argv) != 2:
        print('Usage: python3 script.py <ip:port>')
        sys.exit(1)
    hostname, port_number = sys.argv[1].split(':')
    return remote(hostname, int(port_number))

def execute():
    connection = initialize_connection()

    connection.sendlineafter(b'Give me a document to store\n', b'{"document":"4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"}')
    connection.sendlineafter(b'{"success": "Document 008ee33a9d58b51cfeb425b0959121c9 added to system"}\n', b'{"document":"4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"}')
    
    retrieved_flag = connection.recv().decode()

    print(f'\nFlag! {retrieved_flag}')

if __name__ == '__main__':
    execute()