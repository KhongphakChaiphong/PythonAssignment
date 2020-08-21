import re
name=input("Enter file:")
if len(name)<1:name="regex_sum_42.txt"
handle=open(name)
number=list()
for line in handle:
    x=re.findall('[0-9]+',line)
    number=number+x
sum = 0
for i in number:
    sum=sum+int(i)
print(sum)

