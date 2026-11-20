"""Transport constraints along with matchings. Compare full feasible sets at every quarter turn, and test the extra (different) demand that all transported boundary flags hold simultaneously."""
from ramsey_strip_next_duality_filter import image,solutions
from ramsey_strip_boundary_binary_search import initial,leaves
from ramsey_strip_minimal_shared_constraints import allms
from ramsey_strip_matching_restart import r,turn
f,= [f for f in solutions if f[16]==7 and f[7]==17];assert all(f[f[i]]==r[i] for i in range(30))
C=frozenset(initial);S=set(leaves);union=set();history=[]
for k in range(4):
    exact={m for m in allms if C<=m};assert exact==S and len(S)==36
    union|=C;history.append(C);print('quarter turn',k,'boundary',sorted(C),'feasible',len(S),'cumulative feasible',sum(union<=m for m in allms))
    C=image(C,f);S={image(m,f) for m in S}
assert C==initial and S==set(leaves) and history[2]==turn(initial)
assert len({m for m in allms if set.union(*(set(c) for c in history))<=m})==0
