"""uv run --with igraph --with numpy python ... . Fixed test: first violated subset, sizes 1..4.
Holdout cohort: one valid delete/add from either of the two source H, E fixed to each of the 17 source assignments. Exclude isomorphs of previously tested residuals. No score enters generation.
"""
import json,itertools,numpy as np
from collections import Counter
from ramsey310_matching_scope import key,D
from ramsey310_matching_sides import decode,instances as additions,F,sets,bits
import ramsey310_s3_local_transfer as prev
from ramsey310_matching_joint import joint

def eligible(A,E):
    if any(prev.independent(A,F&~(a|b),7) for side in (E[:3],E[3:]) for j,a in enumerate(side) for b in side[:j]):return
    if any(prev.independent(A,F&~(a|b|c),6) for a,b,c in (E[:3],E[3:])):return
    d=[9-a.bit_count()-sum(r>>v&1 for r in E) for v,a in enumerate(A)]
    if min(d)<1 or max(d)>6 or any(d[i]+d[j]>6 for i,a in enumerate(A) for j in bits(a)):return
    sing=sum(1<<v for v,x in enumerate(d) if x==1);C=list(sets(A,F,7))
    for a,b,c in itertools.product(*zip(E[:3],E[3:])):
        z=sing&~(a|b|c)
        if z.bit_count()>6:return
        C=[s for s in C if (s&z).bit_count()<=1]
    for k in (6,7):
        for t in sets(A,F,k):
            limit=6-k+sum(bool(t&a and t&b) for a,b in zip(E[:3],E[3:]))
            if limit<0:return
            if limit==0:C=[s for s in C if s&t]
    if len(C)>=6 and all(sum(s>>v&1 for s in C)>=x for v,x in enumerate(d)):return d,C

def cut(d,C):
    R=np.array([[s>>v&1 for s in C] for v in range(26)],dtype=np.int8);d=np.array(d)
    for k in range(1,5):
        g=itertools.combinations(range(26),k)
        while batch:=list(itertools.islice(g,512)):
            I=np.array(batch);B=np.sort(R[I].sum(1,dtype=np.int8),axis=1);low=B[:,:6].sum(1);high=B[:,-6:].sum(1);need=d[I].sum(1);bad=np.flatnonzero((need<low)|(need>high))
            if len(bad):j=bad[0];return dict(vertices=batch[j],lo=int(low[j]),hi=int(high[j]),need=int(need[j]))

def main():
    old=json.loads((D/'ramsey310_matching_degree3_types.json').read_text());base=old[0];sources=[]
    for r in json.loads((D/'ramsey310_s3_local_transfer_r10.json').read_text())['uncut']:
        A=base.copy()
        for i,j,x,y in r['path']:A[i]^=1<<j;A[j]^=1<<i;A[x]|=1<<y;A[y]|=1<<x
        sources.append(A)
    known={key(A) for A in old+sources};known.add(key(json.loads((D/'ramsey310_matching_scope.json').read_text())['outside']['rows']))
    for i,l in enumerate((D/'ramsey38_26_e73_hog.g6').read_bytes().splitlines(),1):
        g=additions(decode(l));known.add(key(next(g)))
        if i in (2,5):known.add(key(next(g)))
    seen=set();types=set();cases=[];count=Counter()
    for i,A in enumerate(sources):
        for j,r in enumerate(json.loads((D/f'ramsey310_s3_all_ports_{i}_replay.json').read_text())):
            E=prev.E=tuple(r['E']);
            for Z,edit in prev.neighbors(A):
                zkey=key(Z)
                if zkey in known or (Z,E) in seen:continue
                seen.add((Z,E));types.add(zkey);x=eligible(Z,E)
                if x is None:continue
                d,C=x;cert=cut(d,C);exact=joint(Z,E);count['eligible']+=1;count['cut']+=int(cert is not None);cases.append(dict(source=[i,j],edit=edit,key=zkey.hex(),rows=len(C),cut=cert,exact=exact))
    result=dict(new_types=len(types),new_labeled_assignments=len(seen),counts=count,cases=cases);(D/'ramsey310_smallset_holdout.json').write_text(json.dumps(result));print(result)
if __name__=='__main__':main()
