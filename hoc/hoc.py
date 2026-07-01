f = input()
num = 1
string = ""
try:
    for i in range(1, len(f)):
        if f[i] == f[i-1]:
            num+=1
        else:
            string += f[i-1] + str(num)
            num = 1
    string += f[-1]+str(num)
            
except:
    pass
print(string)
    
