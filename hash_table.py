# Define a hash function
def hash_function(key):
    return sum(ord(c) for c in key) % 10

# Create an array to store the hash table
hash_table = [None] * 10

# Add some key-value pairs to the hash table
hash_table[hash_function("hello")] = "world"
hash_table[hash_function("goodbye")] = "cruel world"

# Get the value associated with the key "hello"
value = hash_table[hash_function("hello")]

# Print the value
print(value)