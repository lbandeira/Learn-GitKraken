
def stringConverter(string_to_convert):
    res = string_to_convert.upper()
    return res

def stringConverter2(string_to_convert1, string_to_convert2):
    res = string_to_convert1.upper() + string_to_convert2.upper()
    return res

str_input = input("Please enter a phrase\nlais")
output = stringConverter(str_input)

print(output)