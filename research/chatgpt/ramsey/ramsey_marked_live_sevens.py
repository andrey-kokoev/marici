"""Catalogue-free whole-orbit greedy on 22 positions. Exact score = number of live 7-sets containing an internal edge of the proposed orbit (count each set once). Stop at zero possible positive gain. Verify output directly over all monochromatic candidates."""
from itertools import combinations,permutations
from math import comb
from pathlib import Path
import json
V=range(4);X=[('c',i) for i in V]+[('p',*x) for x in permutations(V,2)]+[('e',*x) for x in combinations(V,2)]
def reflection(x):
    v=tuple((0,1,3,2)[i] for i in x[1:]);return (x[0],*(sorted(v) if x[0]=='e' else v))
R=[X.index(reflection(x)) for x in X];pairs=list(combinations(range(22),2));O=sorted({tuple(sorted({(i,j),tuple(sorted((R[i],R[j])))})) for i,j in pairs});assert len(O)==127
size=comb(22,7);raw=[bytearray((size+7)//8) for _ in O];lookup={e:a for a,o in enumerate(O) for e in o}
for k,ss in enumerate(combinations(range(22),7)):
    j,b=k//8,1<<(k%8)
    for e in combinations(ss,2):raw[lookup[e]][j]|=b
masks=[int.from_bytes(v,'little') for v in raw];del raw

def matches(o,flat):
    def carry(a,b,i):return i if a==b else a if i==b else 6-a-b-i if flat else i
    def emit(x):
        i=x[1];return [(i,carry(0,i,1))] if x[0]=='c' else [x[1:]] if x[0]=='p' else [x[1:],x[:0:-1]]
    return sum(carry(a,b,i)==j for a,i in emit(X[o[0][0]]) for b,j in emit(X[o[0][1]]))

def run(flat,sign,reverse):
    E=set();live=(1<<size)-1;trace=[];active=list(range(len(O)));priority=[matches(o,flat)*sign for o in O];N=[0]*22
    def legal(o):
        # Includes triangles using both added edges.
        test=N.copy()
        for i,j in o:
            if test[i]&test[j]:return False
            test[i]|=1<<j;test[j]|=1<<i
        return True
    while live:
        active=[a for a in active if legal(O[a])];best=max((((live&masks[a]).bit_count(),priority[a],a if reverse else -a,a) for a in active),default=(0,0,0,0));g,_,_,a=best
        if not g:break
        trace.append((a,g));active.remove(a);live&=~masks[a];E.update(O[a]);
        for i,j in O[a]:N[i]|=1<<j;N[j]|=1<<i
    assert not any(N[i]&N[j] for i,j in E)
    count=sum(all(e not in E for e in combinations(ss,2)) for ss in combinations(range(22),7));assert count==live.bit_count()==size-sum(g for a,g in trace)
    def independence(w):
        if not w:return 0
        b=w&-w;return max(independence(w^b),1+independence(w&~(b|N[b.bit_length()-1])))
    return dict(flat=flat,prefer_more=sign==1,reverse=reverse,remaining=count,alpha=independence((1<<22)-1),edges=len(E),trace=trace)
out=[run(f,s,r) for f in (False,True) for s in (1,-1) for r in (False,True)];print([(z['flat'],z['prefer_more'],z['reverse'],z['remaining'],z['alpha'],z['edges']) for z in out]);Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
