password = len(input('Password: ').strip())

if password < 6:
    message = 'Week'
if 10 <= password >= 6:
    message = 'Medium'
if password > 11:
    message = 'Strong'

print('Your Password is',message)