"""Exact common-frame and sewn independent-frame path comparisons."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import check_clifford_retained_order as C

ROOT=Path(__file__).resolve().parents[1]
UNITS=[C.realize((s,a,b)) for s in (1,-1) for a,b in product((0,1),repeat=2)]
def inv(m):
    d=m[0]*m[3]-m[1]*m[2]
    assert d
    return C.scale(F(1,d),(m[3],-m[1],-m[2],m[0]))
def chain(*args):
    result=C.I
    for a in args: result=C.mul(result,a)
    return result
def apply(m,w): return (m[0]*w[0]+m[1]*w[1],m[2]*w[0]+m[3]*w[1])
def dot(v,w): return sum(a*b for a,b in zip(v,w))
def outer(w): return (w[0]*w[0],w[0]*w[1],w[1]*w[0],w[1]*w[1])
def main():
    out=ROOT/'results/relative-phase-readout.json'
    out.unlink(missing_ok=True)
    common=0
    for U,V,a,b in product(UNITS,repeat=4):
        R=chain(inv(U),V)
        Up=chain(b,U,inv(a)); Vp=chain(b,V,inv(a))
        Rp=chain(inv(Up),Vp)
        assert Rp==chain(a,R,inv(a))
        assert C.scalar(Rp)==C.scalar(R)
        Jp=chain(a,C.J,inv(a))
        assert -C.scalar(chain(Jp,Rp))==-C.scalar(chain(C.J,R))
        common+=1
    for U,V,W in product(UNITS,repeat=3):
        assert chain(inv(U),V,inv(V),W)==chain(inv(U),W)
    # Independent arm frames require BOTH endpoint comparison maps.
    minus=C.scale(-1,C.I)
    sewn=0
    for a1,a2,b1,b2 in product(UNITS,repeat=4):
        Up=chain(b1,C.I,inv(a1)); Vp=chain(b2,minus,inv(a2))
        final_comparison=chain(b1,inv(b2))
        initial_comparison=chain(a2,inv(a1))
        assert chain(inv(Up),final_comparison,Vp,initial_comparison)==minus
        sewn+=1
    # Changing only the second terminal frame can fake +1 if sewing is lost.
    U=C.I; V=minus
    Up=U; Vp=chain(minus,V)
    assert chain(inv(Up),Vp)==C.I
    assert chain(inv(Up),minus,Vp)==minus
    w=(F(3,5),F(4,5)); negative=tuple(-x for x in w)
    assert dot(w,w)==dot(negative,negative)==1
    assert outer(w)==outer(negative)
    assert dot(w,negative)==-1
    assert dot(tuple(2*x for x in w),tuple(2*x for x in w))==4
    assert dot(tuple(x+y for x,y in zip(w,negative)),tuple(x+y for x,y in zip(w,negative)))==0
    # Trace is intentionally incomplete: opposite quarter phases both give 0.
    assert C.scalar(C.J)==C.scalar(C.scale(-1,C.J))==0
    assert C.J!=C.scale(-1,C.J)
    assert -C.scalar(chain(C.J,C.J))==1
    assert -C.scalar(chain(C.J,C.scale(-1,C.J)))==-1
    assert chain(C.E1,C.J,C.E1)==C.scale(-1,C.J)
    # Nonorthogonal coordinate frames require metric transport as well.
    b=(F(2),F(1),F(0),F(1))
    bp=apply(b,w)
    metric=chain(C.reverse(inv(b)),inv(b))
    assert dot(bp,apply(metric,bp))==dot(w,w)
    assert dot(bp,bp)!=dot(w,w)
    assert C.scalar(chain(b,C.J,inv(b)))==C.scalar(C.J)
    inputs=(Path(__file__),Path(C.__file__),ROOT/'retained-active-passive-action.md')
    result={
      'schema':'marici.nima.relative-phase-readout.v1',
      'classification':'common_endpoint_relative_transport_retains_central_sign_independent_frames_require_sewing',
      'comparator':'R12=U1^-1 U2; common frame changes conjugate R12 at its initial fiber',
      'sewing':'U1prime^-1 (b1 b2^-1) U2prime (a2 a1^-1)=a1 R12 a1^-1',
      'controls':{'common_frame_cases':common,'independent_frame_sewing_cases':sewn,'three_path_cases':512,'missing_sewing_hostile':'rejected','fixed_metric_under_nonorthogonal_frame':'rejected'},
      'losses':['single-arm norms and rank-one real outer products erase the central sign','normalized trace does not separate J and -J','full endpoint transport still forgets complete histories'],
      'scope':'Conditional defining real module. A linear recombination and norm readout mathematically distinguish the two-arm sign, but no native physical realization, recombination apparatus, probability law or Born rule is established.',
      'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
