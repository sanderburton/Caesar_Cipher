# Caesar Cipher
This is a basic cipher that works by rotating each character of a message forward through the alphabet
by a specified number of rotations. It is called 'Caesar Cipher' because it has been reported that
Julius Caesar used to encrypt military messages.

I built this from scratch, using python. All work here is my own (though I didn't come up with the
Caesar cipher idea, I did come up with this implentation). The words.txt file was downloaded from SCOWL (http://app.aspell.net/create).

## Smart Cipher
This program is able to take a ciphered message and figure out how many rotations are needed to translate
that message into English. By default the smart cipher option is enabled.

The Smart Cipher option works by trying each rotation amount and comparing the output to a dictionary
of words in the english language. It then reports the percentage of words that were present in the dictionary as the 'confidence'.
## Usage
To run the program from the command line, use the following syntax:
```
python caesar.py [OPTIONS...] Files... 
```

NOTE: if a python interpreter has not been added to your PATH variable, you will get a "command not found" error when using the python command. 

Mac users may need to use 'python3' as macs tend to ship with both python 2 and python 3.

`Files...` refers to one or more relative paths to files

### Options
- Options are case-sensitive in case future capital letter options are added.</br>
- By default, the smartCipher option will be used (use -r to overwrite this). </br>
NOTE: when using the smartCipher option, confidence is affected by how many non-letter symbols are found adjacent to words, including punctuation marks.
```
-s
```
Save output to a file. Program will prompt user to enter a path(including the file name).
```
-r
```
Specify the amount by which to rotate the characters (forward through the alphabet) as an integer.
This option will disable the smartCipher, so that you can manually encrypt/decrypt files. You will be 
prompted to enter a rotation amount as an integer. If a character is rotatedd past 'z', it will wrap to 
the beginning of the alphabet; consequently, rotations greater than 26 are not very useful.



## Examples
To let the Smart Cipher do the work for you, simply give a path to an encrypted file:
```
$ python src/caesar.py samples/msg0.txt
```
Smart Cipher will figure out how many places each character needs to be rotated in order to produce
a human readable message (in english).

`msg0.txt` was created by rotating each character by 16 places. To decipher this, a rotation of 10 is needed (16 + 10 = 26). To manually decipher this file I could run:
```
$ python src/caesar.py -r samples/msg0.txt
Enter rotation amount as an integer: 10
```

If I wanted to decipher the file `rotate_me_by_21.md` (manually), I could run
```
$ python src/caesar.py samples/rotate_me_by_21.md -r
Enter rotation amount as an integer: 21
```
As you can see in these two examples, the order/location of the optional flags doesn't matter. I tried to make the command-line 
interface as user-proof as possible. If invalid input is entered a helpful error message will be
displayed.

To save the output into a text file named `output.txt`:
```
$ python src/caesar.py -rs samples/rotate_me_by_21.md
Enter rotation amount as an integer: 21
Enter relative path to file save location (including the desired filename): output.txt

```

