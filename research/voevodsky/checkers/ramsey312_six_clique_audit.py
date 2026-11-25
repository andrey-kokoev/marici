"""Exact K6 census and small chromatic lower bounds (join of triangle and odd cycle)."""
from pathlib import Path
from itertools import combinations
import json,sys
D=Path(__file__).resolve().parents[1]/'results';out=[]
def bits(m):
 while m:b=m&-m;m-=b;yield b.bit_length()-1
for line,dom in zip(Path(sys.argv[1]).read_text().splitlines(),(D/'ramsey312_five_neg_domains.txt').read_text().splitlines(),strict=True):
 r=line.split();z=dom.split();assert r[:5]==z[:5];s=list(map(int,z[7:]));G=[0]*len(s)
 for t in r[5:]:
    i,j,c=map(int,t.split(':'));assert i!=j;G[i]|=1<<j;G[j]|=1<<i
 def count(m,k):
    if k==1:return m.bit_count()
    n=0
    while m.bit_count()>=k:b=m&-m;m^=b;n+=count(m&G[b.bit_length()-1],k-1)
    return n
 n=count((1<<len(s))-1,6);best=None
 for i in range(len(s)):
    for j in bits(G[i]&((1<<i)-1)):
        for k in bits(G[i]&G[j]&((1<<j)-1)):
            common=G[i]&G[j]&G[k];paths={}
            for root in bits(common):
                if root in paths:continue
                paths[root]=[root];q=[root]
                for v in q:
                    for w in bits(G[v]&common):
                        if w not in paths:paths[w]=paths[v]+[w];q.append(w)
                        elif len(paths[v])%2==len(paths[w])%2:
                            a,b=paths[v][:],paths[w][:];
                            while len(a)>1 and len(b)>1 and a[1]==b[1]:a.pop(0);b.pop(0)
                            cyc=a+b[:0:-1];assert len(set(cyc))==len(cyc) and len(cyc)%2 and all(G[x]>>y&1 for x,y in zip(cyc,cyc[1:]+cyc[:1]));
                            if best is None or len(cyc)<len(best[1]):best=([s[i],s[j],s[k]],[s[t] for t in cyc])
                if best and len(best[1])==5:break
            if best and len(best[1])==5:break
        if best and len(best[1])==5:break
    if best and len(best[1])==5:break
 out.append(dict(deletions=r[:5],six_cliques=n,triangle_cycle=best));print(r[:5],n,len(best[1]) if best else None)
(D/'ramsey312_six_clique_audit.json').write_text(json.dumps(out))
