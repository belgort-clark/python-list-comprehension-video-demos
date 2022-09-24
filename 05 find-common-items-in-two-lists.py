# Find common elements within two lists

students_a = ["Gayle","Bruce", "Brandon", "Tucker", "Erin"]
students_b = ["Bruce","Han","Gayle","Corlene"]

common = [student for student in students_a if student in students_b]

print(common)