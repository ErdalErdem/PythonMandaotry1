with open('Mandatory1/numbers.dat', 'w') as file:
    for number in range(1, 101):
        file.write(f"{number}\n")

even_numbers = []
with open('Mandatory1/numbers.dat', 'r') as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even_numbers.append(number)

print(even_numbers)

