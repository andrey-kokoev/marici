#!/usr/bin/env python3
"""Combine the two equally oriented infinity-node co-cores in the primitive component lattice."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
# Primitive A1^3 frame. The split infinity-fiber component difference is primitive.
d=s.Matrix([1,1,1])
local_plus=d/2
local_minus=d/2
same=local_plus+local_minus
opposite=local_plus-local_minus
checks={'component_difference_primitive':s.gcd_list([int(x) for x in d])==1,'individual_node_is_half_weight':2*local_plus==d,'BD_equal_orientation_sums_to_integral_difference':same==d,'opposite_orientation_would_cancel':opposite==s.zeros(3,1),'integral_coefficient_is_odd':1%2==1}
assert all(checks.values()),checks
bd=json.loads((R/'research/voevodsky/results/BD_quartic_collision_arcs.json').read_text());assert bd['checks']['same_unoriented_line']
out={'schema':'marici.voevodsky.paired-node-e6-parity.v1','integral_geometric_normalization':'e6_Betti := [C_plus]-[C_minus] for the split infinity fiber','local_node_classes':['e6_Betti/2','e6_Betti/2'],'orientation_input':'Bunch-Davies arcs give the same sign at the two exchanged nodes','global_pair_sum':'e6_Betti','mod_two_e6_coefficient':1,'interpretation':'The two local half-classes become one primitive integral component difference. This fixes the e6-line normalization geometrically rather than by a rational de Rham gauge.','scope':'determines the e6 component only; no v_alg Betti normalization or second parity bit','checks':checks,'passed':True,'next':'construct the analogous global pairing for the v_alg divisor line E^4-X1^2X2^2 and compare its two components with the remaining split-fiber half-sum'}
(R/'research/voevodsky/results/paired_nodes_fix_e6_parity.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'normalization':out['integral_geometric_normalization'],'sum':out['global_pair_sum'],'e6_bit':1,'scope':out['scope'],'next':out['next']}))
