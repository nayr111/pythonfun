numbers = [1, 2, 3, 4, 5]
result = [(num, 'Tung Tung Tung Sahur') if num % 2 == 0 else (num, 'Ballerina Capuchina') for num in numbers]
print(result)