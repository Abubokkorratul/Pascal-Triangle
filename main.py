rows = int(input("Enter the number of rows for Pascal's Triangle: "))
for i in range(rows):
    coefficient = 1
    for j in range(i + 1):
        print(coefficient, end=" ")
        coefficient = coefficient * (i - j) // (j + 1)
    print()
