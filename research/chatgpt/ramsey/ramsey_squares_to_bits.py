"""Build binary state/cut incidence from unlabeled adjacency ONLY. Union opposite edges of 4-cycles; integrate parity from a root. Certify isometry without a distance oracle: every unequal pair admits a move lowering Hamming distance. C6 hostile control. Inputs: Exoo deletion 35 and 37."""
from pathlib import Path
import json
from itertools import combinations
from exoo39_symbolic_relations import edges
D=Path(__file__).parent

def decode(adj):
    n=len(adj);es=sorted((i,j) for i in range(n) for j in adj[i] if i<j);parent={e:e for e in es}
    def root(e):
        while parent[e]!=e:parent[e]=parent[parent[e]];e=parent[e]
        return e
    key=lambda a,b:tuple(sorted((a,b)));squares=0
    for a in range(n):
        for b,d in combinations(adj[a],2):
            for c in adj[b]&adj[d]:
                if min(a,b,c,d)!=a or c==a:continue
                squares+=1
                for u,v in [(key(a,b),key(c,d)),(key(a,d),key(c,b))]:parent[root(u)]=root(v)
    classes=sorted({root(e) for e in es});colors={e:1<<classes.index(root(e)) for e in es};word={0:0};todo=[0];consistent=True
    while todo:
        a=todo.pop()
        for b in adj[a]:
            val=word[a]^colors[key(a,b)]
            if b not in word:word[b]=val;todo.append(b)
            elif word[b]!=val:consistent=False
    assert len(word)==n;ok=consistent and len(set(word.values()))==n and all(any((word[a]^word[b])&colors[key(a,c)] for c in adj[a]) for a in range(n) for b in range(n) if a!=b);return dict(states=n,edges=len(es),squares=squares,axes=len(classes),integrable=consistent,isometric=ok)

def graph(B):return [{j for j,t in enumerate(B) if (s^t).bit_count()==1} for s in B]
W=json.loads((D/'ramsey_exoo_chart22_words.json').read_text())['words'];h=[sum(1<<j for j in range(39) if tuple(sorted((j,i))) in edges()) for i in range(39)];I=[0]
for i,v in enumerate(h):
    if i!=37:I.extend([s|1<<i for s in I if not s&v]);
T=[t for t in I if t.bit_count()==9];r=dict(site35=decode(graph([int(w,2) for w in W])),site37=decode(graph([s for s in I if all(t&s for t in T)])),six_cycle=decode([{(i+1)%6,(i-1)%6} for i in range(6)]));print(r);(D/'ramsey_squares_to_bits.json').write_text(json.dumps(r,indent=2)+'\n')
