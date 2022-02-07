# Encrypt and Decrypt Files

## Description

 Python program used for encrypting and decrypting files, usisng a password chosen by the user. This is a __Command-Line__ program, but in the future I'll try to update it to a GUI program.

## Instalation requisits

First you'll need to install the necessary Python libraries.

- Type __pip install -r requirements.txt__ on your terminal.

## Encrypt a file

After installing the requisits you just need to copy the path of the file you want to encrypt and run the following code in the terminal:

- python3 __*\*.py script\**__ -i __*\*path of the file\**__ -e

After you run the code above you'll be asked for a password.

Finally, will be created a zip, in the directory of the file used, containing a *.bin* file. The *.bin* file contains the key used for encryption and is needed for decrypting the file.

__Note:__ The password that you chose for the encryption will be needed to decrypt the file, so don't lose the password. The *.bin* file is guarded by the same password and nobody can access the file without that password.

## Decrypt a file

The process it´s identical to the encryption. To decrypt you just need to run the following code in the terminal:

- python3 __*\*.py script\**__ -i __*\*path of the file\**__ -d

Then you have to type the password and will apear all the text in the file.
