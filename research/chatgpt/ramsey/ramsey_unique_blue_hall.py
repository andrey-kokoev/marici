"""Necessary local expansion for a unique forbidden independent 8-set B=T+missing ports. Singleton outsiders require >=2 red neighbours in B. Enforce triangle-free maximal missing supports via SAT; other port, when present, must hit T twice. Compare to exact singleton-violation labels."""
from ramsey_capacity_transfer_78 import D,json,inds,decode,bits
from pysat.solvers import Solver
from itertools import combinations
from collections import Counter

def run():
    src=json.loads((D/'ramsey_intrinsic_attachment_basis.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in src:
        G=decode(lines[r['parent']-1]);V=[i for i in range(22) if i!=r['deleted']];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];n=len(H);I=inds(H);truth=set(r['forced']);h=Counter();example=None
        for t in I:
            k=t.bit_count()
            if k not in (4,5):continue
            m=8-k;ext=[v for v in range(n) if not (1<<v|H[v])&t];odd=False
            if m==3:odd=any(H[v]>>w&1 for v,w in combinations(ext,2))
            else:
                colors={}
                for v in ext:
                    if v in colors:continue
                    colors[v]=0;st=[v]
                    while st:
                        x=st.pop()
                        for y in ext:
                            if H[x]>>y&1:
                                if y not in colors:colors[y]=1-colors[x];st.append(y)
                                elif colors[y]==colors[x]:odd=True
            if odd:tag='extender obstruction'
            else:
                # Each of m independent supports avoids t and dominates each vertex of t;
                # it can then be enlarged maximally without touching t.
                C=[]
                for j in range(m):
                    lit=lambda v:1+j*n+v
                    C.extend([[lit(v) for v in bits(H[x]&~t)] for x in bits(t)])
                    C.extend([[-lit(x),-lit(y)] for x in range(n) if not t>>x&1 for y in bits(H[x]&~t) if x<y])
                for v in range(n):
                    if t>>v&1:continue
                    need=2-(H[v]&t).bit_count()
                    if need>0:C.extend(list(g) for g in combinations([1+j*n+v for j in range(m)],m-need+1))
                with Solver(name='g3',bootstrap_with=C) as sat:ok=sat.solve()
                tag='passes singleton' if ok else 'singleton obstruction'
            yes=t in truth;assert not yes or tag=='passes singleton';h[k,tag,yes]+=1
            if example is None and tag=='passes singleton' and not yes:example=t
        out.append(dict(parent=r['parent'],counts={str(key):v for key,v in h.items()},example=example))
    return out
if __name__=='__main__':
    z=run();print(sum((Counter(r['counts']) for r in z),Counter()));(D/'ramsey_unique_blue_hall.json').write_text(json.dumps(z)+'\n')
