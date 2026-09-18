#!/usr/bin/env python3
"""Exact check of the supersymmetric line-plane point constructor."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_bracket,line_plane_point
from momentum_twistor_super import external_supertwistor,super_line_plane_point
xs=map(s.Integer,(1,2,4,7,11));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
S={i:external_supertwistor(i,Z[i]) for i in Z}
X=super_line_plane_point(S[1],S[2],S[3],S[4],S[5])
alpha=four_bracket(Z[2],Z[3],Z[4],Z[5]);beta=four_bracket(Z[3],Z[4],Z[5],Z[1])
checks={'bosonic_part_matches_public_constructor':X.z==line_plane_point(Z[1],Z[2],Z[3],Z[4],Z[5]),'fermionic_support_is_line_endpoints':set(X.chi)=={1,2},'fermionic_coefficients_match_source':X.chi[1]==alpha and X.chi[2]==beta,'bosonic_incidence_line':four_bracket(Z[1],Z[2],X.z,Z[3])==0,'bosonic_incidence_plane':four_bracket(X.z,Z[3],Z[4],Z[5])==0}
out={'schema':'marici.nima.super-line-plane-constructed-twistor.v1','source':'arXiv:1008.2958, all_loop__v2_penult.tex:275-278; arXiv:1212.5605 Cramers_rule/table preamble','object':'(12) intersect (345)','chi_coefficients':{str(k):str(v) for k,v in X.chi.items()},'checks':checks,'passed':all(checks.values()),'scope':'Exact bosonic incidence and sparse fermionic linear-combination check for the super line-plane constructor.'}
p=ROOT/'research/nima/results/super-line-plane-constructed-twistor.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
