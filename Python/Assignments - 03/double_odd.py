list_of_numbers = list(map(int, input("Enter a list of numbers: ").split()))

odd_nums = list(filter(lambda x: x % 2 != 0, list_of_numbers))
odd_nums_doubled = list(map(lambda x: x*2, odd_nums))

even_nums = list(filter(lambda x: x % 2 == 0, list_of_numbers))

print("Odd numbers: ", odd_nums)
print("Doubled odd numbers: ", odd_nums_doubled)
print("Even numbers: ", even_nums)
