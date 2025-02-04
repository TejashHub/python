def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_kwargs(name='saktiman',power='lazer')
print_kwargs(name='saktiman')
print_kwargs(name='saktiman',power='lazer', enemy='Dr. Jackaal')