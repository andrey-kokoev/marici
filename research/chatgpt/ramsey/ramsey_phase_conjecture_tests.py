"""Three falsification tests. Quotient by unit multiplication, cyclic rotations when allowed."""
from itertools import product
from math import gcd
from collections import Counter
from ramsey_hall_center_conjecture import independent
import sys,json
from pathlib import Path

def test(m,mode,limit=None,distinct=False):
    F=(1<<m)-1;seen=set();counts=Counter();witness=None
    def rot(s,k):return ((s<<k)|(s>>(m-k)))&F
    for v in product(range(m),repeat=3):
        w=(0,)+v
        if w in seen:continue
        orb=set()
        # Gate always at 0->1, diagonal always 0->2 (by cyclic coordinate renaming).
        for j in (range(4) if mode=='lock' else [0]):
            t=w[j:]+w[:j];orb.update(tuple((u*(x-t[0]))%m for x in t) for u in range(1,m) if gcd(u,m)==1)
        seen.update(orb);multy=len(orb)
        ds=[(w[(i+1)%4]-w[i])%m for i in range(4)]
        if distinct and (len(set(w))!=4 or len({min(d,m-d) for d in ds})!=4):counts['degenerate']+=multy;continue
        if gcd(m,*v)!=1:counts['unreachable']+=multy;continue
        S=1;prev=0;older=0;n=0;first=None;latest=None;hit=None
        while limit is None or n<limit:
            n+=1;N=S|rot(S,w[1])|rot(S,w[2])|rot(S,w[3]);A=[0]*m
            if N==F:
                for i,j in [(0,1),(1,2),(2,3),(3,0)]+([(0,2)] if mode=='diagonal' else []):
                    a,b=w[i],w[j];d=(b-a)%m
                    if not d:continue
                    starts=rot(prev,(2*a)%m) if mode=='gate' and i==0 else rot(S,a)
                    if mode=='certified' and i==0:
                        # All reversed-detour orders need one unit in donors 0,2,3.
                        starts=rot(older,(w[0]+w[2]+w[3])%m)
                    while starts:
                        h=starts&-starts;starts-=h;p=h.bit_length()-1;q=(p+d)%m;A[p]|=1<<q;A[q]|=h
                tri=any(A[i]&A[j] for i in range(m) for j in range(i) if A[i]>>j&1)
                if first is None:first=(n,tri)
                if tri:break
                latest=(n,A)
                if mode!='lock' and not independent(A,F,10):hit=n;break
            if older==prev==S==N:break
            older,prev,S=prev,S,N
        if mode=='lock' and first and not first[1] and tri:
            return dict(counts),{'weights':w,'coverage_depth':first[0],'triangle_depth':n}
        if hit:
            counts['first success <=16' if hit<=16 else 'first success >16']+=multy
            witness=(w,hit)
        elif latest:counts['triangle-free full layer but no success']+=multy
        else:counts['no triangle-free full layer']+=multy
    assert sum(counts.values())==m**3
    return dict(counts),witness
if __name__=='__main__':
    mode=sys.argv[1];out={}
    for m in (range(3,int(sys.argv[2])+1,2) if mode=='lock' else [39]):
        out[m]=test(m,mode,{'lock':None,'diagonal':16,'gate':32,'certified':32}[mode],'--distinct' in sys.argv);print(m,out[m],flush=True)
        if mode=='lock' and out[m][1]:break
    Path(__file__).with_name('ramsey_phase_test_'+mode+('_distinct' if '--distinct' in sys.argv else '')+'.json').write_text(json.dumps(out,indent=2)+'\n')
