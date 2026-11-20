"""Construct on 22 by gluing independent ports onto a (3,6) core. Never reads a 22-vertex witness. Search maximal red neighborhoods WLOG: enlarging one to an independent set on the core cannot add any triangle since ports are mutually minus, and cannot create a minus clique."""
from itertools import combinations
from pathlib import Path
from functools import lru_cache
import gzip,json
H=Path(__file__).resolve().parents[1];D=H.parent/'chatgpt/ramsey';U=lambda n:(1<<n)-1

def solve(g):
 n=ord(g[0])-63;p=21-n;bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);E={(i,j) for j in range(n) for i in range(j) if bits[j*(j-1)//2+i]=='1'};adj=[0]*n
 for i,j in E:adj[i]|=1<<j;adj[j]|=1<<i
 assert not any(adj[i]&adj[j] for i,j in E)
 def ind(avail,s):
    yield s
    while avail:
        v=avail&-avail;avail-=v;yield from ind(avail&~adj[v.bit_length()-1],s|v)
 sets=list(ind(U(n),0));assert max(x.bit_count() for x in sets)<=5
 maximal=[s for s in sets if all(s&(adj[i]|1<<i) for i in range(n))]
 # For each t ports the complement of the union of their neighborhoods cannot contain a minus (7-t)-clique.
 @lru_cache(None)
 def ok(union,t):return not any(s&union==0 for s in bysize.get(7-t,[]))
 bysize={k:[s for s in sets if s.bit_count()==k] for k in range(3,7)}
 if p>=5:bysize[2]=[s for s in sets if s.bit_count()==2]
 def visit(chosen,start):
    if len(chosen)==p:return chosen
    for j in range(start,len(maximal)):
        s=maximal[j];valid=True
        for k in range(1,len(chosen)+1):
            for subset in combinations(chosen,k):
                union=s
                for x in subset:union|=x
                if not ok(union,k+1):valid=False;break
            if not valid:break
        if valid:
            hit=visit(chosen+[s],j)
            if hit:return hit
 rows=visit([],0)
 if rows is None:return None
 # label root 0, ports 1..p, core p+1..21; independent direct verification.
 plus={(i+p+1,j+p+1) for i,j in E}|{(0,i+1) for i in range(p)}|{(i+1,j+p+1) for i,s in enumerate(rows) for j in range(n) if s>>j&1}
 for k,red in [(3,True),(7,False)]:assert not any(all((e in plus)==red for e in combinations(t,2)) for t in combinations(range(22),k))
 return dict(root=0,ports=list(range(1,p+1)),core=list(range(p+1,22)),cross_plus=[[j+p+1 for j in range(n) if s>>j&1] for s in rows],plus_edges=sorted(plus))

def main():
 tested={};hit=None
 for n in (17,16):
    records=(D/'pauli-realization-catalogues/r36_17.g6').read_text().splitlines() if n==17 else gzip.decompress((D/'r36_16.g6.gz').read_bytes()).decode().splitlines()
    for i,g in enumerate(records):
        tested[n]=i+1;hit=solve(g)
        if hit:break
    if hit:break
 assert hit is not None;out=dict(tested=tested,core_g6=g,core_index_zero_based=i,witness=hit);print(tested,hit['cross_plus']);(H/'results/ramsey_37_root_glue.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
