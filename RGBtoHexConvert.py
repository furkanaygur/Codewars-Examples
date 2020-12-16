'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def rgb(r,g,b):
    def get_hex(s):
        if s < 0 : s = 0
        if s > 255 : s = 255
        return hex(s)[2:].upper() if len(hex(s)[2:]) > 1 else "0" + hex(s)[2:]
    return get_hex(r) + get_hex(g) + get_hex(b)

print(rgb(1,2,3))