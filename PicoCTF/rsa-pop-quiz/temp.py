import binascii
from pwn import *

# Not my initial code, my function wasn't this clean
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

r = remote('jupiter.challenges.picoctf.org', 1981)

# Q1
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
q = int([l for l in lines.split('\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
r.sendline('Y')
print(r.recvuntil('n:'))
ans = q * p
print('Sending: {}'.format(ans))
r.sendline('{}'.format(ans))

# Q2
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in lines.split('\n') if 'n :' in l][0].split(':')[1].strip(), 10)
r.sendline('Y')
print(r.recvuntil('q:'))
ans = n / p
print('Sending: {}'.format(ans))
r.sendline('{}'.format(ans))

# Q3
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
r.sendline('N')

# Q4
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
q = int([l for l in lines.split('\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
r.sendline('Y')
print(r.recvuntil('totient(n):'))
ans = (q - 1) * (p - 1)
print('Sending: {}'.format(ans))
r.sendline('{}'.format(ans))

# Q5
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
plain = int([l for l in lines.split('\n') if 'plaintext :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in lines.split('\n') if 'e :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in lines.split('\n') if 'n :' in l][0].split(':')[1].strip(), 10)
r.sendline('Y')
print(r.recvuntil('ciphertext:'))
ans = pow(plain, e, n)
print('Sending: {}'.format(ans))
r.sendline('{}'.format(ans))

# Q6
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
r.sendline('N')

# Q7
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
q = int([l for l in lines.split('\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in lines.split('\n') if 'e :' in l][0].split(':')[1].strip(), 10)
r.sendline('Y')
print(r.recvuntil('d:'))
ans = MMI(e, (q - 1) * (p - 1))
print('Sending: {}'.format(ans))
r.sendline('{}'.format(ans))

# Q8
lines = r.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print(lines)
p = int([l for l in lines.split('\n') if 'p :' in l][0].split(':')[1].strip(), 10)
cipher = int([l for l in lines.split('\n') if 'ciphertext :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in lines.split('\n') if 'e :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in lines.split('\n') if 'n :' in l][0].split(':')[1].strip(), 10)
r.sendline('Y')
print(r.recvuntil('plaintext:'))
q = n / p
d = MMI(e, (q - 1) * (p - 1))
ans = pow(cipher, d, n)
print('Sending: {}'.format(ans))
r.sendline('{}'.format(ans))
lines = r.recvall()
print(lines)
print('In hex: {}'.format(hex(ans)))
print(binascii.unhexlify(hex(ans)[2:]))