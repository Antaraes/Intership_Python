# Encoding a string to ASCII
original_string = "Hello, World."
ascii_encoded_bytes = original_string.encode('ascii')

# Print the ASCII encoded bytes
print("ASCII Encoded Bytes:", ascii_encoded_bytes)

# Decoding the ASCII back to the original string
decoded_string = ascii_encoded_bytes.decode('ascii')
print("Decoded String:", decoded_string)