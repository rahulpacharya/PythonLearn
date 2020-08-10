import Constants


#Reading from a file - using file pointer, file object
fp = open(Constants.DATA_TXT_FILE_1, 'r')  # opening
content1 = fp.read()          # reading
fp.close()                   # closing
print(content1)

# Append to a file , to write - use 'w'
fob = open(Constants.DATA_TXT_FILE_1, 'a')
fob.write("Regards, Rahul Acharya\n")
fob.close()

fob = open(Constants.DATA_TXT_FILE_1, 'r')  # opening
content2 = fob.read()          # reading
fob.close()                   # closing
print(content2)
###########################################
#Regular expressions are patterns that help in filtering the text possessing them, and also in extracting portions of data that match the patterns
import re
pattern='for'
text='information'
if re.search(pattern, text):
    print('Yes')
###########################################
#### Search pattern and extract
###########################################
import io
txt_1 = ''' 

The life of a -poet- is lonely like his thoughts.
While he may yearn to feel one with the world,

the world casts him away -like a cruel mistress!
But *ofcourse*, he is not disheartned*, 
for how does one become a -poet- if not through a multitude of rejections?
'''

fp = io.StringIO(txt_1)
txt_list_1 = fp.readlines()
print(txt_list_1)
print(txt_list_1[:3])
txt_list_1 = [i.strip("\n ") for i in txt_list_1] #just i.strip() also works
print(txt_list_1)

match_object = re.search('-(.*)-',txt_list_1[2])
print(match_object.group(1))


portions = []
for i in txt_list_1:
    mtch1 = re.search('-(.*)-',i)
    mtch2 = re.search('\*(.*)\*',i)
    if mtch1 != None:
        portions.append(mtch1.group(1))
    if mtch2 != None:
        portions.append(mtch2.group(1))
                
print(portions)

###############################################
## Replace a word in string
###############################################
addr = ['100 NORTH MAIN ROAD','100 BROAD ROAD APT.','SAROJINI DEVI ROAD','BROAD AVENUE ROAD']
print(addr)
def subst(pattern, replace_str, string):
    return(string.replace(pattern,replace_str))
new_address = [subst(' ROAD',' RD.',i) for i in addr]
print(new_address)
