
import csv

path='text_files/housing.csv'
try:
    with open(path, 'r') as file_object:
        lines=file_object.read()
    #print(lines)
except:
    print(f"The file does not exist in the location")

else:
    contents1=lines.split('\n')
    #print(contents1)
    textfile = open("split/011/no.txt", "a")
    for line in contents1[:]:
   
        search='semi-furnished'
        if search in line:
            textfile.write(line + "\n")
        #textfile.close()

    contents2=lines.split('\n')
    #print(contents1)
    textfile = open("split/011/yes.txt", "a")
    
    for line in contents2[:]:
        search='unfurnished'
        if search in line:
            textfile.write(line + "\n")
            #textfile.close()


    contents3=lines.split('\n')
    textfile = open("split/011/yesno.txt", "a")
    for line in contents3[:]:
        search=',furnished'
        if search in line:
            textfile.write(line + "\n")
            


      