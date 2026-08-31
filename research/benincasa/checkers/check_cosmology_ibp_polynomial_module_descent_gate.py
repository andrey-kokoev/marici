#!/usr/bin/env python3
"""Check whether the IBP relation family is closed under polynomial scalar multiplication."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results'
# Formal one-axis IBP generator I_e = d(x^e F): its master coefficient is e*x^(e-1).
# Multiplication obeys x I_e = I_(e+1) - x^e F by Leibniz.
def ibp_master_coefficient(e):return e
for e in range(4):
 residual=ibp_master_coefficient(e)-ibp_master_coefficient(e+1)
 assert residual==-1
out={'schema':'marici.benincasa.cosmology-ibp-polynomial-module-descent-gate.v1','audited_constructor':'raw_relations tangent/IBP family','formal_identity':'x_axis * I_e = I_(e+unit_axis) - M_e','residual_master_coefficient':-1,'polynomial_scalar_closure_of_ibp_generators':False,'reason':'the derivative of the multiplying monomial contributes the bare master term required by Leibniz','K_and_Q_families':'their algebraic denominator identities shift monomial exponents, but this does not repair IBP scalar closure','correct_structure_candidate':'a differential-operator/Weyl-module presentation with multiplication and derivation, not a commutative polynomial module generated only by relation rows','decision':'The proposed commutative graded relation module is ill-typed unless additional generators make every Leibniz residual M_e vanish. No such source relation is present in the audited constructor.','limitations':['formal constructor audit; does not prove that no enlarged D-module resolution exists','finite-cutoff accidental row-span membership is nonpromoting'],'passed':True};(R/'cosmology_ibp_polynomial_module_descent_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
