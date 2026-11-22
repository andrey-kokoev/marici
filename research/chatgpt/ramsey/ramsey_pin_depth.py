"""See protocol. Detect chart collisions by automorphisms of the border language, not necessarily of the old graph."""
from itertools import combinations
from pathlib import Path
import networkx as nx,json
D=Path(__file__).parent
def sets(h):
    I=[0]
    for i,r in enumerate(h):I.extend([s|1<<i for s in I if not s&r])
    return I
def borders(h):
    I=sets(h);T=[s for s in I if s.bit_count()==6];return {s for s in I if all(s&t for t in T)},[s for s in I if s.bit_count()==5]
def check(h):return dict(alpha=max(map(int.bit_count,sets(h))),triangles=sum((h[i]&h[j]).bit_count() for i,j in combinations(range(len(h)),2) if h[i]>>j&1)//3)
def add(h,a,b):return [v|((a>>i&1)<<len(h))|((b>>i&1)<<(len(h)+1)) for i,v in enumerate(h)]+[a,b]
def labels(s):return [i for i in range(s.bit_length()) if s>>i&1]
def run():
    data=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();tries=0
    for n in (20,19,18,17,16):
        for rec,line in enumerate(data,1):
            g=nx.from_graph6_bytes(line);h=[sum(1<<j for j in g[i] if j<n) for i in range(n)];B,T=borders(h);tries+=1
            for i,j in combinations(range(n),2):
                flip=(1<<i)|(1<<j);swap=lambda s:s^flip if (s>>i^s>>j)&1 else s
                if not (h[i]^h[j])&~flip or any(swap(s) not in B for s in B):continue
                diff={s for s in T if swap(s) not in T};
                if not diff:continue
                for a,b in combinations(sorted(B),2):
                    u=a|b;f=next((t for t in diff if not t&u),0)
                    if not f or any(t&swap(u)==0 for t in T):continue
                    h2=[swap(h[j if k==i else i if k==j else k]) for k in range(n)];assert B==borders(h2)[0];old=[check(h),check(h2)];ext=[check(add(v,a,b)) for v in (h,h2)];assert all(z['alpha']<=6 and not z['triangles'] for z in old) and ext==[dict(alpha=7,triangles=0),dict(alpha=6,triangles=0)];return dict(record=rec,n=n,examined=tries,swap=[i,j],borders=len(B),red_supports=[labels(a),labels(b)],missed_five=labels(f),old=old,extended=ext,old_edges=[[x,y] for x,y in combinations(range(n),2) if h[x]>>y&1])
    raise ValueError('no collision')
if __name__=='__main__':
    r=run();print({k:v for k,v in r.items() if k!='old_edges'});(D/'ramsey_pin_depth.json').write_text(json.dumps(r,indent=2)+'\n')
