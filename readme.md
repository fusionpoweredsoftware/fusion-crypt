# Fusion Crypt - A Simple File Encryption/Decryption Tool

This repository contains two scripts that provide functionality for secure key generation and basic file encryption/decryption using XOR methods. Please note that while the key generation script uses cryptographically secure methods to generate a key, XOR encryption itself is not secure for serious security applications but can be used for educational purposes or very basic data obfuscation.

## Files

- `genkey.sh`: Generates a secure cryptographic key and saves it to a file.
- `crypt.sh`: Encrypts or decrypts files using XOR encryption. Uses the generated key for encryption and decryption.

## Requirements

- Python 3.x

## genkey.sh

This script generates a cryptographically secure key using Python's `os.urandom()` and saves it to a file named `encryption.key` by default.

### Usage

Run the script from the command line:
```bash
python genkey.sh
```
This will generate a key and save it to `encryption.key`. You can specify a different filename by editing the script.

## crypt.sh

This script encrypts or decrypts files based on their extension (encrypts if normal, decrypts if `.enc`). It uses a key file (`encryption.key` by default) for the XOR encryption process.

### Usage

#### Encrypting a File

To encrypt a file, simply run:
```bash
python crypt.sh yourfile.txt
```
This will generate `yourfile.txt.enc` if `yourfile.txt` is not already encrypted.

#### Decrypting a File

To decrypt a file, ensure the file ends with `.enc` and run:
```bash
python crypt.sh yourfile.txt.enc
```
This will decrypt `yourfile.txt.enc` and save the output to `yourfile.txt`, removing the original encrypted file.

#### Specifying a Key File

If you want to specify a custom key file, you can pass it as a second argument:
```bash
python crypt.sh yourfile.txt yourkey.key
```
This command uses `yourkey.key` for encrypting or decrypting `yourfile.txt`.

## Note

The encryption provided by `crypt.sh` is based on XOR and, although it uses a secure key, should not be considered secure for protecting sensitive data due to the inherent weaknesses of XOR encryption.