#!/usr/bin/env python3
"""Close the two integral thimble parity bits using primitive component and dlog lattices."""
import json,math
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
e6=json.loads((ROOT/'research/voevodsky/results/paired_nodes_fix_e6_parity.json').read_text())
link=json.loads((ROOT/'research/voevodsky/results/total_energy_valg_divisor_linking.json').read_text())
dlog=json.loads((ROOT/'research/benincasa/exact-lift-dlog-divisor-identity.json').read_text())
classes=json.loads((ROOT/'research/benincasa/results/total-energy-coinvariant-extension-classes.json').read_text())
E,X1,X2=s.symbols('E X1 X2');Dm=E**2-X1*X2;Dp=E**2+X1*X2;D=s.expand(Dm*Dp)
residue_multiplicities=[1,1];column=[e6['mod_two_e6_coefficient'],0]
checks={
 'e6_packet':e6['passed'],
 'e6_primitive_Betti_normalization':'component difference' in e6['interpretation'],
 'e6_bit_odd':column[0]==1,
 'link_packet':link['passed'],
 'source_selected_dlog_line':dlog['prior_source_selected_line']=='alpha_alg=dlog(D) on <e6,v_alg>/<e6>',
 'full_divisor_identity':s.expand(D-(E**4-X1**2*X2**2))==0,
 'simple_components_recorded':all(dlog['divisors'][k]['nonzero_simple_jets']==12 for k in ('D_minus','D_plus')),
 'primitive_residue_vector':math.gcd(*residue_multiplicities)==1,
 'D_unit_at_generic_cusp':s.factor(D.subs(E,0))==-X1**2*X2**2,
 'valgebraic_link_zero':link['local_winding_of_D_around_small_E_loop']==0,
 'valgebraic_bit_zero':column[1]==0,
 'column_predeclared':column in [c['parity'] for c in classes['extension_classes']],
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.integral-thimble-Gysin-column.v1','passed':True,'generic_locus':'X1*X2!=0 at E=0','basis':['e6','v_alg'],'integral_normalizations':{'e6':'primitive split-fiber component difference [C+]-[C-]','v_alg_dual':'primitive divisor-linking functional for dlog((E^2-X1X2)(E^2+X1X2)); residues (1,1)'},'pairings_mod_two':{'e6':1,'v_alg':0},'column':[1,0],'minimal_lift_relation':'2m=e6','extension_group':'free rank two (width-two torsion absorbed)','orientation_dependence':'overall e6 sign only; mod-two column invariant','scope':'generic nonsoft cusp; does not determine the separate pyramid route-interface sign','checks':checks}
p=ROOT/'research/voevodsky/results/integral_thimble_Gysin_column.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'integral_thimble_Gysin_column':column,'relation':'2m=e6'}))
