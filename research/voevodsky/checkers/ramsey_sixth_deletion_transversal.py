"""Generate the least predecessor deletions that preserve five old rows and enable a sixth.
Deletion sets are tried against an index of blockers, not against successor colorings.
"""
from ramsey_intact27_joint_five import find,CAT,D,check,decode
from itertools import combinations,islice
from collections import Counter
import gzip,json


def audit():
    idx=42702
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    panels=[];find(a,panels.append);assert len(panels)==6;V=(1<<27)-1;I=[0]
    for i,m in enumerate(a):I.extend([q|1<<i for q in I if not q&m]);
    choices=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];records=[]
    for rows in panels:
        tight=[q for q in I if q.bit_count()+sum(not q&s for s in rows)==8];allq=(1<<len(tight))-1;by=[sum(1<<j for j,q in enumerate(tight) if q>>i&1) for i in range(27)];bad=[]
        for s in choices:
            m=allq
            for i in range(27):
                if s>>i&1:m &= ~by[i]
            assert m;bad.append(m)
        # A deletion set Z and sixth support S work exactly when Z|S meets every tight Q.
        hist=[];ex=None;singleton_choices=[]
        for n in range(5):
            successes=0;sets=0
            for zs in combinations(range(27),n):
                q=allq
                for i in zs:q &= ~by[i]
                compatible=[j for j,m in enumerate(bad) if not q&m];successes+=len(compatible);sets+=bool(compatible)
                if compatible and n==1:
                    z=zs[0]
                    for h in compatible:singleton_choices.append(dict(vertex=z,own_star=choices[h]==a[z],prior_port_contacts=[i for i,r in enumerate(rows) if r>>z&1]))
                if compatible and ex is None:
                    j=compatible[0];s=choices[j];obs=[x for h,x in enumerate(tight) if bad[j]>>h&1];g=a[:]+[0]*7
                    for k,t in enumerate(rows+[s],27):
                        g[k]=t|1<<33;g[-1]|=1<<k
                        for i in range(27):g[i]|=int(bool(t>>i&1))<<k
                    assert check(g,((1<<34)-1)^sum(1<<i for i in zs),3,9);ex=dict(delete=zs,sixth=[i for i in range(27) if s>>i&1],blockers=len(obs),common_to_blockers=[i for i in range(27) if all(x>>i&1 for x in obs)])
            hist.append([n,sets,successes]);
            if successes:break
        assert ex;records.append(dict(rows=rows,tight=len(tight),trials=hist,example=ex,singleton_choices=singleton_choices))
    print([(r['trials'][-1],r['example']) for r in records]);(D.parent/'ramsey_sixth_deletion_transversal.json').write_text(json.dumps(dict(record=idx,maximal_sixth_options=len(choices),records=records),indent=2)+'\n')
if __name__=='__main__':audit()
