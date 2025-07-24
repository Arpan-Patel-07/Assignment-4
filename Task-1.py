try:
    
    sample_file = open('sample.txt', 'r+')              #open file sample.txt

    line1 = sample_file.read()                          #reading line 1
    line2 = sample_file.read()                          #reading line 2

    print('Reading file cintains : ')
    #printing line 1 and 2
    print(line1)                                       
    print(line2)

    sample_file.close()                                 #close the file sample.txt

except FileNotFoundError:
    print('Error: The file', "'sample.txt'", 'not found.')