"""Exact joint search on the same patched-square cores, with no square or old support fixed."""
from itertools import combinations
from collections import Counter
import gzip,json
from ramsey_retention_slice import CAT,D,decode,check


def find(a,on_panel=None):
    I=[0];n=len(a)
    for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v]);
    S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];M={}
    for k in (7,6,5,4):
        qs=[q for q in I if q.bit_count()==k];full=(1<<len(qs))-1;by=[sum(1<<j for j,q in enumerate(qs) if q>>i&1) for i in range(n)];M[k]=[]
        for s in S:
            miss=full
            for i in range(n):
                if s>>i&1:miss &= ~by[i]
            M[k].append(miss)
    assert all(M[7]);N=[sum(1<<j for j in range(i+1,len(S)) if not M[7][i]&M[7][j]) for i in range(len(S))];counts=Counter();example=None
    def search(prefix,options):
        nonlocal example
        while options.bit_count()>=5-len(prefix):
            b=options&-options;options^=b;i=b.bit_length()-1;p=prefix+(i,)
            if len(p)<5:search(p,options&N[i]);continue
            counts['seven']+=1
            for k in (6,5,4):
                for group in combinations(p,9-k):
                    m=M[k][group[0]]
                    for j in group[1:]:m&=M[k][j]
                    if m:break
                else:counts[str(k)]+=1;continue
                break
            else:
                if on_panel is not None:on_panel([S[j] for j in p])
                if example is None:example=[S[j] for j in p]
    search((),(1<<len(S))-1)
    if example:
        g=a[:]+[0]*6
        for i,s in enumerate(example,n):
            g[i]=s|(1<<(n+5));g[-1]|=1<<i
            for j in range(n):g[j]|=int(bool(s>>j&1))<<i
        assert check(g,(1<<(n+6))-1,3,9)
    return dict(maximal_supports=len(S),counts=counts,example=example)

def audit():
    prior=json.loads((D.parent/'ramsey_square_fifth_from_coverage.json').read_text());ids={r['record'] for r in prior};out=[]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:
        for idx,line in enumerate(f):
            if idx in ids:out.append(dict(record=idx,**find(decode(line.strip()))))
    print('distinct cores',len(out), 'stages',[(k,sum(bool(r['counts'].get(k)) for r in out),sum(r['counts'].get(k,0) for r in out)) for k in ('seven','6','5','4')], 'first',next((r for r in out if r['example']),None));(D.parent/'ramsey_intact27_joint_five.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
