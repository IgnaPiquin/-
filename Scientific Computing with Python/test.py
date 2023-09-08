# Define the values and additions
values = [32, 1, 9999, 523]
additions = [8, -3801, 9999, -49]
result = [values[i] + additions[i] for i in range(len(values))]

# Find the maximum width for each column
max_width = max(map(len, map(str, values + additions + result)))
print(max_width)
# Define the format for each line
format_line = f"{{:>{max_width}}}"

# Function to format a line
def format_row(numbers):
    return ' '.join([format_line.format(num) for num in numbers])

# Print the formatted lines
print(format_row(values))
print(format_row(additions))
print("-" * (len(values) * (max_width + 1)))
print(format_row(result))