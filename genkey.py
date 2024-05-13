import os

def generate_secure_key(key_length=256):
    """
    Generate a secure cryptographic key.
    
    Parameters:
        key_length (int): Length of the key in bytes. Default is 256 bytes.
    
    Returns:
        bytes: A securely generated random key.
    """
    return os.urandom(key_length)

def save_key_to_file(key, filename="encryption.key"):
    """
    Save the generated key to a file.
    
    Parameters:
        key (bytes): The cryptographic key to save.
        filename (str): The filename where the key will be saved. Default is "encryption.key".
    """
    with open(filename, 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    # Generate a 256-byte secure key
    key = generate_secure_key()
    # Save the key to a file
    save_key_to_file(key)
    print(f"Key generated and saved to file successfully!")
