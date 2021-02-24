# Caesar Cipher
This is a basic cipher that works by shifting letters down the alphabet by a specified number of characters.

## Usage
To run the program from the command line, use the following syntax:
```
python caesar.py encrypt|decrypt [OPTIONS...] Files... 
```

NOTE: if your python interpreter has not been added to your PATH variable, you will get a "command not found" error when using the python command. 

Mac users may need to use 'python3' as macs tend to ship with both python (python 2) and python 3.
#### encrypt
takes any number of files, 

#### options
```
-s FileName
```
specify a file for the output to be saved to.
```
-r rotationAmount
```
specify the amount by which to rotate the characters (forward through the alphabet) as an integer. By
default the amount for encryption is 10, and the amount for decryption is 16