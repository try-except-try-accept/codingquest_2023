u=100
with open('7') as f:
    d,w,s=f.read().splitlines(),0,[[0,0]]
    f=[list(map(int,f.split(',')))for f in d[1].split()];z=f.pop(0)
    for m in d[3]:
        x,y=s[0]
        a={"D":(0,1),"U":(0,-1),"L":(-1,0),"R":(1,0)}[m]
        x,y=x+a[0],y+a[1];s.insert(0,[x,y]);s.pop(-1)
        for b in s:
            if not(0<=b[0]<u and 0<=b[1]<u)or s.count(b)>1:
                input(w)
        if s[0]==z:
            w+=100;s.append(s[0]);z=f.pop(0)
        w+=1
