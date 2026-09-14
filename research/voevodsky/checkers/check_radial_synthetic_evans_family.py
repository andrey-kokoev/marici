#!/usr/bin/env python3
"""Exact symbolic checks for the finite synthetic Evans family."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-synthetic-evans-family.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_synthetic_evans_family.json'
d=json.loads(CONTRACT.read_text()); lam=s.symbols('lambda'); n=12
L=s.zeros(n)
for j in range(n):
 L[j,j]=2; L[j,(j-1)%n]=-1; L[j,(j+1)%n]=-1
A=s.eye(n)+L
K=s.diag(A,A,2,2); pencil=K-lam*s.eye(26)
D=s.factor(pencil.det()); poly=s.Poly(D,lam)
bulk_char=s.factor((A-lam*s.eye(n)).det())
expected=s.factor((2-lam)**2*bulk_char**2)
checks={}
checks['degree_26']=poly.degree()==26
checks['monic_degree_26']=poly.LC()==1
checks['block_product_formula']=s.expand(D-expected)==0
checks['D_zero_iff_rank_loss_on_exact_roots']=all((K-r*s.eye(26)).rank()<26 for r in set(K.eigenvals()))
checks['all_spectrum_positive_real']=all(v.is_real and v>0 for v in K.eigenvals())
def root_multiplicity(f,root):
 m=0
 while s.simplify(f.subs(lam,root))==0:
  m+=1; f=s.diff(f,lam)
 return m
checks['D_zero_multiplicity_matches_eigenspace_algebraic_data']=all(root_multiplicity(D,v)==m for v,m in K.eigenvals().items())
# Resolvent test away from spectrum.
z=s.Rational(1,2); Hz=(K-z*s.eye(26)).inv()
checks['green_two_sided_inverse_off_zero_set']=(K-z*s.eye(26))*Hz==s.eye(26) and Hz*(K-z*s.eye(26))==s.eye(26)
# Real and orientation symmetries reduce to real coefficients and commutation.
checks['Real_Evans_symmetry']=all(c.is_real for c in poly.all_coeffs())
O=s.zeros(26)
for base in (0,12):
 for j in range(12): O[base+j,base+(-j)%12]=1
O[24,24]=1; O[25,25]=-1
checks['orientation_commutation']=O*K==K*O
J=s.diag(*([1]*12+[-1]*12+[1,-1]))
checks['Real_sector_commutation']=J*K==K*J
# Hostile checks.
K0=s.diag(L,L,2,2)
checks['massless_zero_multiplicity_two']=root_multiplicity(s.factor((K0-lam*s.eye(26)).det()),0)==2
checks['resolvent_refused_at_zero']=D.subs(lam,1)==0 and (K-s.eye(26)).rank()<26
bad=K.copy(); bad[0,12]=1
checks['opposite_Real_parity_coupling_rejected']=J*bad!=bad*J
checks['not_source_Evans_binding']=d['status']=='finite_dimensional_synthetic_evans_not_source_RH' and not d['claim_boundary']['Aspect_Evans_identification']
checks={k:bool(v) for k,v in checks.items()}
roots={str(v):int(m) for v,m in sorted(K.eigenvals().items(),key=lambda x:float(x[0]))}
result={'schema':'marici.voevodsky.radial-synthetic-evans-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'evans_polynomial':str(D),'distinct_eigenvalues_with_multiplicity':roots,'disposition':{'constructed':'entire finite matrix pencil, exact Evans polynomial, and meromorphic Green resolvent','remaining':'no Fredholm, source Evans, physical spectrum, or RH claim','next':'synthetic_RH_jump_factorization'}}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'degree':poly.degree(),'distinct_zeros':len(roots)}))
raise SystemExit(0 if result['passed'] else 1)
