class Planeet:

    shape = 'round'

    def __init__(self, naam, radius, zwaartekracht, stelsel):
        self.naam = naam
        self.radius = radius
        self.zwaartekracht = zwaartekracht
        self.stelsel = stelsel


    def orbit(self):
        return f'{self.naam} is orbiting the {self.stelsel}'


    @classmethod
    def commons(cls):
        return f'All plannets are {cls.shape} because of gravity'


    @staticmethod
    def spin(speed = '2000 miles an hour'):
        return f'The planet spins and spins at {speed}'
