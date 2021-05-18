## FUNCTIONS ##
def stringConverter(string_to_convert):
    res = string_to_convert.upper()
    return res

def mixString(a, b):
    if len(a and b)>1:
        b=str.replace(b,b[2],a[2:3])
        a=str.replace(a,a[2],b[2])
        res = a + " " + b
    return res
    
## MAIN ##
str_input = input("Please enter a phrase\n")
output = stringConverter(str_input)

print(output + "\n")

output = mixString(str_input, 'ola')

print(output)
