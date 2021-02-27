# Caesar Cipher
This is a basic cipher that works by shifting letters down the alphabet by a specified number of characters.

## Usage
To run the program from the command line, use the following syntax:
```
python caesar.py [OPTIONS...] Files... 
```

NOTE: if a python interpreter has not been added to your PATH variable, you will get a "command not found" error when using the python command. 

Mac users may need to use 'python3' as macs tend to ship with both python 2 and python 3.

`Files...` refers to one or more relative paths to files

### Options
OPtions are case-sensitive in case future capital letter options are needed.
By default, the smartCipher option will be used. 
NOTE: when using the smartCipher option, confidence is affected by how many non-letter symbols are found, including punctuation.
```
-s
```
Save output to a file. Program will prompt user to enter the path(including the file name).
```
-r
```
specify the amount by which to rotate the characters (forward through the alphabet) as an integer.
This option will disable the smartCipher, so that you can manually create encrypted files. You will be 
prompted to enter a rotation amount as an integer. If a character is rotatedd past 'z', it will wrap to 
the beginning of the alphabet; consequently, rotations greater than 26 are not useful.



## Examples
`msg0.txt` was created by rotating each character by 16 places. To decipher this, the default rotation of 10 will work:
```
$ python src/caesar.py samples/msg0.txt
```

If I wanted to decipher the file `rotate_me_by_21.md`, I could run
```
$ python src/caesar.py -r 21 samples/rotate_me_by_21.md
```
To save the output into a markdown file:
```
$ python src/caesar.py -r 21 samples/rotate_me_by_21.md -s deciphered.md
```
As you can see, the order of the optional flags doesn't matter, so long as a flag is followed by a valid argument.
