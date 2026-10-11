"""Source baseline and conditional two-orbit intertwiner controls."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from check_twelve_triangle_positive_geometry import POINTS,mean,ONE,OMEGA,projector
from check_triangle_half_phase import transpose,zmv,zmul,zconj,zadd,zscale,znorm
from check_phase_memory_first_moment import step
ROOT=Path(__file__).resolve().parents[1]

def inner(a,b):
    out=(F(0),F(0))
    for x,y in zip(a,b):out=zadd(out,zmul(zconj(x),y))
    return out

def main():
    src=ROOT/'agda/NativeFeedbackFixedPointBridge.agda'
    receipt=json.loads((ROOT/'results/agda-NativeFeedbackFixedPointBridge.json').read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
    assert receipt['source_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
    rows=json.loads((ROOT/'results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']
    pts=dict(POINTS)
    for row in rows:
        f=row['triangle'][0];pts[f]=mean([POINTS[k] for k in f[2:]])
    coeff=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    vs=[zmv(transpose(tuple(pts[k] for k in row['triangle'])),coeff) for row in rows]
    transported=[]
    for row,v in zip(rows,vs):
        R=tuple(tuple(F(a) for a in r) for r in row['rotation'])
        transported.append(zmv(transpose(R),v))
    assert all(v==transported[0] for v in transported)
    v0=transported[0];norm=sum(znorm(z) for z in v0)
    amplitudes=tuple(zscale(inner(v0,v),1/norm) for v in transported)
    assert amplitudes==(ONE,)*12
    u=(F(1),)*12;zero=(F(0),)*12
    assert step(u,zero)==(u,zero)
    i=next(k for k,r in enumerate(rows) if r['outer_arrow']=='AB');j=next(k for k,r in enumerate(rows) if r['outer_arrow']=='BA')
    d=tuple(F(int(k==i)-int(k==j)) for k in range(12))
    family=[]
    for beta in (F(0),F(1,2),F(1),F(2)):
        contrast=tuple(beta*a for a in d)
        # Two-point source orbit: comparison c and its nonidentical exchange.
        # This is an orbit-level numerical candidate, NOT an implementation of
        # the complete native source-to-geometry interpretation.
        first=(tuple(a+b for a,b in zip(u,contrast)),zero)
        second=(u,contrast)
        assert step(*first)==second and step(*second)==first
        decoded=tuple(a+b for a,b in zip(*first))
        assert decoded==tuple(a+b for a,b in zip(*second))
        assert (decoded==u)==(beta==0)
        family.append(dict(contrast_amplitude=str(beta),intertwines_two_point_exchange=True,
                           matches_existing_unperturbed_payload=decoded==u,
                           distinguishes_two_histories=first!=second))
    result=dict(schema='marici.nima.native-feedback-fixed-point-bridge.v1',status='pass',
        source_collective_coefficients=['1']*12,
        baseline='The actual phase-aligned collective field with empty bank is a fixed point.',
        formal_result='Any intertwiner mapping the initial native comparison to this fixed point also maps its distinct exchanged record to the same point. A payload-only reader is exchange-invariant.',
        orbit_adapter_controls=family,
        conclusion='A nontrivial numerical history-exchange image requires a different preparation or encoding. The former barycenter-return experiment supplied such a contrast; the inspected source baseline does not generate it.',
        scope='Obstruction for this initialization and this numerical update, not a prohibition on nonfaithful readouts, retained history, or every WG-to-physics realization.')
    (ROOT/'results/native-feedback-fixed-point-bridge.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
