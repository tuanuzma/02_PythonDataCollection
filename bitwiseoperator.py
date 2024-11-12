# Truth Table for & (and)
# 0  &  0  => 0
# 1  &  0  => 0
# 0  &  1  => 0
# 1  &  1  => 1

x = 7        # 1 1 1
y = 4        # 1 0 0
print(x & y) # 1 0 0


# Truth Table for | (or)
# 0  |  0  => 0
# 1  |  0  => 1
# 0  |  1  => 1
# 1  |  1  => 1

x = 7        # 1 1 1
y = 4        # 1 0 0
print(x & y) # 1 1 1

# Truth Table for ^ XOR
# 0  ^  0  => 0
# 1  ^  0  => 1
# 0  ^  1  => 1
# 1  ^  1  => 0

x = 7        # 1 1 1
y = 4        # 1 0 0
print(x & y) # 0 1 1

# Truth Table for ~ NOT
# ~0   =>  1
# ~1   =>  0

x = 7        # 0 0 0 0 0 1 1 1      
print(~x)    # 1 1 1 1 1 0 0 0
#Answer -8
# if the most significant bit is set to 1
# then it is a negative number
# 1000 is 8 and since all the bits are set to 1 it becomes -8

# XOR used in encryption and decryption
x = 85
# let me encrypt it by a key 51
key = 51
print("Original value: ", 85)

# ENCRYPTION
encryptedvalue = x ^ key
print("Encrypted value:", encryptedvalue)

# DECRYPTION
decryptedvalue = encryptedvalue ^ key
print("Decrypted value:", decryptedvalue)

# NOT operator can be used to find the next divisible by even number
x = 19
# Find the next number which is divisible by 8
print((x + 9) & ~9) # divisible by 10
print((x + 7) & ~7) # divisible by 8
print((x + 5) & ~5) # divisible by 6
print((x + 3) & ~3) # divisible by 4
print((x + 1) & ~1) # divisible by 2

# swap 2 numbers using XOR
x = 5
y = 3
x = x ^ y 
y = x ^ y
x = x ^ y
print(x, y)

# Shift operators
# << left shift
# >> right shift

x = 10          # 0000 1010
print(x >> 1)   # 0000 0101

print(x << 1)   # 0001 0100  x * (2 ** 1)
print(x << 2)   # 0001 0100  x * (2 ** 2)
print(x << 3)   # 0001 0100  x * (2 ** 3)
print(x << 4)   # 0001 0100  x * (2 ** 4)

x = x << 4
print(x >> 1)   # 0001 0100  x / (2 ** 1)
print(x >> 2)   # 0010 1000  x / (2 ** 2)
print(x >> 3)   # 0101 0000  x / (2 ** 3)

# COMPLEX NUMBERS
# square root of 4 => 2, -2
# square root of -4
# complex numbers have 2 parts real and imaginary part
x = complex(3, 4)   # 3 + 4j
y = 5 + 6j
print(x, y)
# arithmetic operators behind complex number
print(x + y)    # (3 + 5) + (4 + 6)j    # Answer 8 + 10j 
print(x - y)    # (3 - 5) + (4 - 6)j    # -2-2j

# you also can get the real and imaginary part of a complex number
print(x.real)
print(x.imag)

# complex number multiplication formula
# (a + bj) * (c + dj) = (ac - bd) + (ad + bc)j
# ((3 * 5) - (4 * 6)) + ((3 * 6) + (4 * 5))j
# (15 - 24) + (18 + 20) => -9 + 38j
print(x * y)    

# complex number division formula
# (a + bj) / (c + dj) = (a + bj)(c - dj)/(c + dj)(c - dj)
# (ac + bd) + (bc - ad)j/c ** 2 + d ** 2

# (ac + bd)                 (bc - ad)
# ---------------   +   --------------- j
# c**2 + d**2       c**2 + d**2
print(x / y)

print(x)

print(abs(x))   # sqrt (realsquare + imaginarysquare) 
# abs() is function to find actual value for the complex number
