# COMP 202 A2 Part 5
# Author: GATTUOCH KUON

from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
# You may want to define more global variables here

####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where')
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word,
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # ADD CODE HERE
    text = two_letter_contractions(whole_word_contractions(text))

    return text

def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    # ADD CODE HERE
    quotation = True
    #I enumarate through toget the value at a given index
    for index, c in enumerate(text):
        if c == '"'  and quotation : #Want to know if c is in quotation
            quotation = not quotation
            text= text[:index] + '“' + text[index+1:]
        elif  c == '"' and not quotation :
            quotation= not quotation
            text=text[:index] + '”'+ text[index+1:]
    return text


####################################################
# Put your own helper functions here!
def english_punctuation_french(c):
    """
    (str)-> str
    Want to convert English punctuation to French punctuation to be translated
    >>> english_punctuation_french("?")
    '('
    >>> english_punctuation_french("“”")
    '()'
    >>> english_punctuation_french("”")
    ')'
    """
    char= convert_quotes(c)
    for i in char:
        if i== "?":
            char= char.replace("?", "(")
        elif i== "(" or i== ")":
            char== char.replace("(", "“")
            char== char.replace(")", "”")
        elif i== "“" :
            char=char.replace("“", "(")
        elif i== "”" :
            char=char.replace("”", ")")
    return char

def digits_to_english_braille(c):
    """
    (str)-> str
    Want to convert digits to English braille for easy trnaslation
    >>> digits_to_english_braille(c) ("5")
    "⠼⠑⠰"
    >>> digits_to_english_braille(c) ("25")
    "⠼⠃⠑"
    >>> digits_to_english_braille(c) ("COMP 250")
    "COMP ⠼⠃⠑⠚⠰"
    """
    is_continuous =False
    t="↑"
    string_1 = ""
    is_last=""
    is_first=""
    while "⠼" in string_1:
        index=string_1.find("⠼" )
        is_first = "⠼" in string_1[index-2:index] and t in string_1[index-2:index]
        is_last = "⠼" in string_1[index-2:index] and t in string_1[index:index+2]
    if is_continuous:
        is_first= False
    if is_first:
        string_1.replace("⠼", "t")
    if is_last:
        is_continuous= True
    if not is_first and not is_last:
        string_1.replace("⠼","")

    return string_1
####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # You may want to put code after this comment. You can also delete this comment.

    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)
    text=english_punctuation_french(text)
    text=digits_to_english_braille(text)

    # You may want to put code after this comment. You can also delete this comment.

    # Run the text through the French Braille translator
    text = text_to_braille(text)

    # You may want to put code after this comment. You can also delete this comment.

    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))

    # You may want to put code after this comment. You can also delete this comment.

    return text


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
