"""Exact two-order barycenter comparison; no inferred native WG realization."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import POINTS, mean, dot, sub, cross, det

ROOT=Path(__file__).resolve().parents[1]


def comparison(points, order):
    a,b,c,d=(points[v] for v in order)
    s=mean([a,b]);p=mean([a,b,c]);q=mean([a,b,d]);t=mean([a,b,c,d])
    relation=tuple(3*p[i]+3*q[i]-2*s[i]-4*t[i] for i in range(3))
    assert relation==(F(0),)*3
    volume6=det((sub(p,s),sub(q,s),sub(t,s)))
    assert volume6==0
    # Oriented quadrilateral s -> p -> t -> q -> s, as two triangles.
    u=cross(sub(p,s),sub(t,s));v=cross(sub(t,s),sub(q,s))
    area=tuple((u[i]+v[i])/2 for i in range(3))
    mup=mean([mean([s,p]),mean([p,t])])
    muq=mean([mean([s,q]),mean([q,t])])
    delta=sub(mup,muq)
    assert delta==tuple((p[i]-q[i])/2 for i in range(3))
    assert delta==tuple((c[i]-d[i])/6 for i in range(3))
    return dict(order=''.join(order),s=s,p=p,q=q,t=t,affine_relation=relation,
                determinant=volume6,oriented_area=area,area_squared=dot(area,area),
                expected_representatives=[mup,muq],representative_difference=delta,
                representative_difference_squared=dot(delta,delta))


def main():
    regular=[comparison(POINTS,order) for order in permutations('ABCD')]
    for r in regular:
        assert r['area_squared']==F(2,9)
        assert r['representative_difference_squared']==F(2,9)
        # Nonzero planar area and zero determinant give exact affine rank two.
        assert r['area_squared']>0
    lookup={r['order']:r for r in regular}
    for order,r in lookup.items():
        reverse=lookup[order[:2]+order[3]+order[2]]
        assert reverse['oriented_area']==tuple(-x for x in r['oriented_area'])
        assert reverse['representative_difference']==tuple(-x for x in r['representative_difference'])
    # Nonregular geometry still satisfies the universal affine dependency.
    skew=dict(POINTS);skew['D']=(F(-1),F(-1),F(2))
    distorted=[comparison(skew,order) for order in permutations('ABCD')]
    assert all(r['area_squared']>0 for r in distorted)
    # Algebraic identity works for any prefix cardinality n, not just an edge.
    for n in range(1,9):
        s=POINTS['A'];c=POINTS['C'];d=POINTS['D']
        p=tuple((n*s[i]+c[i])/(n+1) for i in range(3))
        q=tuple((n*s[i]+d[i])/(n+1) for i in range(3))
        t=tuple((n*s[i]+c[i]+d[i])/(n+2) for i in range(3))
        assert all((n+1)*(p[i]+q[i])-n*s[i]-(n+2)*t[i]==0 for i in range(3))
    # Off-plane perturbation is detected: the zero determinant is substantive,
    # but breaking barycentric provenance is not an authorized comparison.
    r=regular[0];normal=r['oriented_area']
    perturbed=tuple(r['q'][i]+normal[i] for i in range(3))
    control_det=det((sub(r['p'],r['s']),sub(perturbed,r['s']),sub(r['t'],r['s'])))
    assert control_det!=0
    result=dict(schema='marici.nima.barywalk-comparison.v1',status='pass',
                obligation='forward geometric realization; native-to-barycentric comparison map unavailable',
                regular_comparisons=regular,nonregular_comparisons=distorted,
                regular_affine_rank=2,regular_area_squared=F(2,9),
                general_identity='(n+1)(p+q)=n*s+(n+2)*t for two single-vertex extensions of an n-vertex prefix',
                off_plane_control_determinant=control_det,
                disposition='Two-order extension comparisons are necessarily planar. Oriented area and averaged-state difference survive, but volume cannot discriminate native fillability.',
                native_blind_test='not performed: no source-justified map from native terms, types and witnesses to these barycenters has been supplied')
    def encode(x):
        if isinstance(x,F):return str(x)
        if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
        if isinstance(x,(list,tuple)):return [encode(v) for v in x]
        return x
    result=encode(result)
    (ROOT/'results/barywalk-comparison.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('regular_comparisons','nonregular_comparisons')},indent=2))


if __name__=='__main__':main()
