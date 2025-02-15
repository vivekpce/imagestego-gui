# imagestego-gui
Image Steganography Tool

Overview

This is a Python-based GUI application that allows users to hide (encrypt) and retrieve (decrypt) messages within an image using steganography techniques. The application provides an easy-to-use interface using Tkinter.

Features

Encrypt Message: Hide a secret message within an image using Least Significant Bit (LSB) steganography.

Decrypt Message: Retrieve the hidden message from an encoded image using a password.

Password Protection: Ensures secure access to hidden messages.

User-Friendly GUI: Simple interface for selecting images and entering messages.

Automatic File Saving: Saves the encoded image to the desktop and opens it automatically.

Requirements

Ensure you have the following dependencies installed:

pip install opencv-python numpy pillow tkinter

How to Use

Run the script:

python stego.py

Encrypt a Message:

Click on "Encrypt Image"

Select an image file (.png, .jpg, .jpeg)

Enter the secret message

Enter a password

The encoded image will be saved on the desktop

Decrypt a Message:

Click on "Decrypt Image"

Select the encoded image

Enter the correct password

The hidden message will be displayed
