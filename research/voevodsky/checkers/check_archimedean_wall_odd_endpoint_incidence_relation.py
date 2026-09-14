#!/usr/bin/env python3
"""Exact endpoint-frame metric and reciprocal-parity audit."""
import hashlib,json,platform
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];FIX=ROOT/'research/voevodsky/fixtures/archimedean_wall_odd_endpoint_incidence_relation.v1.json';OUT=ROOT/'research/voevodsky/results/archimedean_wall_odd_endpoint_incidence_relation.json';D=json.loads(FIX.read_text());w=[Q(1,2),Q(1,2)];j=[Q(1,4),Q(-1,4)];R=[[Q(0),Q(1)],[Q(1),Q(0)]];C=[[w[0],j[0]],[w[1],j[1]]]
def mv(a,v):return [sum(a[i][k]*v[k] for k in range(len(v))) for i in range(len(a))]
def ip(u,v):return 2*sum(u[i]*v[i] for i in range(2))
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
checks={'wall_unit_energy':ip(w,w)==1,'odd_quarter_energy':ip(j,j)==Q(1,4),'wall_odd_orthogonal':ip(w,j)==0,'incidence_frame_nondegenerate':det(C)==Q(-1,4),'reciprocal_fixes_wall':mv(R,w)==w,'reciprocal_reverses_odd':mv(R,j)==[-x for x in j],'external_relation_not_bulk_map':'no ordinary L2 image' in D['relation_policy'],'homotopy_noninternalization_retained':D['disposition']['homotopy_incidence'].startswith('relational')}
out={'schema':'marici.voevodsky.archimedean-wall-odd-endpoint-incidence-relation-check.v1','passed':all(checks.values()),'checks':checks,'computed':{'incidence_matrix':[[str(x) for x in row] for row in C],'determinant':str(det(C)),'endpoint_Gram':[['1','0'],['0','1/4']],'reciprocal_wall':list(map(str,mv(R,w))),'reciprocal_odd':list(map(str,mv(R,j)))},'disposition':'The external archimedean wall and odd controls map nondegenerately to the reciprocal endpoint plane with exact parity. The homotopy-sector leg remains a boundary relation because the constant-delta orbit has no bulk L2 image.','claim_boundary':D['claim_boundary'],'execution_receipt':{'command':'python research/voevodsky/checkers/check_archimedean_wall_odd_endpoint_incidence_relation.py','python':platform.python_version(),'fixture_sha256':hashlib.sha256(FIX.read_bytes()).hexdigest(),'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in D['sources']},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
