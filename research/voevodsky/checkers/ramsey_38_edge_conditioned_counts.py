"""On the 84 hard prefixes refine the previous inclusion-exclusion lower bound by named middle-edge incidence, then pairs of incidences. Enumerated oracle counts, not a local generator. An event is a Boolean bin on the edges of a candidate middle cycle, not the witness graph's fixed red/blue bit."""
from collections import defaultdict,Counter
from itertools import permutations,combinations,product
from ramsey_38_joint_annuli import D,load,boundaries,zipone
import json
out=[];total=Counter()
for r,desc in zip(load('ramsey_38_joint_frontier'),load('ramsey_38_correction_continuation')):
    I=r['ring'];Z=desc['Z'];U=sorted(r['last']);W=sorted(set(r['middle'])-set(Z));cycles=[];inner=outer=0;parent=defaultdict(dict);em=defaultdict(int)
    for M in boundaries(Z,W):
        bit=1<<len(cycles);cycles.append(M);inner|=bit*bool(zipone(I,M));outer|=bit*any(zipone(M,[U[0],*t]) for t in permutations(U[1:]) if t[0]<t[-1]);
        for x,y in zip(M,M[1:]+M[:1]):em[tuple(sorted((x,y)))]|=bit
        for seq in (M,[M[0],*M[:0:-1]]):
            for i in range(2,len(M)):
                opt=parent[tuple(seq[:i])];v=seq[i];opt[v]=opt.get(v,0)|bit
    def credit(bin):return (bin&inner).bit_count()+(bin&outer).bit_count()-bin.bit_count()
    def test(opts):
        for v,mask in opts.items():
            ls=[(e,m&mask) for e,m in em.items() if m&mask not in (0,mask)]
            for k in (1,2):
                for group in combinations(ls,k):
                    for vals in product((True,False),repeat=k):
                        b=mask
                        for (_,m),val in zip(group,vals):b&=m if val else ~m
                        if credit(b)>0:yield dict(next=v,bits=[(e,val) for (e,_),val in zip(group,vals)],T=b.bit_count(),I=(b&inner).bit_count(),O=(b&outer).bit_count());break
    hard=[]
    for p,opts in parent.items():
        if not any(b&inner&outer for b in opts.values()) or any(credit(b)>0 for b in opts.values()):continue
        cert=None
        for q in test(opts):
            if cert is None or len(q['bits'])<len(cert['bits']):cert=q
            if len(cert['bits'])==1:break
        total[len(cert['bits']) if cert else 'open']+=1;hard.append(dict(prefix=p,certificate=cert))
    out.append(dict(poles=r['poles'],ring=I,hard=hard))
assert sum(total.values())==84;print(total);print(next(x for o in out for x in o['hard']));(D/'ramsey_38_edge_conditioned_counts.json').write_text(json.dumps(out,indent=2)+'\n')
