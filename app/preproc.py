import numpy as np
import csv
import re


print 'Extracting data'

### POSITIVE DATA ####
csv_file_object = csv.reader(open('twitDB_sarcasm.csv', 'rU'))
pos_data=[] 
    
for row in csv_file_object:
    if len(row[0:])==1:
        temp=re.sub(r'#\w+\s?','',row[0:][0])
        if len(temp)>0 and 'http' not in temp and temp[0]!='@' and '\u' not in temp:
            temp=re.sub(r'@\w+\s?','',temp)
            temp.replace('sarcastic','')
            temp.replace('sarcasm','')
            pos_data.append(temp)
pos_data=list(set(pos_data))
pos_data = np.array(pos_data)


### NEGATIVE DATA ####
csv_file_object = csv.reader(open('twitDB_regular.csv', 'rU'))
neg_data=[] 
    
for row in csv_file_object:
    if len(row[0:])==1:
        temp=re.sub(r'#\w+\s?','',row[0:][0])
        if len(temp)>0 and 'http' not in temp and temp[0]!='@' and '\u' not in temp:
            temp=re.sub(r'@\w+\s?','',temp)
            temp.replace('sarcastic','')
            temp.replace('sarcasm','')
            neg_data.append(temp)
neg_data=list(set(neg_data))
neg_data = np.array(neg_data)



print 'Number of  sarcastic tweets :', len(pos_data)
print 'Number of  non-sarcastic tweets :', len(neg_data)


np.save('posproc',pos_data)
np.save('negproc',neg_data)



