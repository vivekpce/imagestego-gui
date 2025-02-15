import cv2
import os

# Encryption Function
def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    d = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = d[char]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    encrypted_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")  # Open image on Windows
    return encrypted_path, password

# Decryption Function
def decrypt_image(image_path, password, original_message_length, input_password):
    if password != input_password:
        print("YOU ARE NOT authorized")
        return
    
    img = cv2.imread(image_path)
    c = {i: chr(i) for i in range(255)}
    
    message = ""
    n, m, z = 0, 0, 0
    for _ in range(original_message_length):
        message += c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    print("Decryption message:", message)

# Example Usage
if __name__ == "__main__":
    choice = input("Enter 'E' for Encryption or 'D' for Decryption: ").upper()
    if choice == 'E':
        image_path = "mypic.jpg"  # Replace with correct image path
        msg = input("Enter secret message:")
        password = input("Enter a passcode:")
        encrypt_image(image_path, msg, password)
    elif choice == 'D':
        image_path = "encryptedImage.jpg"
        pas = input("Enter passcode for Decryption: ")
        original_message_length = int(input("Enter the length of the original message: "))
        decrypt_image(image_path, password, original_message_length, pas)
    else:
        print("Invalid choice!")
