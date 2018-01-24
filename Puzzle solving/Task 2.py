"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
# Try 1 (Success)
numbers = [1, 2]
total = 2  # 2 ^
i = 2
while numbers[i-1] < 4000000:
    numbers.append(numbers[i-2] + numbers[i-1])
    print(numbers[i])
    if numbers[i] % 2 == 0:
        print("Added!")
        total += numbers[i]
    i += 1
print("Total: " + str(total))
