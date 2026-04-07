# Random Python code: Print a triangle pattern
rows = 5

for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))