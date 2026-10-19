"""Certified continuum endpoint self-energies at E=6, with typed flux fixture.
Exact rational box integration and integer-square-root enclosures. No finite-box
spectral broadening or fitted branching probability.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
from hashlib import sha256
import json

BASE=Path(__file__).resolve().parents[1]
SCALE=10**12

def atan_bounds(q,N):
    terms=[Q((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(N)]
    partial=sum(terms,Q());next_term=Q((-1)**N,(2*N+1)*q**(2*N+1))
    return min(partial,partial+next_term),max(partial,partial+next_term)
def pi_bounds():
    a,b=atan_bounds(5,40);c,d=atan_bounds(239,12)
    return 16*a-4*d,16*b-4*c

def radius_bounds(a,b,n):
    # x=4j/n, so x(4-x)=16 j(n-j)/n^2 on the support.
    assert a<=b
    if b<=0 or a>=n:return 0,0
    low=0 if a<=0 or b>=n else min(a*(n-a),b*(n-b))
    a=max(a,0);b=min(b,n)
    high=n*n//4 if 2*a<=n<=2*b else max(a*(n-a),b*(n-b))
    return low,high

def root_bounds(p):
    lo=isqrt(p*SCALE*SCALE)
    return lo,lo if lo*lo==p*SCALE*SCALE else lo+1

def density_two(E,n,pl,ph):
    shift=Q(E*n,4);assert shift.denominator==1;shift=int(shift)
    low=high=0
    for i in range(n):
        a,b=radius_bounds(i,i+1,n);c,d=radius_bounds(shift-i-1,shift-i,n)
        low+=root_bounds(a*c)[0];high+=root_bounds(b*d)[1]
    return Q(16*low,n**3*SCALE)/ph**2,Q(16*high,n**3*SCALE)/pl**2

def density_three(E,n,pl,ph):
    shift=Q(E*n,4);assert shift.denominator==1;shift=int(shift)
    radii=[radius_bounds(i,i+1,n) for i in range(n)]
    low=high=0
    for i,(a,b) in enumerate(radii):
        for j,(c,d) in enumerate(radii):
            f,g=radius_bounds(shift-i-j-2,shift-i-j,n)
            if not g:continue
            low+=root_bounds(a*c*f)[0];high+=root_bounds(b*d*g)[1]
    return Q(128*low,n**5*SCALE)/ph**3,Q(128*high,n**5*SCALE)/pl**3

def real_g2_at_six(n,pl,ph):
    # g1(6-x+i0) has real part (4-x)/2 everywhere, minus
    # sqrt((4-x)^2-4)/2 on x<2. The first term integrates to 1.
    low=high=0
    for i in range(n//2):
        a,b=radius_bounds(i,i+1,n)
        c=4*(n-i-1)**2-n*n;d=4*(n-i)**2-n*n
        assert 0<=c<=d
        low+=root_bounds(a*c)[0];high+=root_bounds(b*d)[1]
    return 1-Q(8*high,n**3*SCALE)/pl,1-Q(8*low,n**3*SCALE)/ph

class Interval:
    def __init__(self,low,high=None):
        self.low=Q(low);self.high=Q(low if high is None else high);assert self.low<=self.high
    @staticmethod
    def cast(x):return x if isinstance(x,Interval) else Interval(x)
    def __add__(self,x):
        x=self.cast(x);return Interval(self.low+x.low,self.high+x.high)
    __radd__=__add__
    def __neg__(self):return Interval(-self.high,-self.low)
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);v=[a*b for a in (self.low,self.high) for b in (x.low,x.high)]
        return Interval(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x);assert x.low>0 or x.high<0
        return self*Interval(1/x.high,1/x.low)
    def square(self):
        return Interval(0 if self.low<=0<=self.high else min(self.low**2,self.high**2),max(self.low**2,self.high**2))
    def record(self):return {'lower':str(self.low),'upper':str(self.high),'decimal_view':[float(self.low),float(self.high)]}
    def contains(self,x):return self.low<=x<=self.high

def main():
    source_path=BASE/'results/multiobject_orbital_selfenergy.json'
    source=json.loads(source_path.read_text(encoding='utf-8'));assert source['verification_passed']
    for name,digest in source['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    pl,ph=pi_bounds();P=Interval(pl,ph)
    check('Machin_pi_enclosure',3<pl<ph<Q(22,7) and ph-pl<Q(1,10**50))
    refinements=[]
    for n in (128,256,512):
        r2=Interval(*density_two(6,n,pl,ph));r3=Interval(*density_three(6,n,pl,ph));a2=Interval(*real_g2_at_six(n,pl,ph))
        check('positive_continuum_densities_'+str(n),r2.low>0 and r3.low>0)
        check('positive_pair_real_part_'+str(n),a2.low>0)
        check('two_density_reflection_'+str(n),density_two(2,n,pl,ph)==density_two(6,n,pl,ph))
        # Exact pair center: integral x(4-x)/(4pi^2) dx=8/(3pi^2).
        exact_pair_center=Interval(Q(8,3)/ph**2,Q(8,3)/pl**2)
        box_pair_center=Interval(*density_two(4,n,pl,ph))
        check('exact_pair_center_inside_box_'+str(n),box_pair_center.low<=exact_pair_center.low<=exact_pair_center.high<=box_pair_center.high)
        refinements.append({'energy':'6','grid_per_coordinate':n,'rho2':r2.record(),'rho3':r3.record(),'Re_g2':a2.record()})
    check('density_and_real_enclosures_refine',all(Q(b[key]['upper'])-Q(b[key]['lower'])<Q(a[key]['upper'])-Q(a[key]['lower']) for a,b in zip(refinements,refinements[1:]) for key in ('rho2','rho3','Re_g2')))
    # No density evaluation near the Hilbert singularity is needed: integrate
    # the exact one-body retarded g1 first. Three-body real part at its center
    # vanishes by reflection symmetry of its continuous spectral measure.
    b2=P*r2;b3=P*r3
    check('retarded_selfenergy_sign',b2.low>0 and b3.low>0)
    check('box_width_controls',r2.high-r2.low<Q(1,100) and r3.high-r3.low<Q(1,100) and a2.high-a2.low<Q(1,100))
    # Declared core Hcore=6 I4; all three lambdas=1. Input is a distinguishable
    # pair. Scalar sector couples to two-output; vector sector to three-output.
    scalar_den=a2.square()+b2.square()
    Ts=b2.square()/scalar_den;Rs=a2.square()/scalar_den
    vector_den=a2.square()+(b2+b3).square()
    Tv=4*b2*b3/vector_den;Rv=(a2.square()+(b2-b3).square())/vector_den
    check('scalar_flux_identity_enclosed',(Ts+Rs).contains(1))
    check('vector_flux_identity_enclosed',(Tv+Rv).contains(1))
    check('scalar_probabilities_in_unit_interval',0<Rs.low<Rs.high<1 and 0<Ts.low<Ts.high<1)
    check('vector_probabilities_in_unit_interval',0<Rv.low<Rv.high<1 and 0<Tv.low<Tv.high<1)
    # Independent exact optical identity controls with rational a,b,c >0.
    for a,b,c in ((Q(1,5),Q(2,7),Q(3,8)),(Q(2,3),Q(1,4),Q(5,6))):
        G=1/(a*a+(b+c)**2)
        check('rational_optical_identity_'+str(a), (a*a+(b-c)**2)*G+4*b*c*G==1)
    P2=Ts/4;P3=Q(3,4)*Tv;survival=Rs/4+Q(3,4)*Rv
    check('unpolarized_probabilities_normalize',(P2+P3+survival).contains(1))
    check('unpolarized_interval_widths',all(v.high-v.low<Q(1,20) for v in (P2,P3,survival)))
    result={'verification_passed':all(checks.values()),'checks':checks,'pi_enclosure':P.record(),
        'energy':'6','refinement_enclosures':refinements,
        'retarded_selfenergy_at_unit_coupling':{'incoming_pair':'(a2-i b2) I4','two_output':'(a2-i b2) P_scalar','three_output':'-i b3 P_vector',
            'a2':a2.record(),'b2':b2.record(),'b3':b3.record()},
        'exact_pair_center_control':'rho2(4)=8/(3pi^2), Re g2(4+i0)=0',
        'three_center_control':'Re g3(6+i0)=0 by reflection symmetry; rho3(6)>0 by positive convolution',
        'integration_certificate':'Box extrema of each square-root density, exact integer sqrt bounds at scale 10^12, and rational Machin pi enclosure. No quadrature-difference error assumption.',
        'typed_scattering_fixture':{'H_core':'6 I4','couplings':{'lambda_in':'1','lambda_2':'1','lambda_3':'1'},
            'scalar_T':Ts.record(),'scalar_R':Rs.record(),'vector_T':Tv.record(),'vector_R':Rv.record(),
            'unpolarized_input':'rho=I4/4','unpolarized_probabilities':{'two_output':P2.record(),'three_output':P3.record(),'survival':survival.record()},
            'ratio_two_to_three':(P2/P3).record(),
            'flux_law':'S=I-i Gamma^(1/2) G_core Gamma^(1/2), Gamma_c=2pi rho_c times the typed vertex Gram',
            'identity':'R_s+T_s=1, R_v+T_v=1 exactly; interval sums contain one but endpoint sums need not equal one.'},
        'qualifications':['Self-energies are infinite-volume retarded boundary values, not finite-box smearing.',
            'Probabilities refer to normalized energy-fiber bright-channel flux at E=6, not initial internal retained weights.',
            'Core energy, couplings, dispersion and endpoint attachment are declared fixture choices.',
            'This is not a native eleven-state spinor coupling, a photon channel identification or a physical ratio prediction.',
            'Other orbital modes orthogonal to the attachment remain free dark channels; no full-channel completeness is inferred from four core coordinates.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in (source_path,Path(__file__))}}
    (BASE/'results/multiobject_onband.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'rho2_E6':r2.record()['decimal_view'],'rho3_E6':r3.record()['decimal_view'],
        'Re_g2_E6':a2.record()['decimal_view'],'probabilities':{k:v['decimal_view'] for k,v in result['typed_scattering_fixture']['unpolarized_probabilities'].items()},
        'ratio':result['typed_scattering_fixture']['ratio_two_to_three']['decimal_view']},indent=2))

if __name__=='__main__':main()
