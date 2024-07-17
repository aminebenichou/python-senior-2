age = 17
if age > 16 :
    print("you can work")
else :
    print("you can't work")

if age > 16:
    print("you can work")
elif age > 14:
    print("you should study")
else :
    print("you can't work")

# initialize a dict then give it values of car company 
# and car model and car year of manufacturing
# then verify if a car is older than 3 years 
# write not eligible to enter

cars = [
    {"company": "Ford", "model": "Mustang", "year": 1964},
    {"company": "Ford", "model": "F-150", "year": 2021},
    {"company": "BMW", "model": "M3", "year": 2022}
]
# if cars[0]['year']-2024 < -3 :
#     print("not eligible to enter")
# if cars[1]['year']-2024 < -3 :
#     print("not eligible to enter")
# if cars[2]['year']-2024 < -3 :
#     print("not eligible to enter")

i = 0
while i<3 :
    if cars[i]['year']-2024 < -3 :
        print(f"The {cars[i]['model']} not eligible to enter")
    i = i + 1


car_names = [
    "RS 7",
    "Audi A4",
    "Mercedes E Class"
]

q = 0
while q<3 :
    if car_names[q][0].lower() == "a" :
        print(f"{car_names[q]}")
    q += 1

for name in car_names :
    if name[0].lower() == 'a':
        print(name)


for i in range(0, 5) :
    print(i)