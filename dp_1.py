numbers = [26, 23, 534, 11, 4, 1, 5, 54, 14, 24]

sequence = []

for key, val in enumerate(numbers):
    current_length = 1
    for i in range(0, key):
        if sequence[i] <= current_length and numbers[i] < val:
            current_length = sequence[i]+1
    sequence.append(current_length)

print numbers
print sequence
