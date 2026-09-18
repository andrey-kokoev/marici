#!/usr/bin/env python3
"""Exact branch structure of the source four-mass prefactor psi."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_mass_auxiliary_branches,four_mass_psi
Z={1:s.Matrix([1,0,2,1]),2:s.Matrix([0,1,1,3]),3:s.Matrix([2,1,0,1]),4:s.Matrix([1,3,1,0]),5:s.Matrix([3,0,1,2]),6:s.Matrix([1,2,4,1]),7:s.Matrix([2,3,1,5]),8:s.Matrix([4,1,3,2])}
branches=four_mass_auxiliary_branches(*(Z[i] for i in range(1,9)))
psis=[four_mass_psi(A,B,Z[1],Z[2],Z[4],Z[5],Z[6],Z[8]) for _,_,A,B in branches]
t=s.symbols('t');sum_psi=s.simplify(sum(psis));product_psi=s.simplify(s.prod(psis));minimal=s.factor(t**2-sum_psi*t+product_psi)
checks={'two_finite_nonzero_values':len(psis)==2 and all(v not in (0,s.zoo,s.nan) for v in psis),'branches_distinct':s.simplify(psis[0]-psis[1])!=0,'branch_sum_rational':sum_psi.is_Rational is True,'branch_product_rational':product_psi.is_Rational is True,'monic_quadratic_from_symmetric_data':s.expand(minimal-(t**2-sum_psi*t+product_psi))==0}
out={'schema':'marici.nima.four-mass-psi-branches.v1','source':'arXiv:1212.5605, psi definition below Table g2n_yangian_invariants','formula':'psi=(1-<A456><B812>/(<A412><B856>))^-1','branch_values':[str(v) for v in psis],'branch_sum':str(sum_psi),'branch_product':str(product_psi),'minimal_polynomial':str(minimal),'checks':checks,'passed':all(checks.values()),'scope':'Exact algebraic evaluation at one generic integer momentum-twistor configuration; psi alone is branch-dependent.'}
p=ROOT/'research/nima/results/four-mass-psi-branches.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
