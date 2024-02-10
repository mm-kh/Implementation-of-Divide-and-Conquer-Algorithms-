def prod(u,v):
    u=str(u)
    v=str(v)
    n=max(len(u),len(v))
    u=int(u)
    v=int(v)
    if(v==0 or u==0):
        return 0 
    else:
        if(n<=2):
            return u*v
        else:
            m=int(n/2)
            M=int((n+1)/2)
            u=str(u)
            v=str(v)
            if len(u)>len(v):
                x=u[:M]
                y=u[M:]
                w=v[:m]
                z=v[m:]
            elif len(u)<len(v):
                x=u[:m]
                y=u[m:]
                w=v[:M]
                z=v[M:] 
            else:
                x=u[:M]
                y=u[M:]
                w=v[:M]
                z=v[M:]
            x=int(x)
            y=int(y)
            w=int(w)
            z=int(z)
            return (prod(x,w) * (10**(2*m))) + ((prod(x,z) + prod(w,y)) * (10**m)) + (prod(y,z))
            # one=prod(x,w)
            # two=prod((x+y),(x+z))
            # three=prod(y,z)
            # return one*(10**(2*m)) + (two-one-three)*(10**m) + three


u=int(input())
v=int(input())
resault=prod(u,v)
print(resault)
            
