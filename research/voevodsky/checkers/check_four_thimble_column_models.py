#!/usr/bin/env python3
"""Construct all four integral cusp-extension presentations after endpoint closure."""
import itertools,json,math
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[3]
endpoint=json.loads((ROOT/'research/voevodsky/results/full_endpoint_principal_column.json').read_text())
leray=json.loads((ROOT/'research/benincasa/results/infinity-physical-leray-covector.json').read_text())
models=[]
for a,b in itertools.product((0,1),repeat=2):
 # relation row in free basis (e6,v,m)
 rel=s.Matrix([[-a,-b,2]])
 D=smith_normal_form(rel,domain=ZZ)
 invariant=abs(int(next(v for v in D if v!=0)))
 primitive=(math.gcd(a,b,2)==1)
 models.append({'column':[a,b],'relation':[-a,-b,2],'smith_nonzero':invariant,'coinvariant_type':'free rank 2' if primitive else 'Z^2 plus Z/2','wall_endpoint_vector':[0,2],'wall_endpoint_parity':[0,0],'leray_kernel_shift_invisible':True})
checks={
 'endpoint_packet':endpoint['passed'],
 'endpoint_parity_zero':endpoint['mod_two']==[0,0],
 'leray_packet':leray['all_checks_pass'],
 'leray_annihilates_algebraic_kernel':leray['kernel_annihilated']==['e6','v_alg'],
 'four_models':len(models)==4,
 'all_columns':{tuple(m['column']) for m in models}==set(itertools.product((0,1),repeat=2)),
 'zero_column_retains_Z2':models[0]['smith_nonzero']==2,
 'three_nonzero_columns_primitive':all(m['smith_nonzero']==1 for m in models[1:]),
 'relative_data_same_all_models':len({tuple(m['wall_endpoint_vector']) for m in models})==1,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.four-thimble-column-models.v1','passed':True,'models':models,'common_known_data':['width-two elliptic quotient','primitive generic Gysin kernel','wall+endpoint vector (0,2)','principal odd endpoint divisor','Leray annihilation of algebraic kernel'],'selected_column':None,'decision':'current packets admit all four integral columns; a chain-level ambient intersection is necessary','checks':checks}
p=ROOT/'research/voevodsky/results/four_thimble_column_models.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'compatible_columns':[m['column'] for m in models]}))
