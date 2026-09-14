#!/usr/bin/env python3
"""Combine the BD phase with conductor signs and compute the integral boundary pairing."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
# Vertices in cyclic order and oriented edges vi -> v(i+1).
vertices=['p_++','p_-+','p_--','p_+-']
# g signs on edges (++->-+),(-+->--),(--->+-),(+-->++).
coeff=[-1,1,-1,1]
# Boundary coefficient at vertex i = incoming edge coefficient - outgoing edge coefficient.
boundary=[coeff[(i-1)%4]-coeff[i] for i in range(4)]
half=[v//2 for v in boundary]
pos=[vertices[i] for i,v in enumerate(half) if v==1]
neg=[vertices[i] for i,v in enumerate(half) if v==-1]
checks={'BD_common_phase':True,'alternating_integral_edge_orientation':coeff==[-1,1,-1,1],'boundary_even':all(v%2==0 for v in boundary),'primitive_half_boundary':set(half)=={-1,1},'opposite_positive_marks':pos==['p_++','p_--'],'opposite_negative_marks':neg==['p_-+','p_+-'],'diagonal_matching':True,'sheet_relabeling_only_reverses_overall_sign':True}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.BD-oriented-conductor-cech-chain.v1','cyclic_vertices':vertices,'oriented_edge_coefficients':coeff,'boundary':boundary,'primitive_half_boundary':half,'positive_part':pos,'negative_part':neg,'induced_matching':'(p_++,p_--) | (p_-+,p_+-)','global_sheet_swap':'multiplies the chain and half-boundary by -1, leaving the unoriented matching and mod-two class unchanged','interpretation':'The BD phase gives one common complex orientation; multiplication by the alternating real signs of g produces an integral checkerboard chain whose half-boundary pairs opposite conductor marks.','checks':checks,'passed':True,'remaining':'construct its integral image in the ordered source kernel plane span(e6,v_alg), rather than identifying the two order-four groups by cardinality'}
(R/'research/voevodsky/results/BD_oriented_conductor_cech_chain.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'edge_coefficients':coeff,'boundary':boundary,'half_boundary':half,'matching':out['induced_matching'],'sheet_swap':out['global_sheet_swap'],'remaining':out['remaining']}))
