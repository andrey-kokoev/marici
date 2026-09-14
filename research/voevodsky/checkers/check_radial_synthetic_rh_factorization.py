#!/usr/bin/env python3
"""Exact checks for the finite synthetic RH factorization."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/radial-synthetic-rh-factorization.v1.json'
RESULT=ROOT/'research/voevodsky/results/radial_synthetic_rh_factorization.json'
d=json.loads(CONTRACT.read_text()); z=s.symbols('z'); n=12
L=s.zeros(n)
for j in range(n): L[j,j]=2; L[j,(j-1)%n]=-1; L[j,(j+1)%n]=-1
K0=s.diag(s.eye(n)+L,s.eye(n)+L,2,2); Kz=K0-z*s.eye(26)
K0i=K0.inv(); V=s.simplify(Kz*K0i); Gp=V; Gm=s.eye(26)
D=s.factor(Kz.det()); D0=D.subs(z,0)
checks={}
checks['K0_invertible']=K0.det()!=0
checks['jump_reconstruction']=Gm.inv()*Gp==V
checks['inside_normalization']=Gp.subs(z,0)==s.eye(26)
checks['outside_normalization']=Gm==s.eye(26)
checks['jump_determinant_ratio']=s.factor(V.det()-D/D0)==0
roots=K0.eigenvals()
checks['contour_radius_separates_spectrum']=all(s.Abs(r)>s.Rational(1,2) for r in roots)
checks['winding_zero_by_no_internal_zeros_or_poles']=all(r>s.Rational(1,2) for r in roots) and D0!=0
# Green relation at exact interior and boundary sample points.
for label,a in [('inside',s.Rational(1,3)),('boundary_real',s.Rational(1,2)),('boundary_imag',s.I/2)]:
 H=(K0-a*s.eye(26)).inv()
 checks[f'green_jump_inverse_{label}']=s.simplify(V.subs(z,a).inv()-K0*H)==s.zeros(26)
# Symmetry and orientation.
checks['Real_polynomial_coefficients']=all(x.is_real for x in s.Poly(D,z).all_coeffs())
O=s.zeros(26)
for base in (0,12):
 for j in range(12): O[base+j,base+(-j)%12]=1
O[24,24]=1; O[25,25]=-1
checks['orientation_jump_commutation']=s.simplify(O*V-V*O)==s.zeros(26)
J=s.diag(*([1]*12+[-1]*12+[1,-1]))
checks['Real_sector_jump_commutation']=s.simplify(J*V-V*J)==s.zeros(26)
# Hostile contours/families.
checks['contour_through_first_zero_rejected']=D.subs(z,1)==0 and (K0-s.eye(26)).rank()<26
L0=s.diag(L,L,2,2)
checks['massless_origin_normalization_rejected']=L0.det()==0
checks['larger_radius_encloses_zeros']=any(r<s.Rational(3,2) for r in roots)
checks['not_source_RH']=d['status']=='synthetic_finite_matrix_RH_factorization_not_source_RH' and not d['claim_boundary']['Aspect_RH_identification']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.radial-synthetic-rh-factorization-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'contour_radius':'1/2','winding':0,'partial_indices':[0]*26,'disposition':{'constructed':'exact normalized finite matrix factorization V=G_minus^-1 G_plus','qualification':'exterior factor is identity and jump is inherited tautologically from the invertible pencil','remaining':'source identification or nontrivial source-derived jump'}}
RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'winding':0,'partial_indices':'all_zero'}))
raise SystemExit(0 if result['passed'] else 1)
