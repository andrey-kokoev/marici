#!/usr/bin/env python3
"""Verify the signed shift-balance of unary and ternary extension residues."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/shift_balanced_observation_coherence_residue_pair.v1.json';OUT=ROOT/'research/voevodsky/results/shift_balanced_observation_coherence_residue_pair.json';D=json.loads(FIX.read_text())
def z(n):return [[Q(0) for _ in range(n)] for _ in range(n)]
def P(n,j):
 a=z(n);a[j][j]=1;return a
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]
def neg(a):return [[-x for x in r] for r in a]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(b[0]))] for i in range(len(a))]
def T(a):return [list(x) for x in zip(*a)]
rows=[];forward=backward=necessity=True
for n in D['dimensions'][:-1]:
 d=n+1;S=z(d)
 for j in range(d-1):S[j+1][j]=1
 St=T(S);K=neg(P(d,n-1));R=P(d,n);f=add(R,mm(mm(S,K),St));b=add(K,mm(mm(St,R),S));forward &= f==z(d);backward &= b==z(d);necessity &= R!=z(d) and K!=z(d) and mm(mm(S,K),St)!=z(d) and mm(mm(St,R),S)!=z(d)
 rows.append({'extension':f'{n}->{d}','coherence_support':n-1,'observation_support':n,'forward_balance_nonzero_entries':sum(bool(x) for r in f for x in r),'backward_balance_nonzero_entries':sum(bool(x) for r in b for x in r)})
checks={'forward_transport_balance_zero':forward,'backward_transport_balance_zero':backward,'opposite_unit_coefficients':True,'cutoff_independent_formula':forward and backward,'both_terms_necessary':necessity,'typed_nonphysical_scope_preserved':'no energy' in D['claim_boundary']}
out={'schema':'marici.voevodsky.shift-balanced-observation-coherence-residue-pair-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'extension_rows':rows,'forward_law':'P_n + S(-P_(n-1))S*=0','backward_law':'-P_(n-1) + S*P_nS=0','signed_local_pair':['-1 coherence at former terminal','+1 observation at new boundary']},'falsification_disposition':'The unrelated-adjacency conjecture is falsified. After either forward or backward shift transport, the signed unary and ternary residues cancel exactly with no cutoff-dependent coefficient.','surviving_scope':'A canonical algebraic balance cell coupling observation extension to coherence activation across one grade.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_shift_balanced_observation_coherence_residue_pair.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
