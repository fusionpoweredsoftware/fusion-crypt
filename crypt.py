import sys
import os

def generate_key(key_file):
    """ Generate a simple key from the key file content or default data if not exists. """
    if os.path.exists(key_file):
        with open(key_file, 'rb') as file:
            key_data = file.read()
    else:
        key_data = os.urandom(256)  # Generate a random key if file doesn't exist
        with open(key_file, 'wb') as file:
            file.write(key_data)
    return key_data

def xor_data(data, key):
    """ XOR the data with the key. The key will cycle if shorter than data. """
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

def process_file(file_path, key_file='encryption.key'):
    key = generate_key(key_file)
    if file_path.endswith('.enc'):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = xor_data(encrypted_data, key)
        new_file_path = file_path.replace('.enc', '')
        with open(new_file_path, 'wb') as file:
            file.write(decrypted_data)
        os.remove(file_path)
    else:
        with open(file_path, 'rb') as file:
            original_data = file.read()
        encrypted_data = xor_data(original_data, key)
        new_file_path = file_path + '.enc'
        with open(new_file_path, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename> [key_file]")
        sys.exit(1)
    file_path = sys.argv[1]
    key_file = sys.argv[2] if len(sys.argv) > 2 else 'encryption.key'
    process_file(file_path, key_file)
