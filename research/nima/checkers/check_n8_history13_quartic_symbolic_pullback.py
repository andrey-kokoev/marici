#!/usr/bin/env python3
"""Formal symbolic pullback proof for the reconstructed history-13 quartic."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
data=json.loads((ROOT/'research/nima/results/n8-history13-quartic-reconstruction.json').read_text());a=s.symbols('a1:9');A1,A2,A3,A4,A5,A6,A7,A8=a
G=s.Matrix([[1,A1,A2+A3+A4,(A2+A3+A4)*A5,(A3+A4)*A6,A4*A7,0],[0,0,1,A5,A6,A7,A8]]).subs(A4,0)
q={x['history_index']:x for x in json.loads((ROOT/'research/nima/results/eight-point-history-positroid-matching.json').read_text())['matches']}[13];emb=q['embedding'];C=s.zeros(2,8)
for j in range(G.cols):C[:,emb['support'][(j+emb['rotation'])%len(emb['support'])]-1]=G[:,j]
Z=s.Matrix([[s.Integer(t)**k for k in range(6)] for t in range(1,9)]);Y=C*Z;P=Y[:,[0,1]];adj=s.Matrix([[P[1,1],-P[0,1]],[-P[1,0],P[0,0]]]);D=s.expand(P.det());H=adj*Y
nums=[s.expand(H[i,j]) for i in range(2) for j in range(2,6)];vars=[x for x in a if x!=A4];domain=s.QQ
Dp=[s.Poly(1,*vars,domain=domain)]
for _ in range(4):Dp.append(Dp[-1]*s.Poly(D,*vars,domain=domain))
Np=[s.Poly(n,*vars,domain=domain) for n in nums];total=s.Poly(0,*vars,domain=domain)
for item in data['quartic_coefficients']:
 e=item['exponents'];degree=sum(e);term=Dp[4-degree]
 for i,k in enumerate(e):
  for _ in range(k):term*=Np[i]
 total+=s.Rational(item['coefficient'])*term
checks={'reconstruction_input_passed':data['passed'],'common_denominator_nonzero':D!=0,'quartic_has_189_terms':len(data['quartic_coefficients'])==189,'cleared_pullback_identically_zero':total.is_zero}
out={'schema':'marici.nima.n8-history13-quartic-symbolic-pullback.v1','history_index':13,'boundary':'G/alpha4=0','affine_target_chart':'pivot columns 1,2','common_denominator':str(s.factor(D)),'cleared_pullback_term_count':len(total.terms()),'checks':checks,'passed':all(checks.values()),'conclusion':'The reconstructed affine quartic vanishes identically under the symbolic seven-parameter boundary map after multiplication by the fourth power of its target-chart denominator.'};p=ROOT/'research/nima/results/n8-history13-quartic-symbolic-pullback.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
