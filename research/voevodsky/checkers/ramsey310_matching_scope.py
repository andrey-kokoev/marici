"""uv run --with igraph. Canonical census of two-edge additions and a scope countertest."""
import igraph as ig,random,hashlib,json
from collections import Counter
from ramsey310_matching_sides import decode,instances,bits,F,Path
from ramsey310_six_set_parent_test import independent
D=Path(__file__).resolve().parents[1]/'results'

def edges(A):return [(i,j) for j,m in enumerate(A) for i in bits(m&((1<<j)-1))]
def key(A):
    g=ig.Graph(n=26,edges=edges(A));g=g.permute_vertices(g.canonical_permutation());return sum(1<<(j*(j-1)//2+i) for i,j in g.get_edgelist()).to_bytes(41,'little')
def toggle(A,i,j):A[i]^=1<<j;A[j]^=1<<i

def search(A,known):
    rng=random.Random(310);start=A.copy();moves=[]
    for step in range(3000):
        adds=[(i,j) for j in range(26) for i in range(j) if not(A[i]>>j&1 or A[i]&A[j])];rng.shuffle(adds)
        for i,j in adds:
            toggle(A,i,j);cands=edges(A);rng.shuffle(cands)
            for x,y in cands:
                if (x,y)!=(i,j) and not independent(A,F&~(A[x]|A[y]),6):break
            else:toggle(A,i,j);continue
            toggle(A,x,y);moves.append([i,j,x,y]);break
        else:return None
        if key(A) not in known:
            assert len(edges(A))==75 and not independent(A,F,8) and all(not A[i]&A[j] for i,j in edges(A))
            return dict(start=start,moves=moves,rows=A)
    return None

if __name__=='__main__':
    source=(D/'ramsey38_26_e73_hog.g6').read_bytes();assert hashlib.sha256(source).hexdigest()=='9a904566a969ef257db9b28719c35f84a86aa63e9a1c56a7691aa3807d35b214'
    freq=Counter();rep={};first=None
    for n,line in enumerate(source.splitlines(),1):
        for j,A in enumerate(instances(decode(line))):
            k=key(A);rep.setdefault(k,(n,j));freq[k]+=1
            if first is None:first=A.copy()
    full=dict(labeled=sum(freq.values()),classes=len(freq),multiplicities=dict(sorted(Counter(freq.values()).items())),first_multiplicity=freq[key(first)],outside=search(first.copy(),freq),igraph=ig.__version__)
    print(json.dumps(full));(D/'ramsey310_matching_representatives.tsv').write_text('parent\taddition_index\tmultiplicity\tcanonical_key\n'+''.join(f'{rep[k][0]}\t{rep[k][1]}\t{freq[k]}\t{k.hex()}\n' for k in sorted(freq)))
