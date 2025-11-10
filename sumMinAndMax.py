numbers = [1, 2, 3, 4, 5]
numbers.sort()

print(numbers, type(numbers))

# Smallest and largest
small = numbers[0]
big = numbers[-1]
print("Smallest:", small)
print("Biggest:", big)
print("========================")

def addition(k):
    value = 0
    for i in k:
        value = value + i
    return value

print("========================")
final = addition(numbers)
print(final-small, final-big )
print("========================")
