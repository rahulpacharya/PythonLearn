## BYTE
## How to get byte value of string 
print('byte') # byte
b_str = b'rahul'
print(b_str[1])
## ascii value of lower case a is 97

#b_str[1] = 65  
#Error coz byte string is immutable

## Byte array is mutable
## Like when reading network data or read image bits, 
#I get binary data and want to store and modify
## Then we use Byte array

ba = bytearray('abcde','utf-8')
print(ba) 
# bytearray(b'abcde')
print(ba[0])  
## returns individual byte value # 97
print(ba[0:4]) 
## returns slice  # bytearray(b'abcd')
ba[0]=65  ## Change lower to upper case A ## MUTABLE
print(ba[0])  
## returns individual byte value
# 65
print(ba[0:4]) 
## returns slice # bytearray(b'Abcd')
