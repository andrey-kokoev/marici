"""Twelve-coordinate regular degree-six photon logarithmic/window tensor and scale transport."""
import argparse
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree6_cut_v1 as cut
import check_photon_local_degree6_v1 as local
import check_photon_general_degree5_window_v1 as prev
base=local.base;sub=prev.sub;cross=sub.cross;channel=prev.channel
CONTRACT=HOME/'contracts/photon-general-degree6-window-v1.json';PROOF=HOME/'photon-general-degree6-window-v1.md'
TEST=HOME/'checkers/test_photon_general_degree6_window_v1.py';MANIFEST=HOME/'scc-models/photon-general-degree6-window-v1.json'
RESULT=HOME/'results/photon-general-degree6-window-v1.json'
Z=(Q(),)*12

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q())
_,_,CASES=cut.inventory()
get=lambda poly,n:poly[n] if n<len(poly) else Q()
D2=tuple(get(c[0],2)/6 for c in CASES);D0=tuple(c[0][0]-d for c,d in zip(CASES,D2))
O2=tuple(get(c[1],2)/6 for c in CASES);O0=tuple(c[1][0]-d for c,d in zip(CASES,O2))
M3=tuple(-get(c[2],3)/6 for c in CASES);M2=tuple(c[2][0]-d for c,d in zip(CASES,M3))
A=scale(-1,add(D0,D2));B=scale(6,D2)
C=scale(-1,add(M2,M3));D=scale(-6,M3)
AO=scale(-1,add(O0,O2));BO=scale(6,O2)
H=tuple(-get(c[3],1) for c in CASES)
FLOW=(add(A,C),add(add(B,scale(-4,C)),D),add(scale(2,C),scale(-2,D)),
      scale(Q(1,4),AO),scale(3,add(AO,BO)),scale(3,H))
K=3*max(sum(map(abs,v),Q())+sum(map(abs,w),Q()) for v,w in ((A,B),(C,D),(AO,BO),(H,Z)))


def coefficients(q,e):
    F,T=zip(*(base.fields(p,v) for p,v in zip(q,e)))
    s={(i,j):base.determinant(base.ma(q[i],q[j])) for i in range(4) for j in range(4) if i!=j}
    out=[Z]*3
    def put(r,c,v):out[r]=add(out[r],scale(c,v))
    for i,j in combinations(range(4),2):
        k,l=tuple(a for a in range(4) if a not in (i,j));x=(s[i,j]+s[k,l])/2
        w=(s[i,k]*s[i,l]+s[j,k]*s[j,l]+s[k,i]*s[k,j]+s[l,i]*s[l,j])/4
        P=base.contract(F[i],F[j])*base.contract(T[k],T[l])
        put(channel(i,j),P*x**4,A);put(channel(i,j),P*x*x*w,B)
        for a in (i,j):
            for b in (k,l):
                y=s[a,b];z=-x-y
                put(channel(a,b),P*y**4/2,C);put(channel(a,b),P*y**3*z/2,D)
    v=base.covariants(q,e)
    for r,((i,j),(k,l)) in enumerate(base.PAIRS):
        x=(s[i,j]+s[k,l])/2
        # This representative also has exact common-log closure on arbitrary polarization components.
        put(r,v[1]*x**4/2+v[3]*x**3,AO);put(r,v[3]*x**3,BO);put(r,v[4]*x**3,H)
    return tuple(out)


def oracle(a,b,h):
    angle=lambda i,j:base.bracket(a[i],a[j]);square=lambda i,j:base.bracket(b[i],b[j])
    inv=lambda i,j:angle(i,j)*square(i,j)
    plus=[i for i in range(4) if h[i]==1];minus=[i for i in range(4) if h[i]==-1];out=[Z]*3
    def put(r,c,v):out[r]=add(out[r],scale(c,v))
    if len(plus) in (0,4):
        S=angle if plus else square
        for (i,j),(k,l) in base.PAIRS:
            x=inv(i,j);w=inv(i,k)*inv(i,l);P=(S(i,j)*S(k,l))**2
            put(channel(i,j),P*x**4,AO);put(channel(i,j),P*x*x*w,BO)
    elif len(plus)==2:
        i,j=plus;k,l=minus;P=(angle(i,j)*square(k,l))**2;x,y,z=inv(i,j),inv(i,k),inv(i,l)
        put(channel(i,j),P*x**4,A);put(channel(i,j),P*x*x*y*z,B)
        put(channel(i,k),P*y**4,C);put(channel(i,k),P*y**3*z,D)
        put(channel(i,l),P*z**4,C);put(channel(i,l),P*z**3*y,D)
    else:
        h3=base.spinor_oracle(a,b,h)[4]
        for r,((i,j),_) in enumerate(base.PAIRS):put(r,h3*inv(i,j)**3,H)
    return tuple(out)


