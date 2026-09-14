#!/usr/bin/env python3
"""Compute local incidence/linking of the total-energy cusp with the v_alg dlog divisor."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
E,X1,X2=s.symbols('E X1 X2')
Dm=E**2-X1*X2;Dp=E**2+X1*X2;D=s.expand(Dm*Dp)
checks={'factor_identity':s.expand(D-(E**4-X1**2*X2**2))==0,'Dminus_unit_at_cusp':Dm.subs(E,0)==-X1*X2,'Dplus_unit_at_cusp':Dp.subs(E,0)==X1*X2,'product_unit_at_cusp':D.subs(E,0)==-X1**2*X2**2,'no_E_factor':s.rem(D,E,E)!=0,'dlog_residue_at_E0':s.limit(E*s.diff(D,E)/D,E,0)==0,'first_E_derivative_zero':s.diff(D,E).subs(E,0)==0}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.total-energy-valg-divisor-linking.v1','v_alg_dlog_divisor':'D=(E^2-X1*X2)(E^2+X1*X2)','restriction_to_total_energy_cusp':'D|E=0=-X1^2*X2^2','generic_locus':'X1*X2 != 0','intersection_with_E0_generic':'empty','residue_of_dlogD_along_E0':0,'local_winding_of_D_around_small_E_loop':0,'geometric_consequence':'A total-energy thimble localized at generic E=0 has zero linking with the two v_alg divisor components.','parity_consequence_if_integral_dual_is_divisor_linking':'b=0','remaining_gate':'identify the integral v_alg dual pairing with the linking functional of the source-proved dlog divisor; the rational connection proves the support but not by itself the integral Betti normalization','checks':checks,'passed':True}
(R/'research/voevodsky/results/total_energy_valg_divisor_linking.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'restriction':out['restriction_to_total_energy_cusp'],'residue':0,'geometric_consequence':out['geometric_consequence'],'conditional_bit':out['parity_consequence_if_integral_dual_is_divisor_linking'],'gate':out['remaining_gate']}))
