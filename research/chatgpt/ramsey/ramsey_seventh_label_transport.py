"""Predeclared stationary-chart hypothesis: add one fixed label to the six square edges. Translations flip an even number of the three opposite-edge pairs. Axis swap exchanges two pair blocks, fixing both members of the diagonal block. Test signature multiset only, not graph automorphisms."""
from itertools import combinations,permutations,product
from collections import Counter
from pathlib import Path
import gzip,json,argparse
D=Path(__file__).parent

def graph(line):
    n=line[0]-63;A=[0]*n;p=0
    for j in range(n):
        for i in range(j):
            if (line[1+p//6]-63)>>(5-p%6)&1:A[i]|=1<<j;A[j]|=1<<i
            p+=1
    return A

def match(V,fp):
    if not V:yield [];return
    a,*R=V
    for b in R:
        if fp[a]==fp[b]:
            for other in match([c for c in R if c!=b],fp):yield [(a,b)]+other

def test(A):
    C=Counter();example=None
    for i,r in enumerate(A):
        if r.bit_count()!=7:continue
        C['charts']+=1;V=[j for j in range(27) if r>>j&1];S=Counter(sum(1<<a for a,j in enumerate(V) if x>>j&1) for h,x in enumerate(A) if h!=i and not r>>h&1)
        fp=[tuple(sum(n for s,n in S.items() if s>>a&1 and s.bit_count()==k) for k in range(1,8)) for a in range(7)];
        if sum(n%2 for n in Counter(fp).values())!=1:continue
        C['fingerprint']+=1
        def inv(swaps):
            for s,n in S.items():
                t=s
                for a,b in swaps:
                    if ((s>>a)^(s>>b))&1:t^=(1<<a)|(1<<b)
                if S[t]!=n:return False
            return True
        tr=fr=False
        for f in range(7):
            for P in match([x for x in range(7) if x!=f],fp):
                if not all(inv([P[0],p]) for p in P[1:]):continue
                tr=True
                for a,b in combinations(P,2):
                    for c in (b,b[::-1]):
                        if inv(list(zip(a,c))):
                            fr=True;example=dict(root=i,labels=V,fixed=V[f],pairs=[[V[x],V[y]] for x,y in P],axis_swap=[[V[x],V[y]] for x,y in zip(a,c)],signature_counts=S);break
                    if fr:break
                if fr:break
            if fr:break
        C['translations']+=tr;C['frame']+=fr
    return C,example
if __name__=='__main__':
    from verify_ramsey_pure_forks import replay
    args=argparse.ArgumentParser();args.add_argument('--limit',type=int,default=1000);limit=args.parse_args().limit;A=replay(json.loads((D/'ramsey_pure_short_fork.json').read_text()))[0];a,e=test(A);print('generated',a,flush=True);total=Counter();ex=None;graphs=0
    with gzip.open(D/'pauli-realization-catalogues/r38_27.g6.gz','rb') as stream:
        for idx,line in enumerate(stream,1):
            if idx>limit:break
            c,e=test(graph(line));total.update(c);graphs+=1
            if e and ex is None:ex=dict(record=idx,**e)
    out=dict(generated=dict(a),catalogue_prefix=graphs,counts=dict(total),first_example=ex);print(out);(D/'ramsey_seventh_label_transport.json').write_text(json.dumps(out)+'\n')
