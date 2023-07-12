def sum_list(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print("Sum:", result)
