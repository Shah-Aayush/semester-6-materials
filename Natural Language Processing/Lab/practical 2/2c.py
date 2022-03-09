import re
s = 'Hello from 19bce245@nirmauni.ac.in to aayush@shah.com about the meeting @2PM www.google.com www.hello.com/okbye'
  
# For EMAIL : 
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 

lst1 = re.findall('\S+@\S+', s)

# For URL : 
# 

lst2 = re.findall('www\.\w*?\.\w{2,3}\S*', s)
#lst1.extend(lst2)

print('Email ids : ')
for string in lst1:
  print('\t>',string)

print('URLs : ')
for string in lst2:
  print('\t>',string)