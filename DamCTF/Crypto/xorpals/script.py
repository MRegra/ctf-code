#!/usr/bin python3

def main():
    f = open("flags.txt", "r")
    for line in f:
        b = bytes.fromhex(line)
        for k in range(255):
            d = bytes([char ^ k for char in b])
            if b'dam' in d:
                return d

print(main())
