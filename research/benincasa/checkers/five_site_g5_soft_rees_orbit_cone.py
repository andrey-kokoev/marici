import json
from pathlib import Path

n=5
I=[[int(i==j) for j in range(n)] for i in range(n)]
S=[[int(i==(j+1)%n) for j in range(n)] for i in range(n)]

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def rank(a):
    a=[r[:] for r in a]; out=0
    for c in range(len(a[0])):
        p=next((i for i in range(out,len(a)) if a[i][c]),None)
        if p is None:continue
        a[out],a[p]=a[p],a[out]
        pv=a[out][c]
        for i in range(len(a)):
            if i!=out and a[i][c]:
                q=a[i][c];a[i]=[pv*x-q*y for x,y in zip(a[i],a[out])]
        out+=1
    return out

# A common nonzero source unit is suppressed; it cannot change the cone.
sp=I
assert mm(S,sp)==mm(sp,S)
assert rank(sp)==n
packet={
 'schema':'marici.five_site_g5_soft_rees_orbit_cone.v1',
 'source_character':[5,0,0,0,0],
 'target_character':[5,0,0,0,0],
 'specialization_matrix_after_common_unit':sp,
 'specialization_rank':rank(sp),
 'cyclic_equivariant':True,
 'kernel_dimension':0,
 'cokernel_dimension':0,
 'mapping_cone_homology_dimension':0,
 'classification':'the first-soft-Rees orbit is the specialization of the generic logarithmic orbit, with no supported excess',
}
Path('research/benincasa/results/five-site-g5-soft-rees-orbit-cone.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
