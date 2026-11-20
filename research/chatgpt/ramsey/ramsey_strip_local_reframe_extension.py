"""Construct from two local prescriptions: choose the other boundary-compatible row-invariant ten-cycle; map the directed entry (0,16) to (29,7). Extend through unique spokes, then check incidence and square, never select on square."""
from ramsey_all_ten_cycle_layers import cycles,N
from ramsey_strip_layer_quarter_turn import C,r
edge=lambda a,b:tuple(sorted((a,b)))
flags={(0,16),(0,17),(4,29),(7,29)};alternatives=[]
for p in cycles:
    E={edge(a,b) for a,b in zip(p,p[1:]+p[:1])};S=set(p)
    if flags<=E and {r[v] for v in S}==S and S!=set(C):alternatives.append(S)
S,=alternatives
for port in (7,4):
    Q=[29,port]
    while len(Q)<10:
        x,=(N[Q[-1]]&S)-{Q[-2]};Q.append(x)
    assert Q[0] in N[Q[-1]]
    def layers(p):
        middle=[next(iter(N[v]-set(p))) for v in p];outer=[next(iter(N[v]-set(p)-set(middle))) for v in middle];return p,middle,outer
    F={a:b for L,K in zip(layers(C),layers(Q)) for a,b in zip(L,K)};assert len(F)==30 and len(set(F.values()))==30
    assert all({F[y] for y in N[x]}==N[F[x]] for x in range(30))
    assert all(F[F[x]]==r[x] for x in range(30));print('directed flag (0,16) ->',(29,port),'target ordered cycle',Q,'square equals row swap',True)
