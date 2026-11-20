"""Four-pin Walsh differences on the Paley(17) two-color (4,4) graph. No diagonal readings."""
from itertools import combinations
from collections import Counter,defaultdict
V=range(17); squares={i*i%17 for i in range(1,17)}
def red(a,b):return (a-b)%17 in squares
def profile(pins,v):return sum(int(red(p,v))<<k for k,p in enumerate(pins))
def chi(s,x):return (-1)**((s&x).bit_count()%2)
if __name__=='__main__':
    assert all(len({red(i,j) for i,j in combinations(q,2)})==2 for q in combinations(V,4))
    census=Counter()
    for pins in combinations(V,4):
        xs={v:profile(pins,v) for v in V if v not in pins};groups=defaultdict(set)
        for i,j in combinations(xs,2):groups[xs[i]^xs[j]].add(red(i,j))
        census[sum(len(g)==2 for g in groups.values())]+=1
    print('mixed labels per pin set:',sorted(census.items()))
    pins=(0,1,2,3);cols=(4,5,6,7);xs={v:profile(pins,v) for v in cols}
    print('profiles',xs)
    for i,j in combinations(cols,2):
        x,y=xs[i],xs[j];d=x^y
        for s in range(16):
            z=1
            for b in (1,2,4,8):
                if s&b:z*=chi(b,x)*chi(b,y)
            assert z==chi(s,d)
        print(i,j,d,red(i,j))
    for i,j,k in combinations(V,3):
        if all(red(a,b) for a,b in combinations((i,j,k),2)):
            print('red triangle',i,j,k);break
