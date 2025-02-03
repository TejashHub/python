input_str = input('Enter String: ').strip().lower()

reverse_str  = ''

for char in input_str:
    reverse_str = char + reverse_str 

print(reverse_str)
