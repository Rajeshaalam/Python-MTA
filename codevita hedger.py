n,k,a= [int(x) for x in input().split()] 
p=[float(x) for x in input().split(" ")]
p1=[float(x) for x in input().split(" ")]
res=0
while(a!=0 or a<min(p)):
    for i in range(0,k):
        m=max(p1)
        j=p1.index(m)
        if (k-i)*p[j] <= a:
            a=a-(k-i)*p[j]
            res=res+(((k-i)*(m*p[j]))/100)
            p1.remove(m)
            p.pop(j)
            break
print(int(res))


