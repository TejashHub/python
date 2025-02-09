# solution 1 | using bar operator

# dic1 = {
#     "Lisa": 67,
#     "John": 99
# }

# dic2 = {
#     "Lisa": 65,
#     "perter": 56
# }

# print(dic1 | dic2)

# solution 2 | using ** operator

# dic1 = {
#     "Lisa": 67,
#     "John": 99
# }

# dic2 = {
#     "Lisa": 65,
#     "perter": 56
# }

# print({**dic1, **dic2})

# solution 3 | copy() and update()

dic1 = {
    "Lisa": 67,
    "John": 99
}

dic2 = {
    "Lisa": 65,
    "perter": 56
}

dic3 = dic2.copy()
dic2 = dic1
dic1 = dic3
dic3.update(dic1)

print(dic3)
