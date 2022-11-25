import pandas as pd
import os

print("Service started!\nPress 'q' to exit.\n")
while True:
    
    file=input('Please enter file name: ')
    if 'q' == file:
        break

    isFile=os.path.isfile(file)
    if (isFile):

        #read our data with pandas dataframe
        df=pd.read_csv(file)

        #remove duplicated rows 
        df=df.drop_duplicates()

        #group by the first letter 
        df_new=pd.DataFrame()
        df_new['first_letter']=df['full_name'].str[0]
        df_new['str_value']=df['full_name'] +","+ df['email'] +","+ df['location']

        df_new=df_new.groupby('first_letter').agg(lambda x: set(x))

        #to get rid of the header we save the dataframe values
        organised_values=df_new.values                                      
        appearing_letters=df_new.index

        #creating the output string
        output=""
        i=0
        for group in organised_values:
            output=output+appearing_letters[i]+"\n"
            i=i+1
            for value in group[0]:
                output=output+str(value)+"\n"
            output=output+"\n"

        print(output)

        #creating the output file
        f = open("output.txt", "w")
        f.write(output)
        f.close()
    else:
        print("Can't find file with this name. Try Again!")
