name = "xyz"
age = 25

info = [name, age]
print(info)


my_dict = {"name":name, "age":age}
print(my_dict)

info.append(1234)
print(info)

my_dict["gpd"] = 14.17
print(my_dict)

# converting the age from int to string
age_str = str(age)
print(age_str[0])


# removing 1234 from info
info.pop()
print(info)
info.remove("xyz")
print(info)

del my_dict["gpd"]
print(my_dict)

if age > 14 :
    print("hi")

if my_dict["name"] == name :
    print("hello " + name)
    print("hello", name)
    print(f"hello {name}")
