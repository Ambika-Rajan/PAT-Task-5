# Sample list containing various data types
data_list = [10, 'hello', 25.5, 'world', 42, None, True, 'Python']

# Using map with a lambda function to check types
check_types = list(map(lambda x: (x, 'Integer' if isinstance(x, int) else 'String' if isinstance(x, str) else 'Other'), data_list))

# Print the results
for item in check_types:
    print(f"Value: {item[0]}, Type: {item[1]}")
