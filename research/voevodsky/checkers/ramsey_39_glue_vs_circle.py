"""Contrast fixed rooted 1+7+27 gluing with an offset-free circulant constructor on 35 vertices."""
import json,sys
from pathlib import Path
from time import monotonic
H=Path(__file__).resolve().parents[1];sys.path.insert(0,str(H.parent/'chatgpt/ramsey'));from ramsey_39_cyclic_constructor import search,verify

def rooted(E):
    n=27;P=[0]*n
    for a,b in E:P[a]|=1<<b;P[b]|=1<<a
    sets=[]
    def ind(s,v):
        sets.append(s)
        while v:
            x=v&-v;v-=x;ind(s|x,v&~P[x.bit_length()-1])
    ind(0,(1<<n)-1);assert max(map(int.bit_count,sets))==7
    rows=[s for s in sets if all(s&(1<<v|P[v]) for v in range(n))];fs=[s for s in sets if s.bit_count()==7];post=[sum(1<<i for i,s in enumerate(fs) if s>>v&1) for v in range(n)];D=[]
    for s in rows:
        hit=0
        for v in range(n):
            if s>>v&1:hit|=post[v]
        D.append(((1<<len(fs))-1)^hit)
    assert all(D) # repeated neighborhoods cannot coexist
    G=[sum(1<<j for j in range(i+1,len(D)) if not D[i]&D[j]) for i in range(len(D))];best=0
    def visit(k,m):
        nonlocal best
        best=max(best,k)
        while k+m.bit_count()>best:
            x=m&-m;m-=x;visit(k+1,m&G[x.bit_length()-1])
    visit(0,(1<<len(G))-1);return dict(maximal_port_neighborhoods=len(rows),minus_sevens=len(fs),max_pairwise_compatible=best)

def main():
    r=rooted(json.loads((H/'results/ramsey_38_root_glue.json').read_text())['witness']['plus_edges']);print(r,flush=True);n=35;d=search(n,monotonic()+60);assert d is not None and verify(n,d)==8
    ds=[i for i in range(1,18) if d>>i&1];E=[[a,b] for a in range(n) for b in range(a+1,n) if min(b-a,n-b+a) in ds];assert not any(min((a-b)%n,(b-a)%n) in ds for a in range(1,n) for b in range(a+1,n) if d>>a&1 and d>>b&1);out=dict(rooted=r,circle_distances=ds,plus_edges=E,maximum_minus_clique=8);print(ds,len(E));(H/'results/ramsey_39_glue_vs_circle.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
