from colorama import Fore
import hashlib

from PIL import Image
def caesar_cipher(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            char = chr((ord(char) + shift) % 256)
        result += char
    return result
def affine_cipher(string, a, b):
    result = ""
    for char in string:
        if char.isalpha():
            char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
        result += char
    return result
def text_to_binary(string):
    result = ""
    for char in string:
        result += bin(ord(char))[2:].zfill(8)
    return result
def binary_to_image(string):
    img = Image.new('RGB', (len(string), 1))
    pixels = img.load()
    for i in range(img.size[0]):
        if string[i] == "0":
            pixels[i, 0] = (0, 0, 0)
        else:
            pixels[i, 0] = (255, 255, 255)
    img.save("image.png")
def xor(string, key):
    result = ""
    for char in string:
        result += chr(ord(char) ^ ord(key))
    return result
#---
prompt=f"""
{Fore.RED}[1]{Fore.GREEN} Caesar Cipher
{Fore.RED}[2]{Fore.GREEN} Affine Cipher
{Fore.RED}[3]{Fore.GREEN} SHA-1
{Fore.RED}[4]{Fore.GREEN} SHA-224
{Fore.RED}[5]{Fore.GREEN} SHA-256
{Fore.RED}[6]{Fore.GREEN} SHA-512
{Fore.RED}[7]{Fore.GREEN} Text to binary
{Fore.RED}[8]{Fore.GREEN} Binary to image
"""
print(prompt)
inputy = input(f"Enter the cipher/hash you want to use: \n{Fore.RED}>>>{Fore.RESET}")
if inputy == "1":
    xyy = input(f"{Fore.GREEN}Enter the text you want to encrypt: \n{Fore.RED}>>>{Fore.RESET}")
    yzz = int(input(f"{Fore.GREEN}Enter the shift value: \n{Fore.RED}>>>{Fore.RESET}"))
    print(f"{Fore.RED}[+]{Fore.GREEN} Ciphered text{Fore.RESET}\n{caesar_cipher(xyy, yzz)}")
if inputy == "2":
    xyy = input(f"{Fore.GREEN}Enter the text you want to encrypt: \n{Fore.RED}>>>{Fore.RESET}")
    yzz = int(input(f"{Fore.GREEN}Enter the a value: \n{Fore.RED}>>>{Fore.RESET}"))
    zzz = int(input(f"{Fore.GREEN}Enter the b value: \n{Fore.RED}>>>{Fore.RESET}"))
    print(f"{Fore.RED}[+]{Fore.GREEN} Ciphered text{Fore.RESET}\n{affine_cipher(xyy, yzz, zzz)}")
if inputy == "3":
    xyy = input(f"{Fore.GREEN}Enter the text you want to hash: \n{Fore.RED}>>>{Fore.RESET}")
    print(f"{Fore.RED}[+]{Fore.GREEN} Hashed text{Fore.RESET}\n{hashlib.sha1(xyy.encode()).hexdigest()}")
if inputy == "4":
    xyy = input(f"{Fore.GREEN}Enter the text you want to hash: \n{Fore.RED}>>>{Fore.RESET}")
    print(f"{Fore.RED}[+]{Fore.GREEN} Hashed text{Fore.RESET}\n{hashlib.sha224(xyy.encode()).hexdigest()}")
if inputy == "5":
    xyy = input(f"{Fore.GREEN}Enter the text you want to hash: \n{Fore.RED}>>>{Fore.RESET}")
    print(f"{Fore.RED}[+]{Fore.GREEN} Hashed text{Fore.RESET}\n{hashlib.sha256(xyy.encode()).hexdigest()}")
if inputy == "6":
    xyy = input(f"{Fore.GREEN}Enter the text you want to hash: \n{Fore.RED}>>>{Fore.RESET}")
    print(f"{Fore.RED}[+]{Fore.GREEN} Hashed text{Fore.RESET}\n{hashlib.sha512(xyy.encode()).hexdigest()}")
if inputy == "7":
    xyy = input(f"{Fore.GREEN}Enter the text you want to convert to binary: \n{Fore.RED}>>>{Fore.RESET}")
    print(f"{Fore.RED}[+]{Fore.GREEN} Binary text{Fore.RESET}\n{text_to_binary(xyy)}")
if inputy == "8":
    xyy = input(f"{Fore.GREEN}Enter the binary text you want to convert to image: \n{Fore.RED}>>>{Fore.RESET}")
    binary_to_image(xyy)
    print(f"{Fore.RED}[+]{Fore.GREEN} Image saved as image.png{Fore.RESET}")
#---