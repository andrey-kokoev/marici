"""Pre-insertion criterion; independent verification of every child."""
from ramsey_retention_slice import check,D
from itertools import combinations,product
from collections import Counter
from hashlib import sha256
import json

def graph(n,ss,col):
    a=[0]*(n+len(ss));es=[(i,i+1) for i in range(n-1)]+[(j,n+i) for i,s in enumerate(ss) for j in s]+[(n+i,n+j) for b,(i,j) in enumerate(combinations(range(len(ss)),2)) if col>>b&1];
    for i,j in es:a[i]|=1<<j;a[j]|=1<<i
    return a

def trial(n,ss,col,gap):
    a=graph(n,ss,col);V=range(len(a));assert check(a,(1<<len(a))-1,3,7);f=[v for v in (gap-1,gap) if 0<=v<n];other=set(V)-set(f)
    def blue(s):return all(not(a[i]>>j&1) for i,j in combinations(s,2))
    X=next((s for s in combinations(sorted(other),6) if blue(s)),None);E=None
    if len(f)==2:E=next((s for s in combinations(sorted(v for v in other if all(not(a[v]>>j&1) for j in f)),5) if blue(s)),None)
    g=graph(n+1,[tuple(j+(j>=gap) for j in s) for s in ss],col);assert check(g,(1<<len(g))-1,3,7)==(X is None and E is None);return ('X' if X else '')+('E' if E else '') or 'pass',dict(path_size=n,port_supports=ss,port_edge_bits=col,gap=gap,blue_six=X,common_blue_five=E)

def main():
    rows=[t for t in combinations(range(6),3) if min(t[1]-t[0],t[2]-t[1])>=2];stats=Counter();samples={}
    for ss in product(rows,repeat=3):
        for col in range(8):
            if not check(graph(6,ss,col),511,3,7):continue
            for gap in range(7):
                r,v=trial(6,ss,col,gap);stats[r]+=1;samples.setdefault(r,v)
    controls={}
    for expected,ss in [('E',[()]*5),('X',[(0,)]*3+[(1,)]*3)]:
        r,v=trial(2,ss,0,1);assert r==expected;controls[r]=v
    print(stats,samples,controls);p=D.parent/'ramsey_forward_path_insertion_protocol.md';out=dict(protocol_sha=sha256(p.read_bytes()).hexdigest(),counts=stats,examples=samples,independent_controls=controls);dest=D.parent/'ramsey_forward_path_insertion.json';s=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':main()
