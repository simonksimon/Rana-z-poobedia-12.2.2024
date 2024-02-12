def create_interval(inp):
    mid=[]
    for i in range(len(inp)):
        mid.append(inp[i])
    end=False
    safety=0
    while end==False and safety<100:
        end==True
        for i in range(len(inp)-1):
            i+=1
            if inp[i-1]>inp[i]:
                mid[i-1]=inp[i]
                mid[i]=inp[i-1]
                for i in range(len(mid)):
                    inp[i]=mid[i]
                end==False
        safety+=1

    out=[str(mid[0])]
    y=0
    for i in range(len(mid)-1):
        i+=1
        if mid[i]!=mid[i-1]+1:
            out[y]=out[y]+","+str(mid[i-1])
            y+=1
            out.append(str(mid[i]))
    out[y]=out[y]+","+str(mid[-1])

    t1=[]
    t2=[]
    for i in range(len(out)):
        for y in range(len(out[i])):
            if out[i][y]==",": t=y
        t1.append(int(out[i][0:t]))
        t2.append(int(out[i][t+1:]))
    r=list(zip(t1, t2))
    print(r)
    return r

create_interval(data)



