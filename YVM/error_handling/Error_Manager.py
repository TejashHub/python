file = open('Youtube.txt','w')

try:
    file.write('chai or code')
finally:
    file.close()

with open('Youtube.txt','w') as file:
    file.write('chai or python')