#!/usr/bin/env python3
"""Identify the two-bit quotient with pairings of four split fibers."""
import json
from itertools import product
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
R=Path(__file__).resolve().parents[3]
# Primitive A1^3 coordinates from the previous saturation calculation.
d=[s.Matrix(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
D=s.Matrix.hstack(d[0],d[1],d[2])
SNF=smith_normal_form(D,domain=ZZ)
# Three primitive half-sums, associated to the three perfect matchings of four labels.
reps={'12|34':(d[0]+d[1])/2,'13|24':(d[0]+d[2])/2,'14|23':(d[0]+d[3])/2}
# Raw lattice criterion in this frame: all three coordinates have equal parity.
def raw(v): return int(v[0]-v[1])%2==0 and int(v[0]-v[2])%2==0
checks={'raw_index_four':abs(int(D.det()))==4,'smith_Z2_squared':[abs(int(SNF[i,i])) for i in range(3)]==[1,2,2],'differences_are_raw':all(raw(v) for v in d),'half_sums_integral':all(all(s.denom(x)==1 for x in v) for v in reps.values()),'half_sums_not_raw':all(not raw(v) for v in reps.values()),'three_nonzero_cosets_distinct':len({(int(v[0]-v[1])%2,int(v[0]-v[2])%2) for v in reps.values()})==3,'sum_three_is_raw':raw(sum(reps.values(),s.zeros(3,1))),'pairing_independent_of_complement':all(raw((d[i]+d[j])/2-(d[k]+d[l])/2) for (i,j,k,l) in [(0,1,2,3),(0,2,1,3),(0,3,1,2)])}
assert all(checks.values()),checks
syndromes={name:[int(v[0]-v[1])%2,int(v[0]-v[2])%2] for name,v in reps.items()}
out={'schema':'marici.voevodsky.bitangent-pairing-parity.v1','primitive_lattice':'A1^3 with coordinates Z^3','raw_difference_lattice':'vectors whose three coordinates have equal parity','raw_generator_matrix':D.tolist(),'smith_diagonal':[1,2,2],'quotient':'(Z/2)^2','zero_class':'unsaturated integer combinations of individual component differences d_i','nonzero_classes':{name:{'representative':[int(x) for x in reps[name]],'syndrome':syndromes[name]} for name in reps},'geometric_labels':'the three perfect matchings 12|34, 13|24, 14|23 of the four split fibers','checks':checks,'passed':True,'next':'use the based path from the physical infinity interval to determine which pairing of critical fibers its transported thimble realizes'}
# cast matrix
out['raw_generator_matrix']=[[int(x) for x in D.row(i)] for i in range(3)]
(R/'research/voevodsky/results/bitangent_pairing_parity.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'smith':out['smith_diagonal'],'quotient':out['quotient'],'nonzero_classes':out['nonzero_classes'],'next':out['next']}))
