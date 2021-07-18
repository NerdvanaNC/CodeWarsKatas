# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e
# int32 to IPv4 (5 kyu)

# Learnt a lot about how binary numbers work!

def int32_to_ip(int32):
    x = '{:032b}'.format(int32)
    return '{}.{}.{}.{}'.format(int(x[0:8], 2), int(x[8:16], 2), int(x[16:24], 2), int(x[24:32], 2))