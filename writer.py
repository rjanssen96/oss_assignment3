import os, time
path_to_watch = "/securechannel/files/"

def check_folder(folder):
    counter = 0
    removed_counter = 0
    print("loop counter: ",counter)
    print("hello")
    before = dict([(f, None) for f in os.listdir(folder)])

    #Define the basis for the bitstream, we start with 0b to identify the string consists of bytes.

    bitstream = '0b'

    while 1:
        time.sleep(0.11)
        #Check every file in the folder. If the file is hidden.txt, add +1 to the counter
        #If the hidden.txt file does not exists then the remove counter will be +1.
        #If the remove counter is 25 the binary string will be translated to a readable text.
        for f in os.listdir(folder):
            if f == "hidden.txt":
                counter += 1
                print("hidden bestaat al: ", counter)
                break
            else:
                removed_counter += 1
                print("remove counter: ", removed_counter)
                if removed_counter > 25:
                    bin2string(bitstream)
            break


        print(counter)

        #check if file exists in the current list. Otherwise add it to the added list.
        #If a file exists in the before lists but not in de after list. Then te file is removed.
        after = dict([(f, None) for f in os.listdir(folder)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            #Check if hidden.txt is created. Ifso 
            if added[0] == "hidden.txt":
                print("Added: ", ", ".join(added))
                #Deze functie doet nu niks!
                #counter += 1
                print("added counter:", counter)

        if removed:
            print("Hello i'm removed")
            if removed[0] == "hidden.txt":

                if counter > 5:
                    bitstream = bitstream + "0"
                    removed_counter = 0
                    print("Bitstream: ", bitstream)
                else:
                    bitstream = bitstream + "1"
                    removed_counter = 0
                    print("Bitstream: ", bitstream)
                print("Removed counter: ", removed_counter)
                counter = 0
                print("Counter: ",counter)

                print("Removed: ", ", ".join(removed))



        print("removed: ",removed)
        print("added: ",added)

        before = after

def bin2string(bitstream):
    #Check if bitstream only exists of 0b, this will be when there is no file created and the counter has been reached.
    if bitstream == "0b":
        main()
    try:
        #Decode bitstream from bits to characters.
        n = int(bitstream, 2)
        decoded = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        print("cleartext: ", decoded)
        print(bitstream)
        exit()
    except AttributeError:
        print("You must change the timers, because we are not receiving a valid input.\nThe timers can be found in the reader.py script.\n")


def main():
    check_folder(folder=path_to_watch)
main()
