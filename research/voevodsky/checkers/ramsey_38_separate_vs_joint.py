"""Fixed prior pools. At every live prefix compare three next-move filters against actual joint continuation: local support of the newest middle edge, separate existence (possibly distinct cycles), and a sufficient overlap bound using counts alone. Count prefix+move instances, not independent graphs. Only consider candidate moves completable to an uncolored-in-the-strips alternating blue middle cycle."""
from itertools import permutations
from collections import Counter,defaultdict
from ramsey_38_joint_annuli import load,zipone,bits,red,boundaries,D
import json
out=[]
for r,d in zip(load('ramsey_38_joint_frontier'),load('ramsey_38_correction_continuation')):
    I,Z,U=r['ring'],d['Z'],sorted(r['last']);W=sorted(set(r['middle'])-set(Z));O=[[U[0],*t] for t in permutations(U[1:]) if t[0]<t[-1] and bits([U[0],*t]) is not None];stats=defaultdict(Counter)
    for M in boundaries(Z,W):
        a=int(bool(zipone(I,M)));b=int(any(zipone(M,L) for L in O));
        for seq in (M,[M[0],*M[:0:-1]]):
            for k in range(2,len(seq)+1):
                s=stats[tuple(seq[:k])];s.update({'all':1,'inner':a,'outer':b,'joint':a*b})
    summary=Counter();witness=None;certified=set();live=set();possible=defaultdict(list)
    for pre,s in stats.items():
        parent=pre[:-1];
        if len(pre)<3 or not stats.get(parent,{}).get('joint'):continue
        live.add(parent);x,y=pre[-2:];local=all(any(red(x,t)==red(y,t) for t in L) for L in (I,U));sep=min(s['inner'],s['outer'])>0;both=s['joint']>0;bound=s['inner']+s['outer']>s['all'];assert (not both or sep and local) and (not bound or both);summary.update(dict(tested=1,local_false=int(local and not both),separate_false=int(sep and not both),safe=int(both),count_certified=int(bound)));possible[parent].append((pre[-1],dict(s)))
        if bound:certified.add(parent)
        if sep and not both and (witness is None or len(pre)<len(witness)):witness=pre
    summary.update(live=len(live),has_count_cert=len(certified));out.append(dict(poles=r['poles'],ring=I,stats=summary,split_example=None if witness is None else dict(prefix=witness,options=possible[witness[:-1]])))
print('totals',sum((Counter(r['stats']) for r in out),Counter()));print('rings with separate false',sum(bool(r['stats']['separate_false']) for r in out));print('first split',next((r['split_example'] for r in out if r['split_example']),None));(D/'ramsey_38_separate_vs_joint.json').write_text(json.dumps(out,indent=2)+'\n')
