line_one = "1fdggggggggggggggggggg"
line_two = "2"
def lines(line_one, line_two):
    if type(line_one) == str and type(line_two) == str:
        if len(line_one) == len(line_two):
            return 1
        if len(line_one) != len(line_two) and len(line_one) > len(line_two):
            return 2
        if len(line_one) != len(line_two) and "learn" in line_two:
            return 3
    else: 
        return 0
result = lines(line_one, line_two)
print(result)