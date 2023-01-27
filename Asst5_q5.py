num_rows = int(input("Input the number of rows:"))

alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

alphabet_index = 0

for row in range(1, num_rows + 1):
    for column in range(1, row + 1):
        print(alphabets[alphabet_index], end="")
        alphabet_index += 1
        if alphabet_index == len(alphabets):
            alphabet_index = 0
    print()