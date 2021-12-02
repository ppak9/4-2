"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.12.02
    3. File_name : py5-r12_박종현
    4. Description : Get the text file and get the sum and average value.
"""

# ----- Define the file to be read and the file to be written. ----- #
inf = input('읽어들일 파일 : ')
outf = input('내 보낼 파일 : ')

# ----- Define the command to use for the file. ----- #

infile = open(inf,'r')
outfile = open(outf,'w')

sum = 0.0
count = 0
for nums in infile:
    num = nums.strip()      #Remove the whitespaces
    sum += float(num)       #Change the variable type
    count += 1

# Write the sum & average in outfile
outfile.write("the sum is " + str(sum)+ '\n')               
outfile.write("the average is"+ str(sum/count))
infile.close()
print('done')               #To see if it's working

