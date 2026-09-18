#!/usr/bin/env python3
"""PSL(2)-invariant de Sitter geometry of continuum history intervals."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
u,v,a,b,c,d=s.symbols('u v a b c d',nonzero=True);D=a*d-b*c;up=(a*u+b)/(c*u+d);vp=(a*v+b)/(c*v+d);dup=s.diff(up,u);dvp=s.diff(vp,v);invariance=s.factor(dup*dvp/(vp-up)**2-1/(v-u)**2)==0
coords=(u,v);f=s.Integer(2)/(v-u)**2;g=s.Matrix([[0,f],[f,0]]);gi=s.simplify(g.inv());Gamma=[[[s.simplify(sum(gi[k,l]*(s.diff(g[l,j],coords[i])+s.diff(g[l,i],coords[j])-s.diff(g[i,j],coords[l])) for l in range(2))/2) for j in range(2)] for i in range(2)] for k in range(2)];Ric=s.zeros(2)
for i in range(2):
 for j in range(2):
  Ric[i,j]=s.simplify(sum(s.diff(Gamma[k][i][j],coords[k])-s.diff(Gamma[k][i][k],coords[j])+sum(Gamma[k][k][l]*Gamma[l][i][j]-Gamma[k][j][l]*Gamma[l][i][k] for l in range(2)) for k in range(2)))
R=s.simplify(sum(gi[i,j]*Ric[i,j] for i in range(2) for j in range(2)));checks={'fractional_linear_metric_invariance':invariance,'lorentzian_signature':s.simplify(g.det()+f**2)==0,'scalar_curvature_constant':not ({u,v}&R.free_symbols),'ricci_proportional_to_metric':s.simplify(Ric-R*g/2)==s.zeros(2)}
out={'schema':'marici.nima.nnmhv-projective-interval-desitter-bridge.v1','endpoint_action':'u -> (a u+b)/(c u+d), v -> (a v+b)/(c v+d)','metric':'ds^2 = 4 du dv/(v-u)^2','scalar_curvature':str(R),'isometry_group':'PSL(2,R) locally isomorphic to SO^+(2,1)','checks':checks,'passed':all(checks.values()),'meaning':'The continuum limit of the history interval triangle is two-dimensional de Sitter kinematic space. The projective symmetry of transport acts as its Lorentz isometry group, unifying the projective and causal representations.','bridges':['projective PSL(2) symmetry','two-dimensional de Sitter space','Lorentz group SO(2,1)','conformal kinematic space of intervals','Möbius-invariant wave operator']};p=ROOT/'research/nima/results/nnmhv-projective-interval-desitter-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
