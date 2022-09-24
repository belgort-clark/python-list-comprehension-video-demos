alphanumeric = ["22","Fruit","99","cat","dog","58484"]

result = [int(s) for s in alphanumeric if s.isdigit()]

print(result)