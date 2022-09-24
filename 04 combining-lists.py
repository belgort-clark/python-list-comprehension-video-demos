# Make all possible combinations of two lists
# You can also add additional lists

colors = ["red","blue","green"]
models = ["mini","max","super max"]

result = [(model,color) for model in models for color in colors]

print(result)