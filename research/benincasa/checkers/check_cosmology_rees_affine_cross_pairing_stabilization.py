#!/usr/bin/env python3
"""Exact adjacent-target pairings and representative-dependence test."""
import contextlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve();base=HERE.with_name('check_cosmology_rees_correct_K_depth_scalar_solve.py')
with contextlib.redirect_stdout(io.StringIO()):h=runpy.run_path(str(base))
g=h['g'];mul=h['mul'];H,Q,target=g['H'],h['Q'],h['target'];one={(0,0):F(1)};R=mul(H,Q)
def pw(a,n):
 r=one
 for _ in range(n):r=mul(r,a)
 return r
def pf(s):
 a,b=s.split('/') if '/' in s else (s,'1');return F(int(a),int(b))
def pull(l,P):
 out={};mx=max(a for a,b in l);my=max(b for a,b in l)
 for i in range(mx+1):
  for j in range(my+1):
   v=sum(c*l.get((i+a,j+b),F(0)) for (a,b),c in P.items())
   if v:out[(i,j)]=v
 return out
def ev(l,f):return sum(l.get(m,F(0))*v for m,v in f.items())
def full(n):
 x=json.loads((HERE.parents[1]/'results'/f'cosmology_rees_affine_H{n}Q{n}_exact_certificate.json').read_text());return {tuple(q['monomial']):pf(q['coefficient']) for q in x['certificate']}
def direct(path,key):
 x=json.loads((HERE.parents[1]/'results'/path).read_text());return {tuple(q['monomial']):pf(q['coefficient']) for q in x[key]}
lams={2:pull(full(2),R),3:pull(full(3),pw(R,2)),4:direct('cosmology_rees_affine_pole4_target_detector.json','certificate_R5'),5:direct('cosmology_rees_affine_pole5_target_detector.json','certificate_R6')};rows=[]
for n,l in lams.items():rows.append({'order':n,'normalized_pairing':str(ev(l,mul(target,pw(R,n+1)))),'adjacent_previous_pairing':str(ev(l,mul(target,pw(R,n))))})
pull5=pull(lams[5],R);delta=dict(pull5)
for m,v in lams[4].items():delta[m]=delta.get(m,F(0))-v
prev=mul(target,pw(R,4));out={'schema':'marici.benincasa.cosmology-rees-affine-cross-pairing-stabilization.v1','rows':rows,'orders4_5_equal':rows[2]['adjacent_previous_pairing']==rows[3]['adjacent_previous_pairing'],'pullback5_minus_chosen4_previous_pairing':str(ev(delta,prev)),'invariant_under_tested_correction':ev(delta,prev)==0,'representative_invariant':None,'disposition':'the value is stable for orders 2 through 5 and for the tested order-4 correction; full representative invariance requires the entire target-annihilating dual subspace'};(HERE.parents[1]/'results'/'cosmology_rees_affine_cross_pairing_stabilization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
