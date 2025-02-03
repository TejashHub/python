distance = int(input('Distance : '))

if distance < 3:
    transport = 'Walk'
elif distance >= 3 and distance <=15:
    transport = 'Bike'
elif distance >= 16:
    transport = 'Car'

print('Choose of Mode',transport)
