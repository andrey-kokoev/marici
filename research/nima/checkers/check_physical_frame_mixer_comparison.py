"""Compare the recovered Rosen frame equations to the attached record law.
Exact local source identities and static intertwining, not a WG-to-GR map.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from check_four_packet_cycle import UNIT,matrix
from check_four_packet_record_feedback import mm,transpose,matrix_of,basis
from check_attached_record_dynamics import carrier_frame,block,update
from check_local_frame_mixer_obstruction import endpoint_frames,determinant
ROOT=Path(__file__).resolve().parents[1]

def add(a,b):return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c):return tuple(tuple(c*x for x in r) for r in a)
def rotation(c,s):return ((c,-s),(s,c))
def main():
    I=matrix(UNIT);J=((F(0),F(-1)),(F(1),F(0)))
    U=matrix_of(lambda z:update(z,1,1),20)
    qs=(I,rotation(F(3,5),F(4,5)),rotation(F(5,13),F(12,13)))
    for q in qs:assert determinant(q)==1 and mm(transpose(q),q)==I
    for q0,q1,q2 in product(qs,repeat=3):
        H=block(carrier_frame(q0,q2),endpoint_frames(q0,q1,q2))
        assert mm(U,H)==mm(H,U)
    families=[]
    for p in (F(1),F(6,5),F(5,4)):
        D=((p*p,F(0)),(F(0),1/(p*p)))
        Di=((1/(p*p),F(0)),(F(0),p*p))
        Cp=add(mm(J,D),scale(mm(D,J),-1))
        N=scale(mm(Di,Cp),F(-1,2))
        # At r=1,r'=0, F'=N F and gamma'=C'.
        assert add(add(mm(transpose(N),D),mm(D,N)),Cp)==((0,0),(0,0))
        c=(p*p+1/(p*p))/2;s=(p*p-1/(p*p))/2
        assert c*c-s*s==1 and 0<=s<F(1,2)
        if p!=1:assert add(N,transpose(N))!=((0,0),(0,0))
        # Independent derivation of the source's connection in its moving
        # orthonormal shape basis B=R D^(-1/2) at u=0.
        B=((1/p,F(0)),(F(0),p));Bi=((p,F(0)),(F(0),1/p))
        K=mm(Bi,add(mm(J,B),scale(mm(N,B),-1)))
        assert K==scale(J,c)
        families.append(dict(p=str(p),connection_coefficient=str(c),
                             focusing_coefficient=str(s*s),
                             endpoint_rotation_in_units_of_pi=str(1-c),
                             orientation_character=1))
    assert len({r['endpoint_rotation_in_units_of_pi'] for r in families})==3
    result=dict(schema='marici.nima.physical-frame-mixer-comparison.v1',status='pass',
        proper_endpoint_frame_controls=27,source_frame_family=families,
        structural_identity='U commutes with all independent proper orthogonal endpoint frame actions. Their determinant attachment characters are trivial.',
        source_metric_warning='The coordinate parallel-transport generator is not generally skew in the Euclidean counting metric. It is compatible with the evolving Rosen metric. Orthonormal frames must be compared before applying the bank covariance law.',
        selection_boundary='Different admitted shape histories have different focusing and frame transport but the same orientation signs and same intrinsic attached mixer. The mixer/orientation data cannot reconstruct the physical history.',
        normalization_boundary='The recovered construction imposes Ric=0. For zero stress tensor Einstein equations contain no dependence on G, so this vacuum reconstruction cannot select gravitational coupling.',
        scope='The calculations compare declared mathematical representations. They do not identify Boolean fibers with physical transverse planes or derive a matter coupling.')
    (ROOT/'results/physical-frame-mixer-comparison.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
