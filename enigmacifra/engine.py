"""
MIT License

Copyright (c) 2024 Darshan P.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This script calculates the percentage of the current day that has elapsed and 
displays it as a progress bar in the console.
"""


import json
from enigmacifra.defaultRotor import ROTORS
Rotor_lst = ROTORS


def rotate_single_dict(x, dc):
    """
    Rotate the keys of the dictionary 'dc' by 'x' positions to simulate the rotation of an Enigma rotor.

    Args:
        x (int): The number of positions to rotate the dictionary.
        dc (dict): The dictionary representing a rotor's wiring.

    Returns:
        dict: A new dictionary with keys rotated by 'x' positions.
    """
    dc_rotated = {}
    keys, values = zip(*dc.items())
    for cnt in range(len(dc)):
        dc_rotated[keys[cnt]] = values[(cnt - x) % len(dc)]
    return dc_rotated


def Encrypting_package(pin, rotor_list):
    """
    Encrypts an entire package (list of rotors) using the provided PIN to determine the rotation for each rotor.

    Args:
        pin (list): A list of integers where each integer is used to rotate a corresponding rotor.
        rotor_list (list): A list of rotor dictionaries to be encrypted.

    Returns:
        list: A list of encrypted rotors.
    """
    package_encrypted = []
    for i in range(8):
        pin_digit = pin[i]
        package_encrypted.append(rotate_single_dict(pin_digit, rotor_list[i]))
    return package_encrypted


def passing(pin_encrypted_list, char):
    """
    Passes a character through a series of rotors to encrypt it.

    Args:
        pin_encrypted_list (list): A list of encrypted rotors through which the character is passed.
        char (str): The character to be encrypted.

    Returns:
        str: The encrypted character.
    """
    for rotor in pin_encrypted_list:
        char = rotor[char]
    return char


def get_key_from_value(dc, value):
    """
    Retrieve the key from a dictionary that corresponds to the specified value.

    Args:
        dc (dict): The dictionary from which to find the key.
        value (any): The value for which the corresponding key is required.

    Returns:
        any: The key corresponding to the provided value.

    Raises:
        ValueError: If the value is not found in the dictionary.
    """
    for key, val in dc.items():
        if val == value:
            return key
    raise ValueError("Value not found in dictionary")


def unpassing(pin_encrypted_list, char):
    """
    Reverse the encryption process for a character by passing it through the rotors in reverse order.

    Args:
        pin_encrypted_list (list): A list of encrypted rotors through which the character is reversed.
        char (str): The character to be decrypted.

    Returns:
        str: The decrypted character.
    """
    for i in range(1, 9):
        char = get_key_from_value(pin_encrypted_list[-i], char)
    return char


"""
Tattoo translates to 'flfvv'. To prevent this repetition, we will update the 'PEL' (Pin Encrypted List) or 'packageE' after every use. This update involves rotating the list by 1 position for each encryption process.
"""


def updating(pin_encrypted_list, encrypt=True):
    """
    Updates the rotor configuration by rotating each rotor after an encryption or decryption process.

    Args:
        pin_encrypted_list (list): The list of rotors to update.
        encrypt (bool, optional): Specifies the direction of the update (True for encryption, False for decryption).
                                   Defaults to True.

    Returns:
        list: The updated list of rotors.
    """
    direction = 1 if encrypt else -1
    pin = [direction] * 8
    return Encrypting_package(pin, pin_encrypted_list)


def process_e(pin_encrypted_list, password):
    """
    Encrypt a string using the provided PIN Encrypted List.

    Args:
        pin_encrypted_list (list): The list of rotors used for encryption.
        password (str): The message to be encrypted.

    Returns:
        str: The encrypted message.
    """
    encrypted_password = ""
    for char in password:
        encrypted_password += passing(pin_encrypted_list, char)
        pin_encrypted_list = updating(pin_encrypted_list)
    return encrypted_password


def process_d(PEL, passwordE):
    """
    Decrypt a string using the provided PIN Encrypted List.

    Args:
        PEL (list): The list of rotors used for decryption.
        passwordE (str): The encrypted message to be decrypted.

    Returns:
        str: The decrypted message.
    """
    password = ""
    for str_ in passwordE:
        password += unpassing(PEL, str_)
        PEL = updating(PEL)
    return password


"""The above rotor list is to be well backed-up and should never be disturbed as it has contains the shuffled rotors"""
if __name__ == "__main__":
    # Interaction with user for PIN and choice of operation (Encrypt/Decrypt)

    pin = input("Enter your 8-digit PIN to encrypt/decrypt the password: ")
    if len(pin) == 8 and pin.isnumeric():
        PIN = [int(i) for i in pin]
        PEL = Encrypting_package(PIN, Rotor_lst)
        eVSd = input('Please enter "E" to encrypt or "D" to decrypt: ')
        if eVSd.lower() == "e":
            password = input("Enter the password to be encrypted: ")
            passwordE = process_e(PEL, password)
            print("Your encrypted password is: ", passwordE)
        elif eVSd.lower() == "d":
            passwordE = input("Enter your encrypted passowrd: ")
            password = process_d(PEL, passwordE)
            print("Your decrypted password: ", password)
        else:
            print('Get lost!! I aksed to enter only "E" or "D"')
            print("Thank you for using me!")
    else:
        if pin.isnumeric() == False:
            print("The above is not PIN, Please only enter numbers")
        else:
            if len(pin) == 1:
                print(f"The above PIN is of 1-digit only")
            elif len(pin) < 8:
                print(f"The above PIN is of only {len(pin)}-digits")
            else:
                print(f"The above PIN is of {len(pin)}-digits")
        print("Program ended!")
