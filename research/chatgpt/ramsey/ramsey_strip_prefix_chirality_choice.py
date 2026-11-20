"""Given a symmetric fivefold flag orbit, test when the directed short route distinguishes its two chiral completions. The group is assumed inferred; do not claim this identifies it from the route alone."""
from ramsey_strip_intrinsic_fivefold_transport import records,P
from ramsey_strip_asymmetric_generator import directed
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_matching_restart import r
base=[0,16,13,19,7,29]
for n,o,m,G,candidates,correct in records:
    gen,hub=directed(m);observed={e for e in m if hub in P[e[0]]};assert len(observed)==5
    pair=[M for M in allms if observed<=M];assert len(pair)==2 and m in pair;other,=[M for M in pair if M!=m]
    p=base if o==0 else [r[v] for v in base];flags=[];survivors=[]
    for i,(a,b) in enumerate(zip(p,p[1:])):
        if i%2:a,b=r[a],r[b]
        e=tuple(sorted((a,b)));assert e in m;flags.append(e);survivors.append(sum(set(flags)<=M for M in pair))
    print('source',n,o,'remaining chiral choices along half-route',survivors,'first decisive flag',flags[survivors.index(1)],'both boundary flags distinguish',not {flags[0],flags[-1]}<=other)
