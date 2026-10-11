"""Test an interface-supported mode under the existing three-stage projector.
Uses source local eigenvectors and rotations; no new binding Hamiltonian.
"""
from pathlib import Path
from fractions import Fraction as F
import json
from check_twelve_triangle_positive_geometry import POINTS,mean,ONE,OMEGA,ZERO,projector
from check_triangle_half_phase import transpose,mm,zadd,zmul,zscale,zconj,znorm,zmv,zmm,zreal
ROOT=Path(__file__).resolve().parents[1]

def apply(m,v):return tuple(row[0] for row in zmm(m,tuple((x,) for x in v)))
def norm(v):return sum(znorm(z) for z in v)
def inner(a,b):
    out=ZERO
    for x,y in zip(a,b):out=zadd(out,zmul(zconj(x),y))
    return out

def main():
    src=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())
    rows=src['triangles_and_transports'];points=dict(POINTS)
    for r in rows:
        label=r['triangle'][0]
        points[label]=mean([POINTS[k] for k in label[2:]])
    coeff=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    vectors=[zmv(transpose(tuple(points[k] for k in r['triangle'])),coeff) for r in rows]
    rotations=[tuple(tuple(F(x) for x in row) for row in r['rotation']) for r in rows]
    blocks=[[mm(R,transpose(S)) for S in rotations] for R in rotations]
    symmetry=zreal(tuple(tuple(blocks[i//3][j//3][i%3][j%3]/12 for j in range(36)) for i in range(36)))
    ps=[projector(v) for v in vectors]
    local=tuple(tuple(ps[i//3][i%3][j%3] if i//3==j//3 else ZERO for j in range(36)) for i in range(36))
    u=tuple(z for v in vectors for z in v);P=projector(u)
    assert norm(u)==80 and zmm(symmetry,local)==P
    assert zmm(P,zmm(symmetry,local))==P
    i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB')
    j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
    def seed(sign):return tuple(zscale(z,1 if k==i else sign if k==j else 0) for k,v in enumerate(vectors) for z in v)
    odd=seed(-1);even=seed(1)
    assert norm(odd)==norm(even)==F(40,3)
    assert apply(local,odd)==odd and apply(local,even)==even
    assert inner(u,odd)==ZERO
    assert apply(symmetry,odd)==apply(P,odd)==(ZERO,)*36
    out=apply(P,even)
    assert out==tuple(zscale(z,F(1,6)) for z in u)
    assert norm(out)/norm(even)==F(1,6)
    assert all(norm(out[3*k:3*k+3])>0 for k in range(12))
    assert apply(P,out)==out
    assert apply(P,u)==u and apply(P,(ZERO,)*36)==(ZERO,)*36
    for epsilon in (F(1,3),F(1),F(2)):
        perturbed=tuple(zadd(a,zscale(b,epsilon)) for a,b in zip(u,odd))
        assert apply(P,perturbed)==u
    # Lossless readout separation: the invisible residual is retained exactly.
    residual=tuple(zadd(a,zscale(b,-1)) for a,b in zip(even,out))
    assert apply(P,residual)==(ZERO,)*36
    assert norm(even)==norm(out)+norm(residual)
    # Existing same-slot residual composition is a DISTINCT operation. A
    # scalar coefficient control checks its capacity to read this hidden mode,
    # not admission of that operation as the geometric dynamics.
    amplitudes=[F(1) if k==i else F(-1) if k==j else F(0) for k in range(12)]
    assert sum(amplitudes)==0
    covariance=sum(a*a for a in amplitudes)/12
    composed=[2*a+a*a for a in amplitudes]
    assert sum(composed)/12==covariance==F(1,6)
    result=dict(schema='marici.nima.inner-face-localized-mode.v1',status='pass',
        support=[rows[i]['triangle'],rows[j]['triangle']],
        source_operator='P_collective P_symmetry P_local=P_collective=u u_dagger/80',
        opposite_phase={'local_selection':'preserved','collective_readout':'zero','initial_squared_norm':'40/3'},
        in_phase={'output':'u/6','retained_squared_norm_fraction':'1/6','occupied_output_blocks':12,'localized':False},
        localization_theorem='Every nonzero-eigenvalue eigenvector of this rank-one cycle lies in span(u), which occupies all twelve blocks. Hence no nonzero persistent cycle eigenmode is confined to the selected two blocks.',
        birth_control='P(u)=u, P(0)=0 and P(u+epsilon*contrast)=u: the current cycle neither nucleates nor amplifies this interface contrast.',
        retention='Zero collective readout is not erasure of the retained source. The exact residual decomposition retains the mode without asserting a new feedback law.',
        separate_response_control={'zero_first_mean':True,'same_slot_self_composition_mean':'1/6','independent_context_composition_mean':'0'},
        boundary='The same-slot nonlinear response is a prior conditional operation, not the existing geometric cycle. Its incidence/physical binding remains to be selected. The amplitude normalization is a trial input, not an electron mass.',
        conclusion='A nontrivial hidden interface contrast exists, but the current collective cycle does not support it as a localized persistent excitation.')
    (ROOT/'results/inner-face-localized-mode.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
