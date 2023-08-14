def horspool(text,pattern,text_file):
    utext = text.upper()
    upattern = pattern.upper()
    alphabet = set(utext + upattern)
    distlist = list(alphabet)
    m = len(upattern)

    n = len(utext)

    dict={}
    for i in range(0,len(distlist)):
        dict[distlist[i]] = m
    for j in range(0,m-1):
        dict[upattern[j]] = m-j-1
        
    
    pos = 0
    count =0
    while pos<= n-m:
        j = m-1
        while j>=0 and utext[pos+j] == upattern[j]:
            j = j-1
        if j==-1:
            count+=1
            linetwo = ("\n\tfound position is "+str(pos)+ " to " +str(pos+m-1)+" in the following text line")
            #print(linetwo)
            text_file.write(linetwo)
        pos = pos +dict[utext[pos+m-1]]    
    if count>0:
        linethree=("\n\t"+text) 
        #print(linethree)
        text_file.write(linethree)
        
    return count

def horspool_dot(text,pattern,text_file):
    utext = text.upper()
    upattern = pattern.upper()
    alphabet = set(utext + upattern)
    distlist = list(alphabet)
    m = len(upattern)
    n = len(utext)
    dict={}
    for i in range(0,len(distlist)):
        dict[distlist[i]] = m
    for j in range(0,m-1):
        dict[upattern[j]] = m-j-1
    pos = 0
    count =0
    while pos<= n-m:
        j = m-1
        while j>=0 and utext[pos+j] == upattern[j]  or upattern[j]=="." :
            j = j-1
        if j==-1:
            count+=1
            linetwo = ("\n\tfound position is "+str(pos)+ " to " +str(pos+m-1)+" in the following text line")
            #print(linetwo)
            text_file.write(linetwo)
        pos = pos +dict[utext[pos+m-1]]    
    if count>0:
        linethree=("\n\t"+text) 
        #print(linethree)
        text_file.write(linethree)
        
    return count

def horspool_quest(text,pattern,text_file):
    utext = text.upper()
    upattern = pattern.upper()
    index = upattern.find("?")
    mod_pattern1= upattern.replace(upattern[index],"")
    mod_pattern2 = mod_pattern1.replaceu(upattern[index-1],"")

    num1 = horspool(text,mod_pattern1,text_file)
    num2 = horspool(text,mod_pattern2,text_file)

    return num1+num2

def horspool_begg(text,pattern,text_file):
    utext = text.upper()
    upattern = pattern.upper()
    mod_pattern = upattern.replace(upattern[0],"")
    alphabet = set(utext + mod_pattern)
    distlist = list(alphabet)
    m = len(mod_pattern)
    n = len(utext)

    dict={}
    for i in range(0,len(distlist)):
        dict[distlist[i]] = m
    for j in range(0,m-1):
        dict[mod_pattern[j]] = m-j-1
    pos = 0
    count =0
    while pos<= n-m:
        j = m-1
        while j>=0 and utext[pos+j] == mod_pattern[j]:
            j = j-1
        if j==-1 and (utext[pos+j]==' ' or pos==0):
            count+=1
            linetwo = ("\n\tfound position is "+str(pos)+ " to " +str(pos+m-1)+" in the following text line")
            #print(linetwo)
            text_file.write(linetwo)
        pos = pos +dict[utext[pos+m-1]]    
    if count>0:
        linethree=("\n\t"+text) 
        #print(linethree)
        text_file.write(linethree)
        
    return count

def horspool_end(text,pattern,text_file):
    utext = text.upper()
    upattern = pattern.upper()
    length = len(upattern)
    mod_pattern = upattern.replace(upattern[length-1],"")
    alphabet = set(utext + mod_pattern)
    distlist = list(alphabet)
    m = len(mod_pattern)
    n = len(utext)

    dict={}
    for i in range(0,len(distlist)):
        dict[distlist[i]] = m
    for j in range(0,m-1):
        dict[mod_pattern[j]] = m-j-1
    pos = 0
    count =0
    while pos<= n-m:
        j = m-1
        while j>=0 and utext[pos+j] == mod_pattern[j]:
            j = j-1    
        if j==-1 and (pos == n-m-1 or utext[pos+m]==" " or utext[pos+m].isalpha()==0):
            count+=1
            linetwo = ("\n\tfound position is "+str(pos)+ " to " +str(pos+m-1)+" in the following text line")
            #print(linetwo)
            text_file.write(linetwo)
        pos = pos +dict[utext[pos+m-1]]    
    if count>0:
        linethree=("\n\t"+text) 
        #print(linethree)
        text_file.write(linethree)
        
    return count

n = int(input("what is the file pair do you want to input ?"))

text_file = open("Output/output"+str(n)+".txt", 'w')
f = open("Input/Text/text"+str(n)+".txt","r")
text = f.readlines()
p = open("Input/Pattern/pattern"+str(n)+".txt","r")
pattern =  p.readline()
print(pattern)
        
lineone = ("\n"+("text"+str(n)+".txt")+" Searching pattern is "+"\""+pattern+"\"")
#print(lineone)
text_file.write(lineone)
count =0
for line in text:
    if pattern.find(".")!= -1:
        count+= horspool_dot(line,pattern,text_file)
    elif pattern.find("?")!= -1:
        count+= horspool_quest(line,pattern,text_file)
    elif pattern.find("^")!= -1:
        count+= horspool_begg(line,pattern,text_file)
    elif pattern.find("$")!= -1:
        count+= horspool_end(line,pattern,text_file)     
    else:
        count+= horspool(line,pattern,text_file)
       
endline =("\nNumber of matches found : "+ str(count))
#print(endline)
text_file.write(endline)
print("output files are generated successfully ")


