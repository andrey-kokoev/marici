"""Exact barycenter walks for all assembly orders of the existing tetrahedron.

Vertex insertion is a declared filtration of fixed source geometry, not a
newly implemented WG growth rule. No physical time is attached to stage index.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from collections import Counter
import json
from check_twelve_triangle_positive_geometry import POINTS, mean, dot, sub

ROOT=Path(__file__).resolve().parents[1]


def determinant(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def main():
    rows=[];walks=[]
    for order in permutations('ABCD'):
        centers=[mean([POINTS[v] for v in order[:n]]) for n in range(1,5)]
        steps=[sub(centers[i+1],centers[i]) for i in range(3)]
        assert centers[-1]==(F(0),)*3
        lengths=[dot(s,s) for s in steps]
        assert lengths==[F(2),F(2,3),F(1,3)]
        assert all(dot(steps[i],steps[j])==0 for i in range(3) for j in range(i+1,3))
        for n in range(1,4):
            # Retained stage count and consecutive centers recover the new
            # source vertex, whereas the final center alone does not.
            recovered=tuple((n+1)*centers[n][i]-n*centers[n-1][i] for i in range(3))
            assert recovered==POINTS[order[n]]
        volume=abs(determinant(*steps))/6
        assert volume==F(1,9)
        walks.append(tuple(centers))
        rows.append(dict(order=''.join(order),barycenters=[[str(x) for x in c] for c in centers],
                         displacement_vectors=[[str(x) for x in s] for s in steps],
                         squared_step_lengths=list(map(str,lengths)),
                         oriented_flag_volume=str(determinant(*steps)/6)))
    assert len(set(walks))==24 and len({w[-1] for w in walks})==1
    signs=Counter(r['oriented_flag_volume'] for r in rows)
    assert signs=={'1/9':12,'-1/9':12}
    assert 24*F(1,9)==F(8,3)
    first=rows[0];second=next(r for r in rows if r['order']=='ABDC')
    assert first['barycenters'][:2]==second['barycenters'][:2]
    assert first['barycenters'][2]!=second['barycenters'][2]
    assert first['barycenters'][3]==second['barycenters'][3]
    # Negative control: simplicial incidence alone does not force right angles.
    distorted=dict(POINTS);distorted['D']=(F(-1),F(-1),F(2))
    cs=[mean([distorted[v] for v in 'ABCD'[:n]]) for n in range(1,5)]
    ds=[sub(cs[i+1],cs[i]) for i in range(3)]
    distorted_dots=[dot(ds[i],ds[j]) for i in range(3) for j in range(i+1,3)]
    assert any(x!=0 for x in distorted_dots)
    result=dict(schema='marici.nima.barycenter-assembly-walk.v1',status='pass',
                source='regular tetrahedral coordinates in check_twelve_triangle_positive_geometry.py',
                orders_checked=24,distinct_walks=24,distinct_final_barycenters=1,
                squared_step_lengths=['2','2/3','1/3'],pairwise_step_dot_products=['0','0','0'],
                total_squared_displacement='3',flag_simplex_volume='1/9',total_flag_volume='8/3',
                recovery='x_(n+1)=(n+1)c_(n+1)-n*c_n; stage count retained',
                comparison=[first,second],all_orders=rows,
                nonregular_control=dict(changed_vertex=['-1','-1','2'],step_dot_products=list(map(str,distorted_dots))),
                disposition='All regular-tetrahedron barycenter flags have orthogonal successive displacements. The final center forgets order; the full indexed walk recovers the ordered vertices. This is geometry of regular flags, not a general simplicial orthogonality or eigenline theorem.')
    out=ROOT/'results/barycenter-assembly-walk.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='all_orders'},indent=2))


if __name__=='__main__':main()
