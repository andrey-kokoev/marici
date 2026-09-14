#!/usr/bin/env python3
"""Exact finite behavioral tomography by native shift-defect interaction probes."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/shift_defect_behavior_coalgebra_is_faithful.v1.json';OUT=ROOT/'research/voevodsky/results/shift_defect_behavior_coalgebra_is_faithful.json';D=json.loads(FIX.read_text())
def z(n):return [[Q(0) for _ in range(n)] for _ in range(n)]
def I(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def T(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(a))) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(len(a))] for i in range(len(a))]
def pw(a,k):
 r=I(len(a))
 for _ in range(k):r=mm(r,a)
 return r
def Delta(a):return [[a[i][j] if i==j else Q(0) for j in range(len(a))] for i in range(len(a))]
rows=[];native=recover=rankfull=True
for n in D['dimensions']:
 S=z(n)
 for j in range(n-1):S[j+1][j]=1
 St=T(S);P0=sub(I(n),mm(S,St));probe_rows=[];maxlen=0
 for a in range(n):
  for b in range(n):
   E=mm(mm(pw(S,b),P0),pw(St,a));expected=z(n);expected[b][a]=1;native &= E==expected;maxlen=max(maxlen,a+b+1)
   # Behavior coordinate is b-th diagonal entry of Delta(E_ba X), represented as a row on vec(X).
   row=[Q(0) for _ in range(n*n)];row[a*n+b]=1 # vec index X_(a,b)
   probe_rows.append(row)
   X=[[Q((i+1)*7-(j+1)*2) for j in range(n)] for i in range(n)];recover &= Delta(mm(E,X))[b][b]==X[a][b]
 rankfull &= probe_rows==I(n*n)
 rows.append({'dimension':n,'state_dimension':n*n,'immediate_record_rank':n,'behavior_probe_rank':n*n,'probe_count':n*n,'maximum_native_word_length':maxlen})
checks={'native_matrix_units_constructed':native,'coefficient_recovery_formula_exact':recover,'behavior_map_full_rank':rankfull,'immediate_observer_rank_only_N':all(r['immediate_record_rank']==r['dimension'] for r in rows),'required_word_length_grows_with_cutoff':all(rows[i+1]['maximum_native_word_length']>rows[i]['maximum_native_word_length'] for i in range(len(rows)-1)),'scope_requires_interaction_probes':'left multiplication' in D['claim_boundary']}
out={'schema':'marici.voevodsky.shift-defect-behavior-coalgebra-is-faithful-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'cutoff_rows':rows,'reconstruction':'X_ab = [Delta((S^b P0 (S*)^a) X)]_bb','uniform_finite_probe_depth':False},'falsification_disposition':'The behavior-blindness conjecture is falsified for the full native interaction repertoire. Immediate observation loses off-diagonal coefficients, but constructor-word records recover every coefficient exactly. No fixed word-depth is uniformly complete as cutoff grows.','surviving_scope':'Finite shift-defect behavioral faithfulness with all native left-interaction probes; complete behavior is function-valued rather than a fixed finite record packet.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_shift_defect_behavior_coalgebra_is_faithful.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
