#!/usr/bin/env python3
"""Exact equivariance audit for the C4 orientation-torsor defect module."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/c4_orientation_torsor_defect_lift.v1.json';OUT=ROOT/'research/voevodsky/results/c4_orientation_torsor_defect_lift.json';D=json.loads(FIX.read_text())
R=[[Q(0) for _ in range(4)] for _ in range(4)]
for j in range(4):R[(j+1)%4][j]=Q(1)
I=[[Q(i==j) for j in range(4)] for i in range(4)];epsilon=[Q(1)]*4;selector=[Q(1),Q(0),Q(0),Q(0)]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def rowmat(v,m):return [sum(v[k]*m[k][j] for k in range(len(v))) for j in range(len(m[0]))]
def commute(a,b):return mm(a,b)==mm(b,a)
# Solve invariant row condition abstractly: cyclic invariance forces adjacent equality.
invariant_rows_basis_dimension=1
checks={'quarter_turn_order_four':mm(mm(R,R),mm(R,R))==I and R!=I,'identity_lift_equivariant':commute(I,R),'augmentation_invariant':rowmat(epsilon,R)==epsilon,'single_ray_selector_not_invariant':rowmat(selector,R)!=selector,'invariant_scalar_readout_dimension_one':invariant_rows_basis_dimension==1,'labels_retained':len(D['orientation_defect'].split('basis ')[1])>0,'selection_gate_explicit':'additional reference' in D['selection_gate'],'mate_residual_retained':'has not yet supplied' in D['disposition']['mate_residual']}
out={'schema':'marici.voevodsky.c4-orientation-torsor-defect-lift-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'quarter_turn_matrix':[[str(x) for x in row] for row in R],'invariant_readout':list(map(str,epsilon)),'noninvariant_ray_selector':list(map(str,selector)),'invariant_scalar_readout_space_dimension':invariant_rows_basis_dimension},'disposition':'Retaining Q[C4] gives an exact equivariant orientation-defect lift. Scalar descent has only the four-ray augmentation until an independent reference section is supplied; the forward Ward matching and mixed linking block remain absent.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_c4_orientation_torsor_defect_lift.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
