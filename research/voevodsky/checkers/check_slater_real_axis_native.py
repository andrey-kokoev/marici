"""Slater real-axis dispersive certificate and source-core optical fixture.
Stable finite orbital Green block: no finite eta or polynomial large subtraction.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
from hashlib import sha256
import json
from check_multiobject_onband import Interval,pi_bounds,radius_bounds,root_bounds,SCALE
from check_offcenter_endpoint_dispersion import real_g1_range,GRID as OLDGRID
from check_native_spinor_pair_adapter import matrix
from check_pentachoron_spin_interfaces import A,S2,S3,S5

BASE=Path(__file__).resolve().parents[1];G=2**40

def load(name):
    path=BASE/'results'/name;r=json.loads(path.read_text(encoding='utf-8'));assert r['verification_passed']
    for source,digest in r['source_hashes'].items():assert sha256((BASE/source).read_bytes()).hexdigest()==digest
    return path,r

# Fixed-point interval primitives. All rounding is directed and integer exact.
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def minus(a,b):return plus(a,neg(b))
def times(a,b):
    v=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]);lo=min(v);hi=max(v)
    return lo//G,-((-hi)//G)
def scale(n,a):return (n*a[0],n*a[1]) if n>=0 else (n*a[1],n*a[0])
def square(a):
    lo=0 if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2);hi=max(a[0]**2,a[1]**2)
    return lo//G,-((-hi)//G)
def hull(values):return min(v[0] for v in values),max(v[1] for v in values)
def power_range(a,n):
    lo=0 if n%2==0 and a[0]<=0<=a[1] else min(a[0]**n,a[1]**n);hi=max(a[0]**n,a[1]**n)
    den=G**(n-1);return lo//den,-((-hi)//den)
def root_fixed(n):
    lo=isqrt(n*G*G);return lo,lo if lo*lo==n*G*G else lo+1

R2=root_fixed(2);R5=root_fixed(5)
def div_int(a,n):return a[0]//n,-((-a[1])//n)
critical={1:[],2:[((0,0),-1)],3:[((G//2,G//2),-1),((-G//2,-G//2),1)],
    4:[(div_int(R2,2),-1),((0,0),1),(neg(div_int(R2,2)),-1)],
    5:[(div_int(plus((G,G),R5),4),-1),(div_int(minus(R5,(G,G)),4),1),
       (div_int(minus((G,G),R5),4),-1),(neg(div_int(plus((G,G),R5),4)),1)]}

def cheb_point(x,n):
    prev=(G,G);current=(x,x)
    if n==0:return prev
    for _ in range(1,n):prev,current=current,minus(scale(2,times((x,x),current)),prev)
    return current

def cheb_range(a,n):
    values=[cheb_point(a[0],n),cheb_point(a[1],n)]
    for location,sign in critical[n]:
        if a[0]<=location[1] and location[0]<=a[1]:values.append((sign*G,sign*G))
    low,high=hull(values);return max(low,-G),min(high,G)

def real_root_range(a,b):
    # Same branch extrema as predecessor, now without a grid conversion.
    def point(w):
        u=w-2*G
        if abs(u)<=2*G:return div_int((u,u),2)
        rad=u*u-4*G*G;l=isqrt(rad);h=l if l*l==rad else l+1
        return div_int((u-h,u-l) if u>0 else (u+l,u+h),2)
    values=[point(a),point(b)]
    if a<=0<=b:values.append((-G,-G))
    if a<=4*G<=b:values.append((G,G))
    return hull(values)

def real_powers(a,b):
    pieces=[]
    if a<0:
        root=real_root_range(a,min(b,0));pieces.append([power_range(root,n) for n in range(1,6)])
    if a<=4*G and b>=0:
        t=div_int((max(a,0)-2*G,min(b,4*G)-2*G),2)
        pieces.append([cheb_range(t,n) for n in range(1,6)])
    if b>4*G:
        root=real_root_range(max(a,4*G),b);pieces.append([power_range(root,n) for n in range(1,6)])
    return [hull([piece[n] for piece in pieces]) for n in range(5)]

def scalar_real(E,n,pl,ph):
    assert G%n==0
    radii=[radius_bounds(i,i+1,n) for i in range(n)]
    powers=[real_powers(E*G-4*(s+2)*G//n,E*G-4*s*G//n) for s in range(2*n-1)]
    coords=[(4*i*G//n,4*(i+1)*G//n) for i in range(n)]
    low=high=0
    for i,x in enumerate(coords):
        for j,y in enumerate(coords):
            # q(t)=(t-x)(t-y)=r2+(4-x-y)r1+[(x-2)(y-2)+1],
            # where r0,r1,r2 are the orthonormal endpoint spectral polynomials.
            v0=plus(times(minus(x,(2*G,2*G)),minus(y,(2*G,2*G))),(G,G))
            v1=minus((4*G,4*G),plus(x,y))
            coefficients=[plus(plus(square(v0),square(v1)),(G,G)),
                scale(2,times(v1,plus(v0,(G,G)))),plus(plus(scale(2,v0),square(v1)),(G,G)),scale(2,v1),(G,G)]
            F=(0,0)
            for c,p in zip(coefficients,powers[i+j]):F=plus(F,times(c,p))
            integrand=times(square(minus(x,y)),F)
            a,b=radii[i];c,d=radii[j];sl=root_bounds(a*c)[0];sh=root_bounds(b*d)[1]
            candidates=(sl*integrand[0],sl*integrand[1],sh*integrand[0],sh*integrand[1])
            low+=min(candidates);high+=max(candidates)
    factor=Q(64,6*n**4*SCALE*G)
    return Interval(factor*low,factor*high)/Interval(pl*pl,ph*ph)

def read_interval(r):return Interval(Q(r['lower']),Q(r['upper']))
def intersect(a,b):return Interval(max(a.low,b.low),min(a.high,b.high))
def grid_out(v):
    return Interval(Q(v.low.numerator*G//v.low.denominator,G),Q(-((-v.high.numerator*G)//v.high.denominator),G))

def main():
    native_path,native=load('native_spinor_pair_adapter.json');endpoint_path,endpoint=load('offcenter_endpoint_dispersion.json');energy_path,energy=load('multiobject_energy_response.json')
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    # One-body off-diagonal Green identity, exact at a rational root g=1/3.
    # R_ab=g^(|a-b|+1) sum_{j=0}^{min(a,b)} g^(2j).
    g=Q(1,3);w=2+g+1/g
    block=[[sum((g**(abs(a-b)+1+2*j) for j in range(min(a,b)+1)),Q()) for b in range(3)] for a in range(3)]
    # Impose the tail Schur term g on site two of the three-site block.
    D=[[Q(w-2 if a==b else -1 if abs(a-b)==1 else 0) for b in range(3)] for a in range(3)];D[2][2]-=g
    check('stable_one_body_Green_block_identity',all(sum(D[a][j]*block[j][b] for j in range(3))==(a==b) for a in range(3) for b in range(3)))
    check('Chebyshev_edge_values',all(cheb_range((G,G),n)==(G,G) and cheb_range((-G,-G),n)==(((-1)**n)*G,((-1)**n)*G) for n in range(1,6)))
    # Independently compare the stable Green-block contraction against exact
    # polynomial division of the same weighted Stieltjes integral.
    for index,g in enumerate((Q(1,3),Q(-1,2))):
        w=2+g+1/g;x=Q(1,2);y=Q(5,2)
        v=(x*y-2*(x+y)+5,4-x-y,1)
        R=[[sum((g**(abs(a-b)+1+2*j) for j in range(min(a,b)+1)),Q()) for b in range(3)] for a in range(3)]
        stable=sum(v[a]*R[a][b]*v[b] for a in range(3) for b in range(3))
        p=(x*x*y*y,-2*x*y*(x+y),x*x+4*x*y+y*y,-2*(x+y),Q(1))
        moments_=(1,2,5,14)
        remainder=sum(p[l]*sum(w**(l-1-j)*moments_[j] for j in range(l)) for l in range(1,5))
        check('stable_vs_polynomial_weighted_response_'+str(index),stable==sum(p[l]*w**l for l in range(5))*g-remainder)
    pl,ph=pi_bounds();refinements=[]
    check('Slater_center_real_zero_control',scalar_real(6,32,pl,ph).contains(0))
    for n in (64,128,256,512):
        real=scalar_real(4,n,pl,ph)
        refinements.append({'mesh':n,'Re_g_A_at_4':real.record()})
    check('Slater_real_bounds_refine',all(Q(b['Re_g_A_at_4']['upper'])-Q(b['Re_g_A_at_4']['lower'])<Q(a['Re_g_A_at_4']['upper'])-Q(a['Re_g_A_at_4']['lower']) for a,b in zip(refinements,refinements[1:])))
    check('Slater_real_part_strictly_negative',real.high<0)
    # Tightness is reported rather than assumed; all enclosures remain valid.
    real=grid_out(real)
    endpoint4=next(r for r in endpoint['real_axis_reports'] if r['energy']=='4')['response_used']
    ap=read_interval(endpoint4['a_pair']);av=read_interval(endpoint4['a_vector3']);bp=read_interval(endpoint4['b_pair']);bv=read_interval(endpoint4['b_vector3'])
    density4=next(r for r in energy['real_axis_density_reports'] if r['energy']=='4')['refinements'][-1]['rho_scalar3']
    ba=grid_out(Interval(pl,ph)*read_interval(density4))
    r6=Interval(Q(root_fixed(6)[0],G),Q(root_fixed(6)[1],G));r5=Interval(Q(R5[0],G),Q(R5[1],G))
    fixture=[]
    for option in (0,1):
        core=11-2*r6+(-r5 if option==0 else r5)
        expected=A(11)-2*S2*S3+(-S5 if option==0 else S5)
        check('source_core_energy_identity_'+str(option),all(matrix([[r['pair_conditional_core_energy']]])[0][0]==expected for r in native['adapter_reports'] if r['doublet_option']==option))
        ds=4-core-2*ap-real;dv=4-core-ap-av
        B=2*bp+ba;den=ds.square()+B.square();denv=dv.square()+(bp+bv).square()
        T2=4*bp.square()/den;TA=4*bp*ba/den;Rs=(ds.square()+ba.square())/den
        # Intersection with [0,1] and exact optical complements is safe, even
        # when correlated Slater interval extremes produce wide quotients.
        unit=Interval(0,1)
        T2=intersect(T2,unit);TA=intersect(TA,unit);Rs=intersect(Rs,unit)
        T2=intersect(T2,1-TA-Rs);TA=intersect(TA,1-T2-Rs);Rs=intersect(Rs,1-T2-TA)
        Tv=4*bp*bv/denv;Rv=(dv.square()+(bp-bv).square())/denv
        Tv=intersect(Tv,1-Rv);Rv=intersect(Rv,1-Tv)
        P2=T2/4;Pa=TA/4;Pv=Q(3,4)*Tv;P3=Pa+Pv;survival=intersect(Rs/4+Q(3,4)*Rv,1-P2-P3)
        check('source_core_scalar_optical_sum_'+str(option),(T2+TA+Rs).contains(1))
        check('source_core_vector_optical_sum_'+str(option),(Tv+Rv).contains(1))
        check('source_core_unpolarized_sum_'+str(option),(P2+P3+survival).contains(1))
        check('source_core_probabilities_bounded_'+str(option),all(0<=v.low<=v.high<=1 for v in (P2,Pa,Pv,P3,survival)))
        fixture.append({'option':option,'source_core_energy':core.record(),'two_output':P2.record(),'scalar_three_output':Pa.record(),'vector_three_output':Pv.record(),'all_three_output':P3.record(),'survival':survival.record()})
    check('source_doublet_choice_changes_triple_flux',Q(fixture[0]['all_three_output']['lower'])>Q(fixture[1]['all_three_output']['upper']))
    check('excited_doublet_has_more_reflection_in_this_fixture',Q(fixture[1]['survival']['lower'])>Q(fixture[0]['survival']['upper']))
    result={'verification_passed':all(checks.values()),'checks':checks,'Slater_real_refinements':refinements,'Slater_real_at_4':real.record(),
        'stable_integrand':'q(t)=(t-x)(t-y)=r2+v1 r1+v0; v1=4-x-y, v0=(x-2)(y-2)+1. Conditional orbital response is v^T R(w) v, w=E-x-y.',
        'Green_block_formula':'R_ab(w)=sum_{j=0}^{min(a,b)} g1(w)^(|a-b|+1+2j), in the h=2I+adjacency gauge.',
        'real_power_rule':'Inside [0,4], Re g1(w)^m=T_m((w-2)/2); outside, g1 is real and powers are enclosed directly.',
        'certificate':'Directed fixed-point integer interval arithmetic; Chebyshev endpoints plus enclosed critical points; exact radical weight bounds and rational pi enclosure. No finite eta.',
        'source_core_fixtures':fixture,'fixture_choices':{'relative_native_orbital_scale':'1','cross_channel_lambdas':'all 1','incoming_density':'I4/4','energy':'4','cycle_energy_rule':'L+(T-I)^dagger(T-I), predecessor equal weight'},
        'physical_coupling_admitted':False,
        'qualifications':['The scalar Slater real part is integrated with its distinct orbital records, not endpoint relabeling.',
            'Probability bounds are deliberately retained if broad; no midpoint calibration is used.',
            'Source core energies replace the arbitrary 6I fixture, but relative scale and couplings are still declared.',
            'Adapters with nonambient effective output action require the explicit output representation choice from the preceding audit.',
            'No physical positron/photon identification or empirical coupling theorem is derived.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (native_path,endpoint_path,energy_path,Path(__file__),BASE/'checkers/check_multiobject_onband.py',BASE/'checkers/check_offcenter_endpoint_dispersion.py')}}
    (BASE/'results/slater_real_axis_native.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'Re_g_A_at_4':real.record()['decimal_view'],'source_core_fixtures':[
        {name:(value['decimal_view'] if isinstance(value,dict) else value) for name,value in row.items()} for row in fixture]},indent=2))

if __name__=='__main__':main()
