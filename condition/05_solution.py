status = input('Weather Status: ')

if( status != 'sunny' and status != 'rainy' and status != 'snowy'):
     message = 'Enter Valid Weather Status'
elif(status == 'sunny'):
    message = 'Go For Walk'
elif(status == 'rainy'):
    message = 'Read a Book'
elif(status == 'snowy'):
    message = 'Build a Snowman'

print(message)