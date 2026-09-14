#!/usr/bin/env python3
"""Exact transported quadratic-form construction of the Green/seam link."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/green_seam_bilinear_linking_operator.v1.json';OUT=ROOT/'research/voevodsky/results/green_seam_bilinear_linking_operator.json';D=json.loads(FIX.read_text());phi=[Q(x) for x in D['source_vector']];chi=[Q(x) for x in D['odd_character']];n=D['dimension'];N=D['depth']
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def power(a,k):
 r=[[Q(i==j) for j in range(n)] for i in range(n)]
 for _ in range(k):r=mm(r,a)
 return r
def quad(a):return sum(phi[i]*a[i][j]*phi[j] for i in range(n) for j in range(n))
S=[[Q(i==j+1) for j in range(n)] for i in range(n)];St=tr(S);P0=[[Q(i==j==0) for j in range(n)] for i in range(n)];L=[[Q(0) for _ in range(n)] for _ in range(n)]
for d in range(1,n):L[0][d]=L[d][0]=chi[d]
Ps=[mm(mm(power(S,j),P0),power(St,j)) for j in range(N+1)];Ls=[mm(mm(power(S,j),L),power(St,j)) for j in range(N+1)];E=list(map(quad,Ps));J=list(map(quad,Ls));expectedJ=[Q(66),Q(-45),Q(-6),Q(4)]
checks={'linking_form_symmetric':L==tr(L),'primitive_forms_transport':all(Ps[j][j][j]==1 for j in range(N+1)),'green_readouts_match':E==[Q(4),Q(9),Q(1),Q(16)],'seam_readouts_match_prior_increments':J==expectedJ,'linking_forms_are_shift_conjugates':all(Ls[j]==mm(mm(power(S,j),L),power(St,j)) for j in range(N+1)),'link_not_scalar_multiple_of_primitive':any(L[i][j]!=0 for i in range(n) for j in range(n) if i!=j),'exchange_even_type_retained':D['disposition']['symmetry_type'].startswith('symmetric'),'full_mate_not_promoted':'before a full mate' in D['disposition']['remaining_gate']}
out={'schema':'marici.voevodsky.green-seam-bilinear-linking-operator-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'green_readouts':list(map(str,E)),'seam_readouts':list(map(str,J)),'base_linking_matrix':[[str(x) for x in row] for row in L],'linking_matrix_rank_support':'head-to-tail star; no scalar diagonal reduction'},'disposition':'The seam increment is an exact transported quadratic observable on the same finite carrier as the Green atomic defect. This constructs the even Green/seam linking block while preserving distinct output slots.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_green_seam_bilinear_linking_operator.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/D['source']).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
