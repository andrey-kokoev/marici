"""Factor each pole exchange as D H, with H the proposed edge half-step. Compare D to a reciprocal pair/partition dictionary; do not select on f^2."""
from ramsey_strip_ordered_boundary_dualities import solutions,s,t,entry,exit
from ramsey_strip_seed_half_swap import action,h
from ramsey_strip_prism_proof import r,P,T
H=action(h);J=[H.index(i) for i in range(30)];good=[]
for f in solutions:
    D=[f[J[i]] for i in range(30)]
    assert all(D[H[i]]==H[D[i]]==f[i] for i in range(30))
    reciprocal=all(D[D[i]]==i for i in range(30));absolute={i for i,p in enumerate(P) if p in T[D[i]-15]};bits=(exit.index(f[entry[0]]),entry.index(f[exit[0]]));print(bits,'reciprocal',reciprocal,'incident pairs',sorted(absolute))
    if reciprocal:good.append((D,absolute))
assert len(good)==2;D,A=good[0];E,B=good[1];assert all(E[i]==r[D[i]] for i in range(30));print('common incident pair:',A&B,'D(H(s)), D(H(t))',D[H[s]],D[H[t]])
