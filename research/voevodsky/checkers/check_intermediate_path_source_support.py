"""A source edit can invalidate a proof path despite valid identical endpoints."""
from fractions import Fraction as Q
from pathlib import Path
import json
names=('x-low','x-high','y-low','y-high');rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
start=(Q(1),Q(2),Q(0),Q(0));middle=(Q(0),Q(1),Q(1),Q(1));end=start
k=tuple(middle[i]-start[i] for i in range(4));assert k==(-1,-1,1,1)
def support(p):return {names[i] for i,x in enumerate(p) if x!=0}
def valid(p,r):return min(p)>=0 and tuple(sum(r[i][0][j]*p[i] for i in range(4)) for j in (0,1))==(1,0) and sum(r[i][1]*p[i] for i in range(4))==2
def zero_kernel(v,r):return tuple(sum(r[i][0][j]*v[i] for i in range(4)) for j in (0,1))==(0,0) and sum(r[i][1]*v[i] for i in range(4))==0
assert all(valid(p,rows) for p in (start,middle,end)) and zero_kernel(k,rows)
path_support=support(start)|support(middle)|support(end)|support(k)
assert path_support==set(names) and support(start)=={'x-low','x-high'}
changed=list(rows);changed[3]=(changed[3][0],Q(2))
assert valid(start,changed) and valid(end,changed)
assert not valid(middle,changed) and not zero_kernel(k,changed)
# Endpoint-only cache says retain; typed path checker must reject.
def check_path(r):
 if not all(valid(p,r) for p in (start,middle,end)):return 'INVALID_INTERMEDIATE_PROOF'
 if not zero_kernel(k,r):return 'INVALID_COMPARISON_EDGE'
 return 'VALID_MATHEMATICAL_PATH'
assert check_path(rows)=='VALID_MATHEMATICAL_PATH'
assert check_path(changed)=='INVALID_INTERMEDIATE_PROOF'
report={'passed':True,'endpoint_proofs_valid_after_y_high_edit':True,'intermediate_proof_invalid_after_y_high_edit':True,'old_zero_bound_syzygy_invalid_after_edit':True,'endpoint_support':sorted(support(start)),'path_support':sorted(path_support),'scope':'Fixed square source and mathematical two-edge loop, not a declared Farkas higher cell or authorized historical event. Evidence cache must include edge and intermediate dependencies.'}
out=Path(__file__).resolve().parents[1]/'results/intermediate-path-source-support.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
