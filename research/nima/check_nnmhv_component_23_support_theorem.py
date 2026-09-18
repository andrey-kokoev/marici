#!/usr/bin/env python3
"""Symbolic matrix identity and all-n combinatorics behind component support."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import adjugate2
from nnmhv_coherence_paths import compile_nnmhv_histories,supports_component_23
a,b,c,d,u,v=s.symbols('a b c d u v');A=s.Matrix([[a,b],[c,d]]);B=s.Matrix([[u,v],[s.symbols('w'),s.symbols('z')]]);xi=s.Matrix([[s.symbols('r'),s.symbols('t')]])
identity=s.simplify(xi*A*adjugate2(B)+xi*(A+B)*adjugate2(-B)+B.det()*xi)
counts=[]
for n in range(6,31):
 hs=compile_nnmhv_histories(n);actual=sum(supports_component_23(h) for h in hs);counts.append({'n':n,'supported':actual,'formula':(n-5)*(n-4)//2})
checks={'matrix_identity_L_plus_R':identity==s.zeros(1,2),'support_count_formula_n6_to30':all(r['supported']==r['formula'] for r in counts),'supported_histories_have_required_ranges':all(h.outer_pair[1]>=h.inner_pair[1]>=5 for n in range(6,31) for h in compile_nnmhv_histories(n) if supports_component_23(h))}
out={'schema':'marici.nima.nnmhv-component-23-support-theorem.v1','identity':'L+R=-det(x_ab) xi','counts':counts,'checks':checks,'passed':all(checks.values()),'proof':'research/nima/nnmhv-component-23-support-theorem.md'}
p=ROOT/'research/nima/results/nnmhv-component-23-support-theorem.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
