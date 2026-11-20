"""Separate ordinary matching propagation from imposing C5 orbit closure of a local hub flag. Test whether the remaining finite flag is forced."""
from collections import Counter
from ramsey_strip_cyclic_matching_eight_states import signatures,hub,ring,P,G,action,moved
from ramsey_strip_forced_local_propagation import propagate,adj
from ramsey_strip_minimal_shared_constraints import allms
A=signatures[1,];B=signatures[1,2];C=signatures[1,3];obs=A&B&C;assert len(obs)==5
d=P.index(tuple(sorted((hub,ring[0]))));d2=P.index(tuple(sorted((ring[0],ring[2]))))
for name,M in [('stay',A),('enlarge',B)]:
 e,=[e for e in M if e[0]==d]
 for symmetric in (False,True):
    given=obs|({e} if not symmetric else frozenset().union(*(moved({e},action(p)) for p in G)))
    chosen,left,rounds=propagate(given);completions=[m for m in allms if given<=m]
    print(name,'orbit closure',symmetric,'given links',len(given),'forced additional',len(chosen)-len(given),'remaining',len(left),'matching completions',len(completions),'remaining degrees',dict(Counter(len(adj[v]&left) for v in left)))
    if symmetric and name=='enlarge':
        assert set(completions)=={B,C} and all(len(adj[v]&left)==2 for v in left)
        for dest in (B,C):
            choice,=[e for e in dest if e[0]==d2];full,rem,rs=propagate(chosen|{choice});assert not rem and full==dest
        print('either finite-pair choice completes uniquely by ordinary local propagation')
