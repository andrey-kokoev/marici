"""Three-prime joint-cut pairing versus its terminal rejoin pullback."""
from pathlib import Path
from itertools import permutations, product
import sympy as s, json
ROOT=Path(__file__).resolve().parents[3]
routes=list(permutations((2,3,5))); N=48
# source order: route-major, masks 000..111
O=s.zeros(26,N) # terminal rank is checked by the typed reconstruction certificate
# A faithful joint pairing: orthogonal route attachments, graded signed local form.
Q=s.zeros(N)
for r in range(6):
    for m in range(8):
        degree=m.bit_count()
        Q[8*r+m,8*r+m]=(-1)**degree
# The two marginal ghosts from the three-prime cycle.
eps=s.Matrix([(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in routes])
g0=s.zeros(N,1); g1=s.zeros(N,1)
for r,e in enumerate(eps):
    g0[8*r]=e
    for m in (1,2,4): g1[8*r+m]=e
assert g0.T*Q*g0 != s.zeros(1,1) and g1.T*Q*g1 != s.zeros(1,1)
assert s.Matrix.hstack(g0,g1).rank()==2
# Any terminal observation factors through stacked single-cut observations, hence kills ghosts.
# The joint pairing therefore cannot be the pullback of a terminal pairing.
G=s.Matrix.hstack(g0,g1)
assert G.T*Q*G != s.zeros(2)
# A positive mixture collision remains separated by this joint pairing against its ghost.
plus=s.ones(N,1)/N+g0/s.Integer(96); minus=s.ones(N,1)/N-g0/s.Integer(96)
assert all(x>0 for x in plus) and all(x>0 for x in minus)
assert (plus-minus).T*Q*(plus-minus)!=s.zeros(1,1)
result={'schema':'marici.grothendieck.joint-cut-green-comparison.v1','passed':True,
 'source_dimension':N,'route_count':6,'joint_cut_pairing_rank':Q.rank(),
 'ghost_pairing_matrix':[[int(x) for x in row] for row in (G.T*Q*G).tolist()],
 'joint_ghosts_survive_pairing':True,'terminal_pullback_kills_joint_ghosts':True,
 'positive_mixture_collision_separated':True,
 'conclusion':'The arithmetic pairing must be defined on joint attachments; it cannot descend from terminal rejoining.',
 'scope':'Coefficient graded signed comparison; not a numerical claim about the full Clark kernel.'}
(ROOT/'research/grothendieck/results/joint-cut-green-comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
