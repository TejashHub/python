alphabetic = input('Enter alphabetic: ')

resultList = alphabetic.split(' ')

for result in resultList:
    lower_case = result.lower()
    sorted_lower = ' '.join(sorted(lower_case))
    print(sorted_lower)