"""Test a fixed observation order, not selected edge subsets: reveal the closing neighbor, then the preceding return-path vertices. Audit all live prefixes, separately against the arbitrary-edge hard set, using explicitly enumerated cycles. Incidence for each side counted independently. Minimize return depth over candidate next moves. Stop before revealing any part of the supplied forward prefix or proposed move."""
import json
from collections import Counter,defaultdict
from itertools import permutations
from ramsey_38_joint_annuli import D,load,zipone,boundaries
out=[];allhist=Counter();hardhist=Counter()
for r,desc,old in zip(load('ramsey_38_joint_frontier'),load('ramsey_38_correction_continuation'),load('ramsey_38_edge_conditioned_counts')):
    I=r['ring'];Z=desc['Z'];U=sorted(r['last']);W=sorted(set(r['middle'])-set(Z));pool=defaultdict(list);hard={tuple(q['prefix']) for q in old['hard']}
    for M in boundaries(Z,W):
        a=bool(zipone(I,M));b=any(zipone(M,[U[0],*t]) for t in permutations(U[1:]) if t[0]<t[-1]);
        for seq in (M,[M[0],*M[:0:-1]]):
            for k in range(2,len(seq)):pool[tuple(seq[:k])].append((seq[k],seq[k+1:][::-1],a,b))
    records=[]
    for prefix,rows in pool.items():
        if not any(a and b for _,_,a,b in rows):continue
        for depth in range(len(rows[0][1])+1):
            bins=defaultdict(lambda:[0,0,0]);
            for v,suffix,a,b in rows:
                key=(v,tuple(suffix[:depth]));counts=bins[key];counts[0]+=1;counts[1]+=a;counts[2]+=b
            wins=[(v,tail,*counts) for (v,tail),counts in bins.items() if sum(counts[1:])>counts[0]]
            if wins:break
        assert wins and (depth>0)==(prefix in hard);allhist[depth]+=1
        if depth:
            hardhist[depth]+=1;v,tail,t,a,b=min(wins)
            rs=[x for x in rows if x[0]==v and tuple(x[1][:depth-1])==tail[:-1]]
            records.append(dict(prefix=prefix,next=v,reverse_prefix=tail,counts=[t,a,b],parent_counts=[len(rs),sum(x[2] for x in rs),sum(x[3] for x in rs)]))
    out.append(dict(poles=r['poles'],ring=I,hard=records))
print('all',allhist,'hard',hardhist);print(max((z for o in out for z in o['hard']),key=lambda z:len(z['reverse_prefix'])));(D/'ramsey_38_return_port.json').write_text(json.dumps(dict(depth_histogram=allhist,rings=out),indent=2)+'\n')
