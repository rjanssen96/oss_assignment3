import os
import time

def my_function(inputtt):
    for x in range(inputtt):
        1==1
#        print(x)

def make_file():
    f = open("/securechannel/files/hidden.txt", "w+")
    f.write("This is line %d\r\n")
    f.close()
    print("File made!")

def remove_file():
    os.remove("/securechannel/files/hidden.txt")
    print("File removed!")

# gather the string that needs to be converted
word = input("Gimme smth to convert pls: ")
str(word)

# convert the string to the binary representation
binary = bin(int.from_bytes(word.encode(), 'big'))
# remove the first two chars from binary (0b)
binary = binary[2:]
print(binary)

# for each character in the binary string, check if it's a 1 or 0
# if it's a 1, make a file, loop 60.000 times (to waste CPU time) and then remove the file
# if it's a 0, make a file, loop 1.000 times (to waste CPU time) and then remove the file
# The reader can then see what is a one or zero, based on the time it took to remove the file
for char in binary:
    if char == '1':
        make_file()

        begin = time.clock()
        my_function(800000)

        remove_file()

        end = time.clock()
        time_result = end - begin

        print(time_result)

        my_function(1000000)
        # reset the end and
        #end = 0
        #begin = 0
    elif char == '0':
        make_file()

        begin = time.clock()
        my_function(4000000)

        remove_file()

        end = time.clock()
        time_result = end - begin

        print(time_result)

        my_function(1000000)
        #end = 0
        #begin = 0
    else:
        print("Neither 1 nor 0")
