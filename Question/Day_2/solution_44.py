alphabetic = input('enter alphabetic: ')

resultList = alphabetic.split(' ')

for result in resultList:
    lower_case = result.lower()
    sorter_word = ''.join(sorted(lower_case))
    print(sorter_word)