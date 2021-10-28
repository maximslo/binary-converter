# Disclaimer: This code is for educational and illustrative purposes only.
#
# Minimal Binary Converter Script by Maxim Slobodchikov
#
# dec_to_bin(5)
# result: '101'
#
# bin_to_dec('101')
# result: 5

def dec_to_bin(n):
     """This function converts a non-negative integer from decimal to binary form."""
     if n == 0:
        return '0'
     elif n == 1:
        return '1'
     else:
        bin_rest = dec_to_bin(n//2)
        if n%2 == 0:
            return bin_rest + '0'
        else:
            return bin_rest + '1'

def bin_to_dec(b):
    """This function converts a binary to a decimal."""
    if b == '0':
        return 0
    elif b == '1':
        return 1
    else: 
        dec_rest = bin_to_dec(b[:-1])
        if b[-1] == '0':
            return 2*dec_rest + 0
        else:
            return 2*dec_rest + 1
