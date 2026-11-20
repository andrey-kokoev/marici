"""Recover an oriented five-cycle from star intersection sizes, without using stored row phases. Address the four slots by successor power. Compare intrinsic and common-clock readings under the stored pole reversal."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';w=json.loads((D/'ramsey_37_dual_stars.json').read_text());F=[[set(s) for s in f] for f in w['stars']];refl=w['reflection']
def read(f,g):
    def pick(h):
        ans=[]
        for s in f:
            js=[j for j,t in enumerate(g) if len(s&t)==h];assert len(js)==1;ans+=js
        assert len(set(ans))==5;return ans
    mate=pick(0);one=pick(1);succ=[mate.index(j) for j in one];out=[]
    for i in range(5):
        j=i;row=[]
        for k in range(1,5):
            j=succ[j];u,=f[i]&f[j];row.append(u)
        assert set(row)==f[i] and succ[j]==i;out.append(row)
    return succ,out
p,a=read(*F);q,b=read(*F[::-1]);assert all(q[p[i]]==i for i in range(5));assert all([refl[u] for u in a[i]]==b[(-i)%5] for i in range(5));out=dict(pole0_successor=p,pole6_successor=q,powers=[1,2,-2,-1],pole0=a,pole6=b);(D/'ramsey_37_star_addresses.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
