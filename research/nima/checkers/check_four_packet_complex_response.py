"""Extract exact complex phase sectors from the existing real feedback map.

No observed mass, fitted phase, new cycle law or complex scalar assumption is
used to select U. The twelve-channel readout remains a declared comparison.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_four_packet_record_feedback import basis, matrix_of, full_cycle, transpose, mm, rank, sub, norm2


def madd(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def mscale(a,c): return tuple(tuple(c*x for x in row) for row in a)
def msub(a,b): return madd(a,mscale(b,F(-1)))
def mv(a,v): return tuple(sum((x*y for x,y in zip(row,v)),F(0)) for row in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def trace(a): return sum((a[i][i] for i in range(len(a))),F(0))

def phase_response(v,U,D):
    # Complex z=r+i*sqrt(3)*b; K=D/sqrt(3), imaginary readout=<Kv,Uv>/||v||².
    n=norm2(v)
    if not n: raise ValueError('Zero vector has no normalized phase response')
    uv=mv(U,v)
    return dot(v,uv)/n, dot(mv(D,v),uv)/(3*n)

def znorm(z): return z[0]*z[0]+3*z[1]*z[1]
def zscale(z,a): return tuple(a*x for x in z)
def zserialize(z): return {'real':str(z[0]),'imaginary_sqrt3_coefficient':str(z[1]),'norm_squared':str(znorm(z))}

def main():
    U=matrix_of(full_cycle,20);Ut=transpose(U);I=basis(20)
    D=msub(U,Ut);H=madd(U,Ut)
    P=mscale(mm(D,D),F(-1,3))
    assert mm(P,P)==P and transpose(P)==P and rank(P)==8
    assert mm(D,P)==D and mm(P,D)==D
    assert mm(D,D)==mscale(P,F(-3))
    assert transpose(D)==mscale(D,F(-1))
    # K=D/sqrt(3) has K²=-P and K^T K=P on the rotating subspace.
    Pplus=mscale(madd(P,mm(H,P)),F(1,2))
    Pminus=mscale(msub(P,mm(H,P)),F(1,2))
    zero=mscale(I,F(0))
    assert madd(Pplus,Pminus)==P and mm(Pplus,Pminus)==zero
    sectors={}
    for name,Q,real in [('sixty_degree',Pplus,F(1,2)),('one_twenty_degree',Pminus,F(-1,2))]:
        assert transpose(Q)==Q and mm(Q,Q)==Q and rank(Q)==4
        # U restricted to Q is real*I + (sqrt(3)/2)*K.
        assert mm(U,Q)==madd(mscale(Q,real),mscale(mm(D,Q),F(1,2)))
        assert trace(mm(D,Q))==0
        witnesses=[mv(Q,e) for e in basis(20)]
        witness_count=0
        for v in witnesses:
            if not norm2(v): continue
            witness_count+=1
            z=phase_response(v,U,D)
            assert z==(real,F(1,2)) and znorm(z)==1
            assert phase_response(tuple(7*x for x in v),U,D)==z
            # Keep the same complex structure when reversing the cycle.
            assert phase_response(v,Ut,D)==(real,F(-1,2))
            assert phase_response(v,I,D)==(F(1),F(0))
            assert norm2(mv(U,v))==norm2(v)
        z=(real,F(1,2));outer=zscale(z,F(12));total=zscale(outer,F(153))
        assert znorm(outer)==144 and znorm(total)==1836**2
        sectors[name]={'rank':rank(Q),'basis_projection_witnesses':witness_count,
                       'unit_phase':zserialize(z),'uniform_twelve_channel_response':zserialize(outer),
                       'times_153_response':zserialize(total),
                       'modulus_readout':1836}
    # All remaining modes are real +/-1, not an additional imaginary scalar.
    Prest=msub(I,P)
    assert rank(Prest)==12 and mm(D,Prest)==zero
    assert mm(mm(U,U),Prest)==Prest
    assert trace(U)==0  # Full spectral trace must not be relabelled as 12 channels.
    # A phase alone cannot keep Re=12 while adding an imaginary component at norm 12.
    eta_controls=(F(0),F(1,10),F(1),F(2))
    for eta in eta_controls:
        square=144+eta*eta
        assert (square==144)==(eta==0)
    # Rescaling the real part of a +/-60/120 response to +12 doubles its modulus.
    for real in (F(1,2),F(-1,2)):
        gain=F(12)/real
        normalized=zscale((real,F(1,2)),gain)
        assert normalized[0]==12 and znorm(normalized)==24**2
    # Unselected initial rotating amplitude remains free despite fixed phase.
    for amplitude in (F(0),F(1,10),F(1),F(2)):
        assert znorm(zscale((F(1,2),F(1,2)),amplitude))==amplitude**2
    # U^6 is an operator identity; do not extend retained histories past depth 3.
    power=I
    for _ in range(6): power=mm(U,power)
    assert power==I
    report={'status':'passed','input':'unchanged four-packet record-feedback U',
            'complex_structure':'K=(U-U^T)/sqrt(3), K²=-P',
            'rotating_dimension':8,'real_mode_dimension':12,
            'sectors':sectors,
            'candidate_12_plus_i_eta':'not derived: fixed-real additive quadrature differs from fixed-modulus phase',
            'phase_only_153_times_12_modulus':1836,
            'no_fit_inputs':True,
            'gates':['No source-selected adapter from 20D feedback carrier to 12 directed relationship channels',
                     'No selected sector, initial complex amplitude, or quadrature reference',
                     'No mass/energy readout or physical units selected']}
    path=Path(__file__).resolve().parents[1]/'results'/'four-packet-complex-response.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: exact complex sectors at 60/120 degrees, conjugate reversal, unit modulus, 1836 unchanged by phase alone. No fitted eta or mass prediction.')

if __name__=='__main__': main()
