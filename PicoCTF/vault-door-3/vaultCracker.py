

def checkPassword(password):
    if (not len(password) == 32):
        return False
    buffer = [""]*32
    print(buffer)
    for i in range(8):
        buffer[i] = password[i]
    for i in range(8, 16):
        buffer[i] = password[23-i]
    for i in range(16, 32, 2):
        buffer[i] = password[46-i]
    for i in range(31, 16, -2):
        buffer[i] = password[i] 
    print(''.join(buffer))

checkPassword("jU5t_a_sna_3lpm12g94c_u_4_m7ra41")
