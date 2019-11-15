# COMP 202 Assignment 2 Part 3
# Author: GATTUOCH KUON
# Student ID:260-877-635

import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    '''
    numb="" # an empty str to keep count of my numbers
    for element in range(1,9):# i loop through all my 8 elements
        if str(element) in s:
            numb+=str(1) # i add 1 if my str is a raised digit
        else:
            numb+=str(0) # i concaternate a 0 when its not a raised digit
    return numb


def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''
    s = s[::-1]
    str_1= int(s, 2)
    str_2 = int("2800",16)
    str_3= str_1 + str_2
    str_hex = hex(str_3)

    return str_hex[2:] #i slice off the first two strings to get deisred hex


def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''
    comb ="..oo."
    if len(s)==8: # i check if my str is a 6-dot with length 8
        if s[0:2] not in comb:
            return False
        elif s[3:5] not in comb:
            return False
        elif s[6:8] not in comb:
            return False
        elif s[2]!="\n" or s[5]!="\n":
            return False
        else:
            return True # return true if my str has the o_string format
    elif len(s)==11:# i check if my str is 8-dot with length 11
        if s[0:2] not in comb:
            return False
        elif s[3:5] not in comb:
            return False
        elif s[6:8] not in comb:
            return False
        elif s[9:11] not in comb:
            return False
        elif s[2]!="\n" or s[5]!="\n" or s[8]!="\n":
            return False
        else:
            return True # at this point my str pass the test and is 8-format
    else:
        return False # this return false for all other cases  less 6-dot format
                    # or more than 8-dot format

def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    '''
    #i convert my o_string->raised->binary->hex-> Unicode
    if is_ostring(s):
        strings_pos= ostring_to_raisedpos(s)
        raised_binary = raisedpos_to_binary(strings_pos)
        binary_hex= binary_to_hex(raised_binary)
        hex_Unicod =hex_to_unicode(binary_hex)
        return hex_Unicod

    return s


if __name__ == '__main__':
    doctest.testmod()
