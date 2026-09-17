#!/usr/bin/env python3
"""Exact phase-preserving reduction of the globally sewn theta transform."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[1]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
ROOT=Path(__file__).resolve().parents[2];a,b=s.symbols('a b',real=True);X,Y,U,V=s.symbols('X Y U V',real=True);Z=X+s.I*Y;Zp=U+s.I*V
prod=s.expand_complex(Zp*s.conjugate(Z));re=s.re(prod).expand();im=s.im(prod).expand();checks={'real_product_formula':s.simplify(re-(X*U+Y*V))==0,'imag_product_formula':s.simplify(im-(X*V-Y*U))==0}
# Cauchy-Riemann: U=X_a=Y_b and V=Y_a=-X_b.
Xa,Ya,Xb,Yb=s.symbols('Xa Ya Xb Yb',real=True);re_cr=(X*Xa+Y*Ya);im_cr=(X*Ya-Y*Xa);norm_a=2*(X*Xa+Y*Ya);norm_b=2*(X*Xb+Y*Yb);subs={Xb:-Ya,Yb:Xa};checks.update({'real_is_half_a_derivative':s.simplify(re_cr-norm_a/2)==0,'imag_is_minus_half_b_derivative':s.simplify(im_cr+norm_b.subs(subs)/2)==0})
out={'schema':'marici.nima.theta-completed-phase-preserving-representation.v1','identities':{'Re(Zprime conjugate Z)':'(1/2) partial_a |Z|^2','Im(Zprime conjugate Z)':'-(1/2) partial_b |Z|^2','Q_alpha_beta':'beta partial_a |Z|^2 - alpha partial_b |Z|^2'},'checks':checks,'passed':all(checks.values()),'source_interpretation':'after full modular resummation, the two-copy form is the directional derivative of the squared modulus of one completed transform','remaining_sign_gate':'prove the required directional monotonicity of |Z(a+ib)|^2 on the admitted source domain','claim_boundary':'exact factorization only; no directional sign is inferred','rh_proved':False};p=ROOT/'research/nima/results/theta-completed-phase-preserving-representation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
