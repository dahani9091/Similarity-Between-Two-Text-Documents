from numpy import *
def ListsVectors(txt1,txt2):
    txt1,txt2=txt1.split(),txt2.split()    # conversion (string to list)
    GlobalTxt=[c for c in txt1]
    V1,V2=[],[]
    for c in txt2:
        q=c in GlobalTxt
        if q == False :
            GlobalTxt.append(c)
    s=0
    for c in GlobalTxt:
        for p in txt1:
            if p==c :
                s+=1
        V1.append(s)
        s=0
    s=0
    for c in GlobalTxt:
        for p in txt2:
            if p==c :
                s+=1
        V2.append(s)
        s=0
    return V1,V2
def similarity(txt1,txt2):
    V1,V2=ListsVectors(txt1, txt2)
    s1=0
    s2=0
    for i in V1:
        s1+=i**2
    s1=sqrt(s1)
    for i in V2:
        s2+=i**2
    s2=sqrt(s2)
    V1,V2=array(V1),array(V2)
    V1=V1/s1
    V2=V2/s2
    similarity=vdot(V1,V2)/(sqrt(vdot(V1,V1))*sqrt(vdot(V2,V2)))
    return similarity
'''demo'''
print(similarity('kp adel adel','al issam issam')) #you are going to find  0 xD









