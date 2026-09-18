#!/usr/bin/env python3
"""Exact components of the branch-summed four-mass N2MHV invariant."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_mass_auxiliary_branches,four_mass_psi
from momentum_twistor_super import SuperTwistor,external_supertwistor,super_five_bracket,super_five_bracket_product_component
Z={1:s.Matrix([1,0,2,1]),2:s.Matrix([0,1,1,3]),3:s.Matrix([2,1,0,1]),4:s.Matrix([1,3,1,0]),5:s.Matrix([3,0,1,2]),6:s.Matrix([1,2,4,1]),7:s.Matrix([2,3,1,5]),8:s.Matrix([4,1,3,2])};S={i:external_supertwistor(i,Z[i]) for i in Z}
probes=[((1,5),(2,6),(1,5),(2,6)),((1,5),(2,6),(3,7),(4,8)),((2,7),(3,8),(1,6),(4,5)),((4,8),(1,7),(2,5),(3,6))]
values=[[] for _ in probes];psis=[]
for alpha,beta,A,B in four_mass_auxiliary_branches(*(Z[i] for i in range(1,9))):
 SA=SuperTwistor(A,{7:s.Integer(1),8:alpha});SB=SuperTwistor(B,{3:s.Integer(1),4:beta})
 left=super_five_bracket((SA,S[1],S[2],S[3],S[4]));right=super_five_bracket((SB,S[5],S[6],S[7],S[8]));psi=four_mass_psi(A,B,Z[1],Z[2],Z[4],Z[5],Z[6],Z[8]);psis.append(psi)
 for i,pairs in enumerate(probes): values[i].append(s.factor(psi*super_five_bracket_product_component(left,right,pairs)))
rows=[]
for pairs,branches in zip(probes,values):
 total=s.simplify(sum(branches));rows.append({'pairs':[list(x) for x in pairs],'branches_nonzero':all(v!=0 for v in branches),'branches_distinct':s.simplify(branches[0]-branches[1])!=0,'summed_component':str(total),'sum_rational':total.is_Rational is True,'sum_nonzero':total!=0})
checks={'two_algebraic_branches':len(psis)==2 and s.simplify(psis[0]-psis[1])!=0,'four_independent_components_checked':len(rows)==4,'all_branch_contributions_nonzero':all(r['branches_nonzero'] for r in rows),'all_branch_sums_rational':all(r['sum_rational'] for r in rows),'all_branch_sums_nonzero':all(r['sum_nonzero'] for r in rows)}
out={'schema':'marici.nima.four-mass-branch-summed-superinvariant.v1','source':'arXiv:1212.5605 starred class in Table g2n_yangian_invariants and four_mass_explicit_solution','formula':'sum_branches psi [A,1,2,3,4] [B,5,6,7,8]','component_probes':rows,'checks':checks,'passed':all(checks.values()),'scope':'Four exact degree-eight components of the source-prescribed two-solution sum at generic integer kinematics.'}
p=ROOT/'research/nima/results/four-mass-branch-summed-superinvariant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
