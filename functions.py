def area(radius):
    return 3.142 * radius * radius

def vol(area, length):
    print(f'Lengte is {area * length}')

radius = int(input('Geef de radius: '))
length = int(input('Geef de lengte: '))

area(radius)
vol(area(radius), length)
