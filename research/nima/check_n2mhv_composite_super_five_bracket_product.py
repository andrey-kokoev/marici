#!/usr/bin/env python3
"""Exact Grassmann product for one source-listed composite N2MHV invariant."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_super import (external_supertwistor,super_line_plane_point,
 super_five_bracket,multiply_super_five_brackets,
 super_five_bracket_product_component)
xs=map(s.Integer,(1,2,4,7,11,16,22,29));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)};S={i:external_supertwistor(i,Z[i]) for i in Z}
X=super_line_plane_point(S[4],S[5],S[6],S[7],S[8])
left=super_five_bracket((S[1],S[2],S[3],X,S[8]));right=super_five_bracket(tuple(S[i] for i in (4,5,6,7,8)))
product=multiply_super_five_brackets(left,right)
sample=tuple((a,b) for a,b in ((1,4),(2,5),(3,6),(7,8)))
# Nilpotence must remove every monomial repeating a label within one SU(4) component.
selected_fast=super_five_bracket_product_component(left,right,sample)
checks={'selected_component_algorithm_matches_full_product':selected_fast==product.get(sample,0),'grassmann_degree_eight':all(sum(len(pair) for pair in key)==8 for key in product),'canonical_two_generators_per_su4_component':all(all(a!=b for a,b in key) for key in product),'generic_product_nonzero':bool(product),'selected_component_present_nonzero':sample in product and product[sample]!=0,'input_degrees_four':all(len(m)==4 for m in left) and all(len(m)==4 for m in right)}
out={'schema':'marici.nima.n2mhv-composite-super-five-bracket-product.v1','source':'arXiv:1212.5605 Table g2n_yangian_invariants, configuration (1 2 3)(4 5)(6 7)(8)','formula':'[1,2,3,(45)cap(678),8] [4,5,6,7,8]','left_coefficients':len(left),'right_coefficients':len(right),'nonzero_degree_eight_coefficients':len(product),'sample_component':'(chi_1 chi_4)^1 (chi_2 chi_5)^2 (chi_3 chi_6)^3 (chi_7 chi_8)^4','sample_value':str(product.get(sample,0)),'fast_sample_value':str(selected_fast),'checks':checks,'passed':all(checks.values()),'scope':'Complete sparse degree-eight Grassmann product at one exact generic rational kinematic point; one N2MHV Yangian invariant, not the tree amplitude.'}
p=ROOT/'research/nima/results/n2mhv-composite-super-five-bracket-product.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
