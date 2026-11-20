"""Exact partner scores from McKay r38_27.g6.gz record 1. Explore all maximum-score ties in ascending mask order."""
g6=r'ZGoXI_J?Ec@JScg@sa@o_OG\CP?IOd?KCQ?LA?WlH_@AC?i?@Ab?Ql?oY?AO'
bits=''.join(f'{ord(c)-63:06b}' for c in g6[1:]);ind=[0];rows=[]
def append(p):
    n=len(rows);assert p in ind
    rows.append(p);ind.extend([s|1<<n for s in ind if not s&p]);assert max(map(int.bit_count,ind))<=8
for j in range(27):append(sum(1<<i for i in range(j) if bits[j*(j-1)//2+i]=='1'))
def explore(ind, n, path=()):
    eight=[s for s in ind if s.bit_count()==8];seven=[s for s in ind if s.bit_count()==7]
    opts=sorted(p for p in ind if all(p&s for s in eight))
    if not opts:return {n:1}
    universe=(1<<len(opts))-1
    contain=[sum(1<<j for j,p in enumerate(opts) if p>>i&1) for i in range(n)]
    def touching(p):
        v=0
        while p:
            t=p&-p;v|=contain[t.bit_length()-1];p^=t
        return v
    misses=[(s,universe^touching(s)) for s in seven];scores=[]
    for p in opts:
        bad=0
        for s,m in misses:
            if not s&p:bad|=m
        scores.append(len(opts)-(bad&touching(p)).bit_count())
    top=max(scores);leaders=[p for p,v in zip(opts,scores) if v==top]
    print(path,n,len(opts),top,len(leaders),flush=True)
    if top==0:return {n+1:len(leaders)} # no two extensions coexist
    totals={}
    for j,p in enumerate(leaders,1):
        child=ind+[s|1<<n for s in ind if not s&p]
        for size,count in explore(child,n+1,path+(j,)).items():totals[size]=totals.get(size,0)+count
    return totals

if __name__=='__main__': print('terminal labelled histories:',explore(ind,27))
