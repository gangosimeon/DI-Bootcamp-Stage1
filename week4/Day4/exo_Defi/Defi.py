import string
liste=[
    ["7","i","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ","#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"],
    ]
ch1=ch2=ch3=""

for chain in liste:
    ch1=ch1+chain[0]
    ch2=ch2+chain[1]
    ch3=ch3+chain[2] 
ch=ch1+ch2+ch3

j=0
while j < (len(ch)-1):
    if ch[j] not in string.ascii_letters and ch[j+1] not in string.ascii_letters: 
        ch=ch.replace(ch[j]+ch[j+1]," ")
        for k in ch:
            if k not in string.ascii_letters and k!=" ":
                ch=ch.replace(k,"")
    j+=1             
print(ch)