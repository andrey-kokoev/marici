"""Independent cross-check on a fixed sample of --sweep results. uv run --with igraph --with python-sat python ..."""
from ramsey312_google_two_step import *
import igraph,random

def main():
 el=list(sets(F,11));ten=list(sets(F,10));rs=json.loads((D/'ramsey312_five_sweep_cover_samples.json').read_text());pool=[sum(1<<int(v) for v in l.split()) for l in (D/'ramsey312_five_clique_inputs.txt').read_text().splitlines()];rng=random.Random(4340);chosen=rng.sample(pool,min(40,len(pool)));res=[]
 def clauses(h):
    lo=sum(1<<v for v in bits(h) if (adj[v]&h).bit_count()<11);clauses=[[-1-v,-1-w] for v in bits(lo) for w in bits(adj[v]&lo&((1<<v)-1))];clauses.extend([i+1 for i in bits(s)] for s in {s&lo for s in el if not s&~h});return lo,clauses
 for d,n,tag,c in rs:
    h=F^d;lo,C=clauses(h)
    for b,t in zip(c[::2],c[1::2]):
        assert b.bit_count()==1 and b&lo and not b&t and t.bit_count()==10 and not t&~h and all(not adj[i]&t for i in bits(t));C.append([-b.bit_length(),*[i+1 for i in bits(t&lo)]])
    with Solver(name='g4',bootstrap_with=C) as sl:assert not sl.solve()
 for d in chosen:
    h=F^d;lo,C=clauses(h);S=[]
    with Solver(name='g4',bootstrap_with=C) as sl:
        while sl.solve():
            s=sum(1<<(i-1) for i in sl.get_model() if i>0)&lo;S.append(s);sl.add_clause([-(i+1) if s>>i&1 else i+1 for i in bits(lo)])
    # Instead of targeted independent-set searches, explicitly index all independent tens inside this core.
    tens=[t for t in ten if not t&d];cols=[int.from_bytes(bytes(sum(((t>>i)&1)<<j for j,t in enumerate(tens[k:k+8])) for k in range(0,len(tens),8)),'little') for i in range(n_vertices)];allten=(1<<len(tens))-1;miss=[]
    for s in S:
        m=allten
        for i in bits(s):m&=~cols[i]
        assert s and m;miss.append(m)
    pairs=[(i,j) for i,s in enumerate(S) for j in range(i) if not s&S[j] or not miss[i]&miss[j]];G=igraph.Graph(n=len(S),edges=pairs);w=G.clique_number();assert w==5;res.append(dict(d=d,supports=len(S),edges=len(pairs),omega=w))
 print('certificate replays',len(rs),'clique replays',len(res));(D/'ramsey312_five_sweep_replay.json').write_text(json.dumps(dict(covers=len(rs),graphs=res)))
n_vertices=52
if __name__=='__main__':main()
