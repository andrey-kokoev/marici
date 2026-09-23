"""Signed comparison commutes with validated positive row presentation transport."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
source=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
perm=(3,0,2,1);scale=(Q(2),Q(3),Q(1,2),Q(4))
dest=tuple((tuple(s*Q(v) for v in source[i][0]),s*Q(source[i][1])) for i,s in zip(perm,scale))
A=((Q(0),Q(1),Q(0),Q(1)),Q(1));B=((Q(1),Q(2),Q(0),Q(1)),Q(0));C=((Q(0),Q(1),Q(1),Q(2)),Q(0))
def digest(rows):return sha256(repr(rows).encode()).hexdigest()
def transport(packet,src,dst,src_hash,dst_hash,order,factors):
 if src_hash!=digest(src) or dst_hash!=digest(dst):raise ValueError('STALE_MANIFEST')
 if sorted(order)!=list(range(len(src))) or len(factors)!=len(src) or any(s<=0 for s in factors):raise ValueError('BAD_ROW_WITNESS')
 if tuple((tuple(factors[j]*Q(v) for v in src[i][0]),factors[j]*Q(src[i][1])) for j,i in enumerate(order))!=dst:raise ValueError('BAD_ROW_WITNESS')
 m,c=packet
 return tuple(m[i]/factors[j] for j,i in enumerate(order)),c
def delta(x,y):return tuple(y[0][i]-x[0][i] for i in range(4)),y[1]-x[1]
src_hash=digest(source);dst_hash=digest(dest)
for x,y in ((A,B),(B,C),(A,C)):
 tx=transport(x,source,dest,src_hash,dst_hash,perm,scale)
 ty=transport(y,source,dest,src_hash,dst_hash,perm,scale)
 assert delta(tx,ty)==transport(delta(x,y),source,dest,src_hash,dst_hash,perm,scale)
try:transport(A,source,dest,src_hash,'stale',perm,scale)
except ValueError as err:assert str(err)=='STALE_MANIFEST'
else:raise AssertionError('stale manifest accepted')
for order,factors in ((perm,(Q(-2),)+scale[1:]),((0,1,2,3),scale)):
 try:transport(A,source,dest,src_hash,dst_hash,order,factors)
 except ValueError as err:assert str(err)=='BAD_ROW_WITNESS'
 else:raise AssertionError('invalid witness accepted')
report={'passed':True,'signed_comparison_squares':3,'surplus_fixed_under_row_witness':True,'stale_manifest_refused':True,'negative_scale_and_wrong_permutation_refused':True,'source_digest':src_hash,'destination_digest':dst_hash,'scope':'Exact mathematical witness-transported packet comparisons, not source issuer token transfer, history 2-cell, or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/comparison-row-witness-square.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
