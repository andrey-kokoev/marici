import contextlib, io, json
from fractions import Fraction as F
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    from five_site_disjoint_region_pair_exact_survivor import I


def sqrt_i(value):
    import math
    assert value.lo>0
    lo=F(str(math.sqrt(float(value.lo))-1e-13));hi=F(str(math.sqrt(float(value.hi))+1e-13))
    assert lo*lo<=value.lo and hi*hi>=value.hi
    return I(lo,hi)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

s5=I(F(2236067,10**6),F(2236068,10**6))
c72=(s5-I(1))*I(F(1,4));c144=-(s5+I(1))*I(F(1,4))
s72=sqrt_i(I(10)+I(2)*s5)*I(F(1,4));s144=sqrt_i(I(10)-I(2)*s5)*I(F(1,4))
p=[(I(1),I(0),I(1)),(c72,s72,I(1)),(c144,s144,I(1)),(c144,-s144,I(1))]
c=[(I(0),I(0),I(0))]
for k in range(4):c.append(add(c[-1],p[k]))
d24=sub(c[4],c[2]);d13=sub(c[3],c[1]);offset=sub(c[1],c[2])
triple=dot(offset,cross(d24,d13))
assert not triple.lo<=0<=triple.hi

packet={
 'schema':'marici.five_site_region_pair_polar_soft_exclusion.v1',
 'owner_focal_segment':'[C_2,C_4] (and orientation reversals)',
 'other_focal_segment':'[C_1,C_3] (and orientation reversals)',
 'equal_focal_lengths':'|C_2-C_4|=|C_1-C_3| by cyclic regular-pentagon geometry',
 'polar_wall_condition':'for ell in [C_2,C_4], |ell-C_1|+|ell-C_3|=|C_2-C_4|',
 'triangle_equality_requirement':'ell must also lie in [C_1,C_3]',
 'supporting_line_scalar_triple_interval':[str(triple.lo),str(triple.hi)],
 'segments_disjoint_certified':True,
 'polar_collision_count_on_homogeneous_slice':0,
 'all_four_active_soft_orientations_excluded':True,
 'classification':'polar Morse-Bott coefficient is a valid boundary type but is not activated on the frozen homogeneous slice',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-polar-soft-exclusion.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('supporting_line_scalar_triple_interval','segments_disjoint_certified','polar_collision_count_on_homogeneous_slice','new_carrier_datum')},sort_keys=True))
