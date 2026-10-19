"""Certified real-axis endpoint dispersive parts, no finite eta substitution.
Integrate exact one-body retarded response first; box-enclose remaining integral.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
from hashlib import sha256
import json
from check_multiobject_onband import Interval,pi_bounds,radius_bounds,root_bounds,SCALE

BASE=Path(__file__).resolve().parents[1]
GRID=10**10

def load(name):
    path=BASE/'results'/name;r=json.loads(path.read_text(encoding='utf-8'));assert r['verification_passed']
    for source,digest in r['source_hashes'].items():assert sha256((BASE/source).read_bytes()).hexdigest()==digest
    return path,r

def real_g1_point(w):
    # w in integer units GRID. Exact radical endpoint enclosure.
    u=w-2*GRID
    if abs(u)<=2*GRID:
        return u//2,-((-u)//2)
    rad=u*u-4*GRID*GRID;low=isqrt(rad);high=low if low*low==rad else low+1
    if u>0:a,b=u-high,u-low
    else:a,b=u+low,u+high
    return a//2,-((-b)//2)

def real_g1_range(a,b):
    assert a<=b
    values=[real_g1_point(a),real_g1_point(b)]
    # Real g1 increases within [0,4], decreases outside, continuously meeting
    # its extrema -1 and +1 at the band edges.
    if a<=0<=b:values.append((-GRID,-GRID))
    if a<=4*GRID<=b:values.append((GRID,GRID))
    return min(x[0] for x in values),max(x[1] for x in values)

def signed_product(al,ah,bl,bh):
    values=(al*bl,al*bh,ah*bl,ah*bh)
    return min(values),max(values)

def real_pair(E,n,pl,ph):
    assert GRID%n==0
    low=high=0
    for i in range(n):
        a,b=radius_bounds(i,i+1,n);sl=root_bounds(a)[0];sh=root_bounds(b)[1]
        gl,gh=real_g1_range(E*GRID-4*(i+1)*GRID//n,E*GRID-4*i*GRID//n)
        l,h=signed_product(sl,sh,gl,gh);low+=l;high+=h
    return Interval(Q(8*low,n*n*SCALE*GRID),Q(8*high,n*n*SCALE*GRID))/Interval(pl,ph)

def real_vector_triple(E,n,pl,ph):
    assert GRID%n==0
    rad=[radius_bounds(i,i+1,n) for i in range(n)]
    responses=[real_g1_range(E*GRID-4*(s+2)*GRID//n,E*GRID-4*s*GRID//n) for s in range(2*n-1)]
    low=high=0
    for i,(a,b) in enumerate(rad):
        for j,(c,d) in enumerate(rad):
            sl=root_bounds(a*c)[0];sh=root_bounds(b*d)[1];gl,gh=responses[i+j]
            l,h=signed_product(sl,sh,gl,gh);low+=l;high+=h
    return Interval(Q(64*low,n**4*SCALE*GRID),Q(64*high,n**4*SCALE*GRID))/Interval(pl*pl,ph*ph)

def decode_interval(r):return Interval(Q(r['lower']),Q(r['upper']))
def intersect(a,b):return Interval(max(a.low,b.low),min(a.high,b.high))
def round_out(a):
    return Interval(Q(a.low.numerator*GRID//a.low.denominator,GRID),Q(-((-a.high.numerator*GRID)//a.high.denominator),GRID))

def main():
    energy_path,energy=load('multiobject_energy_response.json');center_path,center=load('multiobject_onband.json')
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    pl,ph=pi_bounds();P=Interval(pl,ph);reports=[];values={}
    check('one_body_edge_extrema',real_g1_point(0)==(-GRID,-GRID) and real_g1_point(4*GRID)==(GRID,GRID))
    check('one_body_real_center_zero',real_g1_point(2*GRID)==(0,0))
    check('branch_crossing_interval',real_g1_range(-GRID,5*GRID)==(-GRID,GRID))
    for E in (2,4):
        refinements=[]
        for n in (128,256,512):
            pair=real_pair(E,n,pl,ph);vector=real_vector_triple(E,n,pl,ph)
            check('retarded_real_parts_bounded_'+str(E)+'_'+str(n),-1<=pair.low<=pair.high<=1 and -1<=vector.low<=vector.high<=1)
            check('vector_reflection_'+str(E)+'_'+str(n),real_vector_triple(12-E,n,pl,ph).low==-vector.high and real_vector_triple(12-E,n,pl,ph).high==-vector.low)
            check('pair_reflection_'+str(E)+'_'+str(n),real_pair(8-E,n,pl,ph).low==-pair.high and real_pair(8-E,n,pl,ph).high==-pair.low)
            refinements.append({'mesh':n,'Re_g_pair':pair.record(),'Re_g_vector3':vector.record()})
        check('real_enclosure_mesh_refines_'+str(E),all(Q(b[k]['upper'])-Q(b[k]['lower'])<Q(a[k]['upper'])-Q(a[k]['lower']) for a,b in zip(refinements,refinements[1:]) for k in ('Re_g_pair','Re_g_vector3')))
        check('negative_vector_real_part_'+str(E),vector.high<0)
        check('real_enclosure_width_'+str(E),pair.high-pair.low<Q(1,20) and vector.high-vector.low<Q(1,20))
        if E==2:
            old=decode_interval(center['retarded_selfenergy_at_unit_coupling']['a2']);reflected=-old
            check('independent_pair_real_control_overlap',pair.low<=reflected.high and reflected.low<=pair.high)
        else:
            check('pair_center_real_zero_enclosed',pair.contains(0));pair=Interval(0)
        density_report=next(r for r in energy['real_axis_density_reports'] if r['energy']==str(E))['refinements'][-1]
        bp=round_out(P*decode_interval(density_report['rho_pair']));bv=round_out(P*decode_interval(density_report['rho_vector3']))
        pair=round_out(pair);vector=round_out(vector);values[E]=(pair,vector,bp,bv)
        reports.append({'energy':str(E),'refinements':refinements,'response_used':{'a_pair':pair.record(),'a_vector3':vector.record(),'b_pair':bp.record(),'b_vector3':bv.record()}})
    # This is the endpoint-only submodel, lambda_A=0, not a substitute for the
    # combined Slater-record fixture's unresolved scalar real part.
    flux=[]
    for E,(ap,av,bp,bv) in values.items():
        ds=E-6-2*ap;dv=E-6-ap-av
        den_s=ds.square()+4*bp.square();den_v=dv.square()+(bp+bv).square()
        Ts=4*bp.square()/den_s;Rs=ds.square()/den_s
        Tv=4*bp*bv/den_v;Rv=(dv.square()+(bp-bv).square())/den_v
        Ts=intersect(Ts,1-Rs);Rs=intersect(Rs,1-Ts)
        Tv=intersect(Tv,1-Rv);Rv=intersect(Rv,1-Tv)
        p2=Ts/4;p3=Q(3,4)*Tv;survival=intersect(Rs/4+Q(3,4)*Rv,1-p2-p3)
        check('offcenter_scalar_flux_'+str(E),(Ts+Rs).contains(1))
        check('offcenter_vector_flux_'+str(E),(Tv+Rv).contains(1))
        check('offcenter_unpolarized_flux_'+str(E),(p2+p3+survival).contains(1))
        check('offcenter_probabilities_between_zero_one_'+str(E),all(0<x.low<=x.high<1 for x in (p2,p3,survival)))
        flux.append({'energy':str(E),'two_output':p2.record(),'vector_three_output':p3.record(),'survival':survival.record()})
    result={'verification_passed':all(checks.values()),'checks':checks,'real_axis_reports':reports,'endpoint_only_scattering':flux,
        'one_body_boundary_formula':'Re g1(w+i0)=(w-2)/2 in [0,4]; [(w-2)-sign(w-2)sqrt((w-2)^2-4)]/2 outside.',
        'pair_real_formula':'integral rho1(x) Re g1(E-x+i0) dx',
        'vector_triple_real_formula':'integral rho1(x)rho1(y) Re g1(E-x-y+i0) dxdy',
        'certificate':'Integrate the last spectral variable analytically before box integration. Bound continuous branch-point response by endpoint values and exact extrema at 0,4. Exact signed products, integer sqrt and rational pi bounds.',
        'scattering_fixture':'Hcore=6I4, lambda_in=lambda_2=lambda_vector3=1, lambda_A=0; incoming rho=I4/4.',
        'qualifications':['These are real-axis retarded dispersive certificates, with no finite eta approximation.',
            'The scalar Slater-record principal-value response is not the endpoint triple response and remains open.',
            'The scattering fixture explicitly switches off the Slater vertex, rather than silently assigning it an endpoint self-energy.',
            'Native source-to-core attachment and physical coupling/calibration remain unestablished.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in
            (energy_path,center_path,Path(__file__),BASE/'checkers/check_multiobject_onband.py')}}
    (BASE/'results/offcenter_endpoint_dispersion.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verification_passed':True,'check_count':len(checks),'real_parts':[
        {'energy':r['energy'],'pair':r['response_used']['a_pair']['decimal_view'],'vector3':r['response_used']['a_vector3']['decimal_view']} for r in reports],
        'offcenter_probabilities':[{key:(value['decimal_view'] if isinstance(value,dict) else value) for key,value in r.items()} for r in flux]},indent=2))

if __name__=='__main__':main()
