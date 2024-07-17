def sum(a, b, e=0):
    c = a + b + e
    return c



a = sum(65, 32, 3)
print(a)

# cars is a list   
cars = [
    {"company": "Ford", "model": "Mustang", "year": 1964},
    {"company": "Ford", "model": "F-150", "year": 2021},
    {"company": "BMW", "model": "M3", "year": 2022}
]


def verifyCar(car):
    if 2024 - car['year'] > 3 :
        print(f"the {car['model']} is not eligible to enter")


i = 0
while i<len(cars):
    verifyCar(cars[i])

    i += 1

for car in cars :
    verifyCar(car)