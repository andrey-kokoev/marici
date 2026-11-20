"""All one- and two-border continuations after twinning 0 on the 35-circle. uv run --with igraph python <file>."""
from collections import Counter
from itertools import combinations
import igraph as ig
from ramsey_clique_power_blowup import layers
S={1,34,7,28,11,24,16,19};parent=[*range(35),0];n=len(parent);N=[sum(1<<j for j,y in enumerate(parent) if (x-y)%35 in S) for x in parent];sets=layers(N);assert max(map(int.bit_count,sets))==9 and all(x in sets for x in N)
eight=[x for x in sets if x.bit_count()==8];nine=[x for x in sets if x.bit_count()==9];opts={x for x in sets if all(x&t for t in nine)}
g=ig.Graph(n,[(i,j) for i,j in combinations(range(n),2) if N[i]>>j&1]);group=g.get_automorphisms_vf2();print('automorphisms',len(group),'legal profiles',len(opts));todo=opts.copy();stats=Counter();reps=[]
ordered=sorted(opts);full=(1<<len(opts))-1
columns=[int.from_bytes(bytes(sum(((p>>i)&1)<<b for b,p in enumerate(ordered[j:j+8])) for j in range(0,len(ordered),8)),'little') for i in range(n)]
def hits(s):
    ans=0
    while s:b=s&-s;s-=b;ans|=columns[b.bit_length()-1]
    return ans
hit8=[(t,hits(t)) for t in eight];witness=None
records=[]
for p in ordered:
    if p not in todo:continue
    orb={sum(1<<perm[i] for i in range(n) if p>>i&1) for perm in group};assert orb<=todo;todo-=orb
    rm=full^hits(p);bm=full
    for t,h in hit8:
        if not t&p:
            bm&=h
            if not bm:break
    red=rm.bit_count();blue=bm.bit_count();twin=p in N
    if witness is None and (rm or bm):
        m=rm or bm;q=ordered[(m&-m).bit_length()-1];r=q|((1<<n) if rm else 0);A=N.copy()
        for border in (p,r):A=[x|((border>>i&1)<<len(A)) for i,x in enumerate(A)]+[border]
        ss=layers(A);assert all(x in ss for x in A) and max(map(int.bit_count,ss))==9;witness=(p,r);print('verified 38: two border masks',witness,flush=True)
    stats[twin,red,blue]+=len(orb);reps.append((twin,len(orb),p.bit_count(),red,blue));records.append((p,*reps[-1]))
assert not todo
from pathlib import Path
Path(__file__).with_suffix('.tsv').write_text('mask\ttwin\torbit_size\tdegree\tred_next\tblue_next\n'+''.join('\t'.join(map(str,row))+'\n' for row in records))
print('orbits',len(reps),'by (twin,extendible)',Counter((t,bool(r+b)) for t,_,_,r,b in reps));print('labelled by (twin,extendible)',{(t,ext):sum(w for (u,r,b),w in stats.items() if u==t and bool(r+b)==ext) for t in (True,False) for ext in (True,False)});print('max next choices',max(r+b for _,_,_,r,b in reps))
