def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
input_list = [10, 20, 30, 20, 40, 10, 50]
result = remove_duplicates(input_list)
print("Unique List:", result)
