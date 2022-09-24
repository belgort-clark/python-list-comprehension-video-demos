# Calling a function within a list comprehension


def convert_f_to_c(temp):
    return round((temp - 32) * 5 / 9)


temps = [90, 88, 91, 75, 93, 65]

result = [convert_f_to_c(temp) for temp in temps]

print(result)