def combine(values,coefs):
    out=Z
    for x,c in zip(values,coefs):out=add(out,scale(x,c))
    return out


def shifts(tau):
    assert 0<tau<1
    r=[Z]*18;l=[Z]*18;even=scale(-1,add(A,C));odd=add(scale(-1,A),C)
    r[0]=scale(tau**4/4,even);r[2]=scale(tau**3/3,odd)
    r[5]=scale(tau*tau/2,even);r[8]=scale(tau,odd)
    r[1]=scale(-tau**4/4,AO);r[7]=scale(-tau*tau/4,AO)
    l[12:18]=[scale(-1,v) for v in FLOW]
    return tuple(r),tuple(l)


def mapped(values,perm):
    out=[Z]*3
    for r,((i,j),_) in enumerate(base.PAIRS):out[channel(perm[i],perm[j])]=values[r]
    return tuple(out)


def tail_bound(N,a,tau):
    assert type(N) is int and N>=6 and 0<a and 2*a<tau<1
    r=2*a;k=N-5
    return K*r**6*(r/tau)**k/(k*(1-r/tau))


def validate(c):
    assert c['schema']=='marici.photon-general-degree6-window.v1' and c['owner']=='marici.Nima'
    assert c['source_monomial_order']==list(cut.MONOMIALS)
    for k in ('generic_degree6_regular_log_window_constructed','Born2_Born4_and_Born3_square_retained',
              'full_six_direction_local_transport_derived','cut_and_scale_kernels_distinguished',
              'two_variable_generated_difference_analytic','all_eighteen_finite_matching_directions_retained'):
        assert c[k] is True,k
    for k in ('physical_matching_selected','source_identified_by_scale_transport','full_massless_amplitude_jointly_analytic',
              'all_orders_or_full_IR_inventory_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c);parents=(cut.build(),local.build(),prev.build())
    counts={k:0 for k in ('helicity','Bose','flow','Ward','forward_polynomial','forward_series','rim','R_restriction')}
    for cc,ss in ((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        a,b,q=base.cm(cc,ss);alpha=ss*ss
        for h in product((1,-1),repeat=4):
            assert coefficients(q,base.polarizations(a,b,h))==oracle(a,b,h);counts['helicity']+=1
        for i,h in enumerate(base.PHI):
            observed=coefficients(q,base.polarizations(a,b,h))[0]
            response=0 if i==0 else 1 if i==1 else 2 if i in (2,3) else 3
            angle=1-alpha if i==3 else alpha
            assert tuple(-x for x in observed)==tuple(cut.p.evaluate(case[response],angle) for case in CASES)
        for sector,source in (('c1_squared',(0,0,Q(1,4),-Q(3,4),0,0,0,0)),
                              ('c0_r4',(Q(1,4),-Q(1,4),0,0,0,Q(1,4),0,-Q(1,8)))):
            weights=tuple(source[i]*source[j] for i,j in cut.PAIRS);target=cut.archived_target(sector)
            for i,h in enumerate(base.PHI):
                r=0 if i==0 else 1 if i==1 else 2 if i in (2,3) else 3;z=1-alpha if i==3 else alpha
                assert -dot(coefficients(q,base.polarizations(a,b,h))[0],weights)==cut.p.evaluate(target[r],z)
                counts['R_restriction']+=1
    a,b,q=base.cm()
    for h in ((1,1,-1,-1),(1,1,1,1),(1,1,1,-1)):
        e=base.polarizations(a,b,h);v=coefficients(q,e)
        for perm in permutations(range(4)):
            assert mapped(coefficients(tuple(q[i] for i in perm),tuple(e[i] for i in perm)),perm)==v;counts['Bose']+=1
    comps={ix:coefficients(q,tuple(base.VECTOR_BASIS[i] for i in ix)) for ix in product(range(4),repeat=4)}
    cutmap=tuple(tuple(get(case[r],n) for case in CASES) for r in range(4) for n in range(max(len(c[r]) for c in CASES)))
    cut_kernel=base.nullspace(cutmap);flow_kernel=base.nullspace(FLOW)
    assert len(base.reduced_rows(cutmap)[1])==7 and len(base.reduced_rows(FLOW)[1])==6
    assert len(cut_kernel)==5 and len(flow_kernel)==6
    extra=next(k for k in flow_kernel if any(dot(row,k) for row in cutmap))
    assert all(dot(row,extra)==0 for row in FLOW)
    for ix,cs in comps.items():
        v=local.covariants(q,tuple(base.VECTOR_BASIS[i] for i in ix))
        assert add(add(cs[0],cs[1]),cs[2])==combine(v[12:],FLOW);counts['flow']+=1
        for k in cut_kernel:assert all(dot(x,k)==0 for x in cs)
    assert any(any(dot(x,extra) for x in cs) for cs in comps.values())
    for leg in range(4):
        for other in product(range(4),repeat=3):
            total=[Z]*3
            for k in range(4):
                ix=list(other);ix.insert(leg,k);value=comps[tuple(ix)];scalar=q[leg][k//2][k%2]
                total=[add(x,scale(scalar,y)) for x,y in zip(total,value)]
            assert total==[Z]*3;counts['Ward']+=36
    a,b,q=base.cm(Q(1),Q());cs={};vs={}
    for i,out in enumerate(cross.LABELS):
        for j,inc in enumerate(cross.LABELS):
            e=base.polarizations(a,b,inc+tuple(-h for h in out));cs[i,j]=coefficients(q,e);vs[i,j]=local.covariants(q,e)
    for k in range(12):
        Cs=[[cs[i,j][0][k] for j in range(4)] for i in range(4)];Cu=[[cs[i,j][2][k] for j in range(4)] for i in range(4)]
        assert Cu==cross.gamma(Cs) and all(cs[i,j][1][k]==0 for i,j in cs)
        absA=cross.scale(-1,Cs)
        for tau in (Q(1,4),Q(1,2),Q(3,4)):
            rational,logs=shifts(tau)
            for z in (Q(1,16),Q(-1,16),Q(1,9)):
                P=[[sum((vs[i,j][n]*rational[n][k]*z**local.DEGREES[n] for n in range(18)),Q()) for j in range(4)] for i in range(4)]
                assert P==sub.polynomial_part({6:absA},z,tau);counts['forward_polynomial']+=1
            L=[[combine(vs[i,j],logs)[k] for j in range(4)] for i in range(4)]
            assert sub.analytic_coefficient({6:absA},6,tau,Q(2))==sub.log_form(L,tau,Q(2))
            for m in range(1,6):
                expected=cross.scale(-1/(Q(m)*tau**m),cross.crossed_sum(absA,6+m))
                assert sub.analytic_coefficient({6:absA},6+m,tau,Q(1))==({None:expected} if expected!=sub.zero() else {});counts['forward_series']+=1
            for z in (tau/2,-tau/2,2*tau,-2*tau):
                expected=cross.scale(abs(z)**6,absA if z>0 else cross.scale(-1,cross.gamma(absA))) if abs(z)<tau else sub.zero()
                assert sub.residue_from_Cauchy({6:absA},z,tau)==expected;counts['rim']+=1
    assert FLOW[5][8]==Q(1,32) and FLOW[5][10]==Q(1,320)
    assert tail_bound(12,Q(1,16),Q(1,2))<Q(1,10**8)
    refused=['equate_rank6_scale_kernel_with_rank7_cut_kernel','erase_h6_from_forward_nullity',
             'reuse_odd_degree_crossing_sign','treat_monomial_kernel_as_physical_Born_equivalence']
    for key in ('physical_matching_selected','source_identified_by_scale_transport','full_massless_amplitude_jointly_analytic',
                'all_orders_or_full_IR_inventory_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported generic degree-six lift promotion: '+key)
    paths=set().union(*({ROOT/p for p in parent['source_sha256']} for parent in parents))
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    enc=lambda M:[[str(x) for x in row] for row in M]
    return {'schema':'marici.photon-general-degree6-window-receipt.v1','status':'pass',
        'scope':'generic_degree6_quadratic_two_photon_regular_log_window_not_physical_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'source_monomial_order':list(cut.MONOMIALS),'counts':counts,'common_log_flow_G6_G6prime_G6doubleprime_F6_F6prime_H6':enc(FLOW),
        'common_log_H6':'h3*(10*g3+f3)/320','mu_log_derivative_H6':'-h3*(10*g3+f3)/160',
        'cut_rank':7,'transport_rank':6,'cut_kernel':enc(cut_kernel),'transport_kernel':enc(flow_kernel),
        'transport_null_but_cut_nonzero':list(map(str,extra)),
        'local_matching_dimension':18,'local_forward_kernel_dimension':10,
        'tail_coefficient_bound_K':str(K),'tail_bound_N12_a1_16_tau_half':str(tail_bound(12,Q(1,16),Q(1,2))),
        'general_identity_and_analytic_proofs_machine_formalized':False,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    q=argparse.ArgumentParser(description=__doc__);q.add_argument('--check',action='store_true');a=q.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale generic degree-six window receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','cut_rank','transport_rank','common_log_H6','mu_log_derivative_H6','physical_matching_selected')}))

if __name__=='__main__':main()
