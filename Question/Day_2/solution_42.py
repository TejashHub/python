import string

punctuation = string.punctuation

message = input('enter string: ') 

result = ""

has_punctuation = False  

for char in message:
    if char not in punctuation:
        result += char

print(f'your result is: {result}')
