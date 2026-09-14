#!/usr/bin/env python3
"""Counterexample: regular diagonal dlog support does not determine an off-diagonal cusp extension."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
E,c,lam=s.symbols('E c lambda', nonzero=True)
D=c+E**2 # a unit at E=0
# Coefficient matrix A(E)dE: first line is regular with diagonal dlog D,
# while the extension into it has arbitrary logarithmic residue lambda.
A=s.Matrix([[s.diff(D,E)/D,lam/E],[0,0]])
Res=s.simplify((E*A).subs(E,0))
checks={'D_unit_at_zero':D.subs(E,0)==c,'diagonal_residue_zero':Res[0,0]==0,'offdiagonal_residue_arbitrary':Res[0,1]==lam,'nilpotent_extension_survives':Res**2==s.zeros(2),'example_flat_on_one_dimensional_base':True}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.diagonal-regular-extension-counterexample.v1','connection':'A=dlog(c+E^2) on target diagonal plus lambda*dE/E off diagonal','residue_matrix':[[str(x) for x in Res.row(i)] for i in range(2)],'conclusion':'Zero residue of the v_alg diagonal connection at E=0 does not imply zero elliptic-to-v_alg extension residue.','category_error':'The divisor E^4-X1^2X2^2 lies in the kinematic base and controls diagonal transport of the algebraic line; v_alg^vee is a fiber Betti functional. Identifying these two linking problems requires the missing comparison map.','invalidated_claim':'b=0 does not follow from disjointness of E=0 and the base dlog divisor.','checks':checks,'passed':True}
(R/'research/voevodsky/results/diagonal_regular_extension_counterexample.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'residue':out['residue_matrix'],'conclusion':out['conclusion'],'invalidated':out['invalidated_claim']}))
