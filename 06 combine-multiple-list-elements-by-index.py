first_name = ["Bruce", "Gayle", "Tucker", "Bella"]
last_name = ["Elgort", "Ujifusa", "Elgort", "Elgort"]
ages = ["58","60","6","12"]

result = [f"{first} {last} - who is {age} years old" for first,last,age in zip(first_name, last_name,ages)]

print(result)