"""Parameter test for a history-indexed (non-terminal) Green form."""
from pathlib import Path
import sympy as s, json
ROOT=Path(__file__).resolve().parents[3]
N=48
Q=s.diag(*[(-1)**m.bit_count() for r in range(6) for m in range(8)])
eps=s.Matrix([(-1)**(bin(r).count('1')%2) for r in range(6)])
# Use the two known marginal ghosts as calibration directions.
g0=s.zeros(N,1);g1=s.zeros(N,1)
for r,e in enumerate(eps):
    g0[8*r]=e
    for m in (1,2,4):g1[8*r+m]=e
G=s.Matrix.hstack(g0,g1)
# History-indexed correction: it changes only attachment correlations and leaves
# the local graded form on the complement untouched.
alpha,beta=s.symbols('alpha beta', real=True)
H=Q + alpha*(g0*g0.T)/6 + beta*(g1*g1.T)/(-18)
assert s.simplify((G.T*H*G)[0,0]-6-alpha*6)==0
assert s.simplify((G.T*H*G)[1,1]+18-beta*18)==0
assert (G.T*H*G)[0,1]==0
# Any alpha,beta != -1 keeps the two ghost directions nondegenerate.
H1=H.subs({alpha:1,beta:1})
assert H1.det()!=0
result={'schema':'marici.grothendieck.history-indexed-green-ansatz.v1','passed':True,
 'dimension':N,'base_form_rank':Q.rank(),'calibration_ghost_matrix':[[6,0],[0,-18]],
 'corrected_ghost_matrix_at_alpha_beta_1':[[12,0],[0,-36]],
 'corrected_form_rank':H1.rank(),
 'terminal_descent':'not imposed; imposing it would annihilate both calibration directions',
 'status':'ansatz only; coefficients must be fixed by the analytic Clark cross-cut kernel, not chosen numerically'}
(ROOT/'research/grothendieck/results/history-indexed-green-ansatz.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
