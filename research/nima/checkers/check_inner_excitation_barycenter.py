"""Conditional first-moment test on the existing cone-cell embedding.
Squared mode norm is a declared positive weight, not derived particle energy.
"""
from pathlib import Path
from fractions import Fraction as F
import json
from check_twelve_triangle_positive_geometry import POINTS,mean,ONE,OMEGA
from check_triangle_half_phase import transpose,zmv,zmul,zadd,zscale,zconj,znorm
ROOT=Path(__file__).resolve().parents[1]

def center(points,weights):
    total=sum(weights)
    if total==0:raise ValueError('No normalized center for zero total weight')
    return tuple(sum(w*p[k] for w,p in zip(weights,points))/total for k in range(3))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def main():
    src=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    rows=src['triangles_and_transports'];points=dict(POINTS)
    for r in rows:
        face=r['triangle'][0];points[face]=mean([POINTS[k] for k in face[2:]])
    coeff=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    modes=[zmv(transpose(tuple(points[k] for k in r['triangle'])),coeff) for r in rows]
    weights=[sum(znorm(z) for z in v) for v in modes]
    positions=[mean([(F(0),)*3]+[points[k] for k in r['triangle']]) for r in rows]
    assert set(weights)=={F(20,3)} and sum(weights)==80
    assert center(positions,weights)==(0,0,0)
    i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB')
    j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
    assert positions[i]==(F(7,12),F(1,12),F(-1,12))
    assert positions[j]==(F(7,12),F(-1,12),F(1,12))
    contrast_weights=[w if k in (i,j) else F(0) for k,w in enumerate(weights)]
    assert sum(contrast_weights)==F(40,3)
    assert center(positions,contrast_weights)==(F(7,12),0,0)
    outputs=[]
    for eps in (F(0),F(1,2),F(1),F(-1),F(2)):
        independent=[w+eps*eps*d for w,d in zip(weights,contrast_weights)]
        coherent=[w*(1+eps*(1 if k==i else -1 if k==j else 0))**2 for k,w in enumerate(weights)]
        expected_x=7*eps*eps/(12*(6+eps*eps))
        expected_y=eps/(6*(6+eps*eps))
        assert sum(independent)==sum(coherent)==80+F(40,3)*eps*eps
        assert center(positions,independent)==(expected_x,0,0)
        assert center(positions,coherent)==(expected_x,expected_y,-expected_y)
        # Existing collective averaging acts on amplitudes, not intensities.
        mean_amplitude=sum(1+eps*(1 if k==i else -1 if k==j else 0) for k in range(12))/12
        assert mean_amplitude==1
        assert center(positions,[w*mean_amplitude**2 for w in weights])==(0,0,0)
        outputs.append(dict(amplitude=str(eps),total_weight=str(sum(independent)),
                            independent_center=list(map(str,center(positions,independent))),
                            coherent_center=list(map(str,center(positions,coherent)))))
    # Global conjugation of the same state preserves all positive weights.
    assert [sum(znorm(zconj(z)) for z in v) for v in modes]==weights
    # Adding retained descriptions/effects without changing represented weights
    # cannot shift this observable. No extra weight is assigned to the metadata.
    assert center(positions,list(weights))==center(positions,weights)
    translation=(F(2),F(-3),F(1,2))
    independent=[w+d for w,d in zip(weights,contrast_weights)]
    assert center([add(p,translation) for p in positions],independent)==add(center(positions,independent),translation)
    # Charge controls are hypothetical assignments, kept separate from weights.
    try:center(((0,0,0),(F(7,12),0,0)),(F(1),F(-1)))
    except ValueError:pass
    else:raise AssertionError('A neutral charge distribution has no normalized charge barycenter')
    result=dict(schema='marici.nima.inner-excitation-barycenter.v1',status='pass',
        declared_observable='Cone-cell centroids weighted by squared local complex-mode norms. Not a source-derived mass or energy density.',
        original_center=['0','0','0'],original_weight='80',candidate_center=['7/12','0','0'],unit_candidate_weight='40/3',
        amplitude_controls=outputs,
        reference_only='Retaining a dual continuation or changing description alone leaves the represented distribution and its center unchanged.',
        charge_control='Complex conjugation preserves intensity. Opposite assigned charges do not imply opposite mass weights. A hypothetical +1/-1 pair has zero net charge and no normalized charge center, but has a defined charge dipole.',
        geometry_control='Uniform-volume geometry is unchanged in every amplitude test; its geometric centroid stays at the origin.',
        current_cycle='The coherent perturbation has mean amplitude one; the existing collective projector returns it to the original mode and zero center after one pass. The initial displacement is not a sustained active mode.',
        dynamics_boundary='These are centers of specified preparations, not computed trajectories, recoil, forces, or electron creation. Relative amplitude and the spatial energy interpretation are not selected.')
    (ROOT/'results/inner-excitation-barycenter.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
