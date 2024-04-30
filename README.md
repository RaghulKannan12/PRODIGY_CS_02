# PRODIGY_CS_02
# Pixel Manipulation for Image Encryption

Imagine you have a secret message you want to send to a friend, but instead of using words, you decide to hide the message within an image. This code helps you do just that using a technique called image encryption and decryption.

Opening and Creating Images:
First, we use a Python library called PIL (Python Imaging Library) to work with images.
We define two functions: encrypt_image and decrypt_image. These functions handle the encryption and decryption processes, respectively.
When encrypting or decrypting an image, we open the original image and create a new image that will hold the encrypted or decrypted data.
Pixel Manipulation:
Every image is made up of tiny dots called pixels. Each pixel contains information about its color.
To hide our secret message, we manipulate the color of each pixel in the image.
In the encrypt_image function, we loop through every pixel in the original image. For each pixel:
We extract its color information (Red, Green, Blue values).
We apply an encryption operation to each color component of the pixel. This operation modifies the color values based on a secret key provided by the user.
We store the modified color values in a new pixel in the encrypted image.
The decrypt_image function does the opposite. It reverses the encryption process to reveal the original image.
Saving the Encrypted and Decrypted Images:
Once the encryption or decryption process is complete, we save the modified image to a new file.
For encryption, the new image is saved as "encrypted_image.png".
For decryption, the new image is saved as "decrypted_image.png".
User Interaction:
The main function is where the user interacts with the program.
It prompts the user to choose whether to encrypt or decrypt an image and provides the necessary inputs such as the image path and encryption/decryption key.
After each operation, it asks if the user wants to perform another operation.
