"""Forward 33 -> 34 test with five installed maximal rows retained, one deletion and two new ports. Combine degree deficits with exact load constraints."""
from ramsey_intact27_joint_five import CAT,D,decode,find,check
from itertools import combinations_with_replacement
from collections import Counter
import gzip,json

def audit():
    prior=json.loads((D.parent/'ramsey_intact27_pack_layers.json').read_text());ids={i for k in ('86','87') for i in prior[k]['seven_candidates']};stats=Counter();cores=[];first={};F=(1<<27)-1
    for idx,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')):
        if idx not in ids:continue
        a=decode(l.strip());panels=[];find(a,panels.append)
        if not panels:continue
        cores.append(idx);I=[0]
        for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v]);
        S=[s for s in I if all(s&(n|1<<i) for i,n in enumerate(a))]
        for rows in panels:
            stats['panels']+=1;zs=[]
            for z in range(27):
                stats['deletions']+=1;p=F^(1<<z);d=[7-(a[i]&p).bit_count()-sum(s>>i&1 for s in rows) if i!=z else 0 for i in range(27)];both=sum(1<<i for i,v in enumerate(d) if v==2);one=sum(1<<i for i,v in enumerate(d) if v>=1)
                if max(d)>2 or any((s&p).bit_count()<6 for s in rows) or any(both>>i&1 and a[i]&both for i in range(27)):continue
                stats['local_degree_pass']+=1;opts={s&p for s in S if both&s==both and (s&p).bit_count()>=6};zs.append((z,p,one,opts))
            if not zs:continue
            loads={k:[] for k in (7,8)}
            for q in I:
                k=q.bit_count()+sum(not q&s for s in rows)
                if k in loads:loads[k].append(q)
            for z,p,one,opts in zs:
                opts=[s for s in opts if all(q&s or q>>z&1 for q in loads[8])];stats['individual_pass']+=bool(opts)
                near=[q for q in loads[7] if not q>>z&1];degree_pairs=0;won=False
                for s,t in combinations_with_replacement(opts,2):
                    if one&~(s|t):continue
                    degree_pairs+=1
                    if all(q&(s|t) for q in near):
                        g=a[:]+[0]*8
                        for k,r in enumerate(rows+[s,t],27):
                            g[k]=r|(1<<34);g[-1]|=1<<k
                            for j in range(27):g[j]|=int(bool(r>>j&1))<<k
                        assert check(g,((1<<35)-1)^(1<<z),3,9);first.setdefault('win',dict(record=idx,delete=z,old=rows,new=[s,t]));won=True;break
                stats['degree_pair_and_load8_pass']+=bool(degree_pairs);stats['net_gain']+=won
    out=dict(layers=[86,87],records=cores,counts=stats,examples=first);print(out);(D.parent/'ramsey_delete_one_grow_two.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
