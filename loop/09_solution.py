fruits = [
    "apple", "banana", "mango", "grapes", "pineapple", "orange", 
    "apple", "banana", "mango", "orange", "grapes", "pineapple", 
    "strawberry", "watermelon", "kiwi", "blueberry", "papaya", 
    "banana", "apple", "kiwi", "mango", "blueberry", "grapes"
]

unique_fruits = set()   

for fruit in fruits:
    if fruit in unique_fruits:
        print(f'Dublicate Fruite {fruit}')
        break
    unique_fruits.add(fruit)
