input_string="pwwkew"
s=set()
temp=0
max_val=0

for i in range(len(input_string)):
    while(input_string[i] in s):
        s.remove(input_string[temp])
        temp+=1
    s.add(input_string[i])
    max_val=max(max_val,i-temp+1)
print(max_val)