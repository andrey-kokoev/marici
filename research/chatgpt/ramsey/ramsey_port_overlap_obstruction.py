"""Predict four-port extension from the incidence of tight and near-tight blue sets.
Only the independent verification stage tries pairs of future attachments."""
from pathlib import Path
from itertools import combinations_with_replacement
from collections import Counter
from ramsey_clique_power_blowup import layers

def test(line):
    n=line[0]-63;bits=''.join(f'{b-63:06b}' for b in line[1:]);A=[sum(1<<j for j in range(n) if i!=j and bits[max(i,j)*(max(i,j)-1)//2+min(i,j)]=='1') for i in range(n)];F=layers(A);assert max(map(int.bit_count,F))==5
    M=[t for t in F if all(t>>i&1 or A[i]&t for i in range(n))];allm=(1<<len(M))-1
    tests=[(s,s.bit_count(),sum(1<<i for i,t in enumerate(M) if t&s)) for s in F if s.bit_count()>=3];five=[s for s,k,_ in tests if k==5];stats=Counter();fp=0;actual=0
    for a,b in combinations_with_replacement(F,2):
        if any(not(s&a or s&b) for s in five):continue
        allowed=allm;near=[]
        for s,k,h in tests:
            slack=6-k-int(not(s&a))-int(not(s&b))
            if slack==0:allowed &=h
            elif slack==1:near.append(h)
        obligations=set(h&allowed for h in near);obligations.discard(allowed) if allowed else None
        if not allowed:reason='no tight transversal'
        elif 0 in obligations:reason='unreachable near-tight set'
        else:
            # Distinct obligations with disjoint support must be served by opposite future ports.
            vs=sorted(obligations,key=int.bit_count);vs=[x for i,x in enumerate(vs) if not any(y&x==y for y in vs[:i])];color={};ok=True
            for x in vs:
                if x in color:continue
                color[x]=0;stack=[x]
                while stack and ok:
                    t=stack.pop()
                    for y in vs:
                        if y&t:continue
                        if y not in color:color[y]=1-color[t];stack.append(y)
                        elif color[y]==color[t]:ok=False;break
            reason='passes' if ok else 'odd conflict cycle'
        stats[reason]+=1
        # Ground truth: two maximal red neighborhoods must cover every near-tight obligation.
        opts=[1<<i for i in range(len(M)) if allowed>>i&1];truth=any(all((i|j)&h for h in near) for i,j in combinations_with_replacement(opts,2));actual+=truth
        assert not truth or reason=='passes';fp+=int(not truth and reason=='passes')
    return len(M),dict(stats),actual,fp
if __name__=='__main__':
    for i,line in enumerate((Path(__file__).with_name('pauli-realization-catalogues')/'r36_17.g6').read_bytes().splitlines(),1):print(i,*test(line),flush=True)
