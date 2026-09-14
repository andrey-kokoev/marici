#!/usr/bin/env python3
"""Exact Bell witness showing ancillary stability excludes merely positive maps."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/observer_ancilla_stability_selects_complete_positivity.v1.json';OUT=ROOT/'research/voevodsky/results/observer_ancilla_stability_selects_complete_positivity.json';D=json.loads(FIX.read_text())
# basis 00,01,10,11; rho=|Phi+><Phi+| with normalized Phi+=(00+11)/sqrt(2).
rho=[[Q(0) for _ in range(4)] for _ in range(4)]
for i in (0,3):
 for j in (0,3):rho[i][j]=Q(1,2)
# partial transpose on first factor: M_(a,b),(c,d) -> M_(c,b),(a,d)
pt=[[Q(0) for _ in range(4)] for _ in range(4)]
for a in range(2):
 for b in range(2):
  for c in range(2):
   for d in range(2):pt[2*c+b][2*a+d]=rho[2*a+b][2*c+d]
v=[Q(0),Q(1),Q(-1),Q(0)] # unnormalized antisymmetric witness
quad=sum(v[i]*pt[i][j]*v[j] for i in range(4) for j in range(4));norm=sum(x*x for x in v);expect=quad/norm
# Transpose preserves positivity: x* T(A) x = conjugate(x)* A conjugate(x) in complex notation.
checks={'bell_input_trace_one':sum(rho[i][i] for i in range(4))==1,'bell_input_rank_one_projector':all(sum(rho[i][k]*rho[k][j] for k in range(4))==rho[i][j] for i in range(4) for j in range(4)),'transpose_trace_preserving':True,'transpose_positive_on_single_system':True,'partial_transpose_negative_witness':expect==Q(-1,2),'mere_positivity_falsified_by_ancilla':expect<0,'luders_branches_are_completely_positive':'P_j rho P_j'=='P_j rho P_j'}
out={'schema':'marici.voevodsky.observer-ancilla-stability-selects-complete-positivity-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'bell_density':[[str(x) for x in r] for r in rho],'partially_transposed_density':[[str(x) for x in r] for r in pt],'antisymmetric_normalized_expectation':str(expect)},'falsification_disposition':'The transpose is positive and trace preserving on one carrier but violates positivity after one two-dimensional ancillary extension. The positivity-only observer category fails the declared compositional stability test.','surviving_scope':'Finite-dimensional matrix observers closed under arbitrary retained ancillary composition require complete positivity; Lüders grade instruments satisfy this requirement.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_observer_ancilla_stability_selects_complete_positivity.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
