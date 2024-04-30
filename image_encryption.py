from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            # Example encryption operation: add the key value to each RGB component
            encrypted_pixel = tuple((pixel[i] + key) % 256 for i in range(3))
            encrypted_image.putpixel((x, y), encrypted_pixel)

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    decrypted_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            # Example decryption operation: subtract the key value from each RGB component
            decrypted_pixel = tuple((pixel[i] - key) % 256 for i in range(3))
            decrypted_image.putpixel((x, y), decrypted_pixel)

    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        image_path = input("Enter the path to the image: ")
        key = int(input("Enter the encryption/decryption key (an integer value): "))
        if choice == 'encrypt':
            encrypt_image(image_path, key)
        else:
            decrypt_image(image_path, key)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
