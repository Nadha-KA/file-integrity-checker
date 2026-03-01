import hashlib

def calculate_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()
try:
    file_name = input("Enter file name: ")
    original_hash = calculate_hash(file_name)
    print("\nOriginal File Hash Stored!")
    print("Hash:", original_hash)
    input("\nPress Enter after modifying or verifying the file...")
    new_hash = calculate_hash(file_name)
    if original_hash == new_hash:
        print("\nFile Integrity Verified - File Not Modified")
    else:
        print("\nWarning! File Modified or Tampered")
except FileNotFoundError:
    print("File not found!")
