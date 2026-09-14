#!/usr/bin/env python3
"""Serialize the normalized physical period monodromy and its predictions."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
law=json.loads((R/'research/voevodsky/results/marked_top_log_discontinuity_law.json').read_text())
assert law['ordered_physical_parity']==[1,0]
# Period-column order (Pi111_reg, Pi_epsilon6, Pi_valg).
# Positive loop convention; reversing the loop replaces +1 by -1.
T=[[1,1,0],[0,1,0],[0,0,1]]
I=[[1,0,0],[0,1,0],[0,0,1]]
N=[[T[i][j]-I[i][j] for j in range(3)] for i in range(3)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
N2=mm(N,N)
def Tk(k):return [[1,k,0],[0,1,0],[0,0,1]]
checks={'unipotent':all(T[i][i]==1 for i in range(3)),'nilpotent_square_zero':N2==[[0]*3 for _ in range(3)],'rank_one_image':sum(v!=0 for row in N for v in row)==1,'top_jump_is_e6':N[0]==[0,1,0],'v_alg_spectator':all(T[i][2]==I[i][2] and T[2][i]==I[2][i] for i in range(3)),'two_windings_even':Tk(2)[0][1]%2==0,'reverse_loop_same_mod2':(-1)%2==1}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.physical-cusp-monodromy-transvection.v1','period_basis':['Pi111_reg','Pi_epsilon6','Pi_v_alg'],'positive_loop_monodromy':T,'nilpotent_logarithm':N,'negative_loop_monodromy':Tk(-1),'k_winding_monodromy_formula':'[[1,k,0],[0,1,0],[0,0,1]]','experimental_relations':['one winding: Delta Pi111_reg = 2*pi*i Pi_epsilon6 after logarithmic normalization','k windings: normalized jump coefficient = k','two windings: parity readout returns 0','loop reversal changes the integer sign and preserves mod-two parity','Pi_v_alg has zero cusp jump in this marked-top channel'],'mod_two_monodromy':[[v%2 for v in row] for row in T],'ordered_single_winding_parity':[1,0],'comparison_gate':law['comparison_gate'],'checks':checks,'passed':True}
(R/'research/voevodsky/results/physical_cusp_monodromy_transvection.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'T':T,'N':N,'predictions':out['experimental_relations'],'parity':out['ordered_single_winding_parity']}))
