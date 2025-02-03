order_size = input('Order Size ').strip().lower()
extra_shot = input('Do you want an extra shot? (Yes/No) ').strip().lower()

extra_shot_type = ['yes', 'no']

order_size_type = ['small', 'extra small', 'medium', 'extra medium', 'large', 'extra large']

if extra_shot not in extra_shot_type:
        print('Enter Only Yes/No')
else:
    if order_size not in order_size_type:
        print('Enter Valid Order Size')
    else:
        if(extra_shot == 'yes'):
            print('Your Coffie is ',order_size, 'With Some Extra Sort')
        else:
            print('Your Coffie is ',order_size)

