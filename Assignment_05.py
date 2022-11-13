#------------------------------------------#
# Title: Assignment_05.py
# Desc: Lab05-A starter script edited
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# SHarms, 2022-Nov-10, Edited File
# SHarms, 2022-Nov-12, Edited File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strRow = ''

# Get user Input
print('Write or Read file data.')
while True:
    print('\n[a] add data to list\n[w] to write data to file\n[r] to read data from file')
    print('[x] to delete an entry\n[d] display data\n[exit] to quit')
    strChoice = input('a, w, r, x, d, or exit: ').lower()  # convert choice to lower case at time of input
    print('\n')

    if strChoice == 'exit':
        break
    if strChoice == 'a':
        # Ask user to input data and store it in the in-memory list
        artist = input('Artist Name: ')
        title = input('Album Title: ')
        lstRow = {'artist':artist, 'title':title}      
        lstTbl.append(lstRow)
        print('Your entry: ', lstRow)
        pass
    elif strChoice == 'w':
        # Add code here to write from in-memory list to file
        with open(strFileName, 'w') as f:
            for item in lstTbl:
                strRow = item['artist'] + ',' + item['title'] + '\n'
                f.write(strRow)
        f.close()
        pass
    elif strChoice == 'r':
        # Read the file line by line into in-memory list.
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'artist': lstRow[0], 'title': lstRow[1]}
            lstTbl.append(dicRow)
            print(dicRow)
        objFile.close()
        pass
    elif strChoice == 'x':
        #Delete entry as indicated by user.
        garb_Art = input('Artist to delete:')
        for i in range(len(lstTbl)):
            if lstTbl[i]['artist'] == garb_Art:
                del lstTbl[i]
                break 
        pass
    elif strChoice == 'd':
        # Display the data to the user.
        print('Here are all the rows:\n',lstTbl)
        pass
    else:
        print('Please choose either a, w, r, x, or exit!')

