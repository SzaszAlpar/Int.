import os

print("Service started!\nPress 'q' to exit.\n")
while True:
    
    
    file=input('Please enter file name: ')
    
    if 'q' == file:
        break
    
    isFile=os.path.isfile(file)
    if (isFile):
        f = open(str(file), "r",encoding="utf-8")

        #we don't ignore the header, we need to know which column is the "full_name"
        header=f.readline() 
        columns=header.split(',')
        index=columns.index("full_name")
        #read every line and put it in their group, based on the full_name's first letter
        groups={}
        for line in f :
            columns=line.split(',')
            first_letter=columns[index][0]                                              
            if(first_letter in groups.keys()):
                groups[first_letter].append(line)
            else:
                groups[first_letter]=[line]
            
        f.close()

        #we have a dictionary where the keys are the appearing first letters, and the values are the string. Ready to create a single string
        output=""
        for key in groups.keys():
            group = [*set(groups[key])]                      #remove duplicated elements
            output=output + key + ":\n"
            for values in group:
                output=output+values
            
            output=output+"\n"

        print(output)

        #creating the output file
        f = open("output.txt", "w")
        f.write(output)
        f.close()
    else:
        print("Can't find file with this name. Try Again!")
