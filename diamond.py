import string

def letter_pos(letter):
    return string.ascii_uppercase.index(letter)

def diamond_length(letter):
    return 2 * letter_pos(letter) + 1

def margin_list_for(letter):
    margin = [0] + [ x + 1  for x in range(0, letter_pos(letter)) ]
    return margin[::-1]

def line_str(letter, pos):
    line_length = diamond_length(letter)
    margin_list = margin_list_for(letter)

    line = ""
    for i in range(0, line_length):
        if i == margin_list[pos] or i == (line_length - margin_list[pos] - 1):
            line += string.ascii_uppercase[pos]
        else:
            line += " "

    return line

def print_diamond(letter):
    for i in range(letter_pos(letter) + 1):
        print(line_str(letter, i))

    for i in reversed(range(letter_pos(letter))):
        print(line_str(letter, i))


class DiamondInfo:
    def __init__(self, length, margin):
        self.length = length
        self.marginList   = [margin]

def test_diamond_length():
    assert diamond_length("A") == 1
    assert diamond_length("B") == 3
    assert diamond_length("C") == 5
    assert diamond_length("D") == 7

def test_get_margin_list_for_letter():
    assert margin_list_for("A") == [0]
    assert margin_list_for("B") == [1, 0]
    assert margin_list_for("C") == [2, 1, 0]

def test_get_diamond_first_line_for_letter():
    assert line_str("A", 0) == "A"
    assert line_str("B", 0) == " A "
    assert line_str("C", 0) == "  A  "

def test_get_diamond_line_for_letter():
    assert line_str("B", 1) == "B B"
    assert line_str("C", 1) == " B B "
    assert line_str("D", 2) == " C   C "
#
#    A
#   B B
#  C   C
# D     D
#E       E
