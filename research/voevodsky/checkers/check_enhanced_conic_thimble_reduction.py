#!/usr/bin/env python3
"""Mod-two strict-transform reduction for the conic through four enhanced points."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
geom=json.loads((ROOT/'research/voevodsky/results/split_fiber_first_normal_jet.json').read_text())
# Basis H,E++,E+-,E-+,E-- for the first blowup at four simple marked points on C.
C=s.Matrix([2,-1,-1,-1,-1]);Cmod=C.applyfunc(lambda v:int(v)%2)
exceptional_sum=s.Matrix([0,1,1,1,1])
checks={
 'prior_smoothing_packet':geom['passed'],
 'conic_degree_two':int(C[0])==2,
 'four_point_multiplicity_one_in_first_blowup':all(int(v)==-1 for v in C[1:]),
 'mod_two_equals_exceptional_sum':Cmod==exceptional_sum,
 'ambient_H_part_even':int(Cmod[0])==0,
 'exceptional_support_four':sum(int(v) for v in Cmod)==4,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.enhanced-conic-thimble-reduction.v1','passed':True,'blowup_basis':['H','E++','E+-','E-+','E--'],'strict_transform_conic':[2,-1,-1,-1,-1],'mod_two_class':[0,1,1,1,1],'desired_column_formula':'pi_alg(E+++E+-+E-++E--) mod 2','pi_alg_columns_available':False,'remaining':'compute four exceptional curve images in the integral (e6,v_alg) Gysin-kernel marking','scope':'first common blowup; any further local semistable exceptional chains must be pushed forward to these classes','checks':checks}
p=ROOT/'research/voevodsky/results/enhanced_conic_thimble_reduction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'thimble_parity_support':['E++','E+-','E-+','E--']}))
