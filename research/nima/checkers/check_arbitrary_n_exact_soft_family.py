#!/usr/bin/env python3
"""Exact momentum-conserving celestial soft family with nonzero hard limit."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
eps=s.symbols('epsilon', real=True)
def row(n):
 z=[s.Integer(i) for i in range(n)];zs=z[0];hard=z[1:];base=[]
 for i,a in enumerate(hard):base.append(s.factor(1/s.prod(a-b for j,b in enumerate(hard) if i!=j)))
 V=s.Matrix([[hard[j]**k for j in range(3)] for k in range(3)]);rhs=-s.Matrix([zs**k for k in range(3)]);corr=list(V.inv()*rhs)
 w=[eps]+[s.factor(base[j]+(eps*corr[j] if j<3 else 0)) for j in range(n-1)]
 moments=[s.factor(sum(w[i]*z[i]**k for i in range(n))) for k in range(3)]
 hardlimits=[s.factor(x.subs(eps,0)) for x in w[1:]]
 return {'n':n,'soft_coordinate':str(w[0]),'hard_limit_nonzero':all(x!=0 for x in hardlimits),'momentum_moments':[str(x) for x in moments],'momentum_conserved_identically':moments==[0,0,0],'soft_leg_vanishes':w[0].subs(eps,0)==0,'hard_limit_conserved':all(s.factor(sum(hardlimits[i]*hard[i]**k for i in range(n-1)))==0 for k in range(3))}
rows=[row(n) for n in range(5,13)]
checks={'soft_leg_is_exact_epsilon':all(r['soft_leg_vanishes'] for r in rows),'momentum_conserved_for_all_epsilon':all(r['momentum_conserved_identically'] for r in rows),'hard_limit_nonzero_and_conserved':all(r['hard_limit_nonzero'] and r['hard_limit_conserved'] for r in rows)}
out={'schema':'marici.nima.arbitrary-n-exact-soft-family.v1','construction':'Start from barycentric momentum-conserving weights on n-1 hard real celestial points. Add a soft leg of signed energy epsilon and solve a 3x3 Vandermonde correction on three hard energies.','rows':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'For every finite n>=5 there is an exact real celestial family with momentum conservation identically in epsilon, one leg vanishing at epsilon=0, and a nonzero conserved hard limit.','remaining_map_data':['helicity and polarization assignment','normalization from momentum eigenstates to Bondi shear/news modes','radiative symplectic pairing','soft-factor action on the NNMHV component','cluster-edge degree-one map'],'claim_boundary':'epsilon is a soft-frequency deformation coordinate by explicit construction, not physical time.'};p=ROOT/'research/nima/results/arbitrary-n-exact-soft-family.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'construction':out['construction'],'checks':checks,'conclusion':out['conclusion'],'remaining_map_data':out['remaining_map_data'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
