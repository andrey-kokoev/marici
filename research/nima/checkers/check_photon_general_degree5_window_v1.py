"""Six-coordinate general degree-five photon log/window tensor, including H5 flow."""
import argparse
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_general_degree5_cut_v1 as cut
import check_photon_degree5_window_v1 as restricted
local=restricted.local;base=local.base;sub=restricted.sub;cross=sub.cross;channel=restricted.channel
CONTRACT=HOME/'contracts/photon-general-degree5-window-v1.json';PROOF=HOME/'photon-general-degree5-window-v1.md'
TEST=HOME/'checkers/test_photon_general_degree5_window_v1.py';MANIFEST=HOME/'scc-models/photon-general-degree5-window-v1.json'
RESULT=HOME/'results/photon-general-degree5-window-v1.json'
Z=(Q(),)*6

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q())
def unit(i):return tuple(Q(int(i==j)) for j in range(6))
E=tuple(unit(i) for i in range(6))
A=add(scale(Q(1,16),E[0]),scale(Q(1,60),E[4]))
B=scale(Q(1,240),E[4])
O=add(scale(-Q(1,96),E[1]),scale(-Q(5,48),E[3]))
H=add(scale(-Q(1,80),E[2]),scale(-Q(1,480),E[5]))
FLOW=(add(scale(-Q(1,12),E[0]),scale(-Q(1,60),E[4])),
      add(scale(Q(1,16),E[0]),scale(-Q(1,240),E[4])),scale(Q(5,2),O),H)
R=(Q(1,16),Q(-3,16),Q(),Q(-1,16),Q(3,16),Q())


def coefficients(q,e):
    F,T=zip(*(base.fields(p,v) for p,v in zip(q,e)))
    s={(i,j):base.determinant(base.ma(q[i],q[j])) for i in range(4) for j in range(4) if i!=j}
    out=[Z]*3
    def put(r,c,v):out[r]=add(out[r],scale(c,v))
    for i,j in combinations(range(4),2):
        k,l=tuple(a for a in range(4) if a not in (i,j));x=(s[i,j]+s[k,l])/2
        w=(s[i,k]*s[i,l]+s[j,k]*s[j,l]+s[k,i]*s[k,j]+s[l,i]*s[l,j])/4
        P=base.contract(F[i],F[j])*base.contract(T[k],T[l])
        put(channel(i,j),-P*x**3,A);put(channel(i,j),-P*x*w,B)
        for a in (i,j):
            for b in (k,l):put(channel(a,b),P*s[a,b]**3/96,E[0])
    v=local.covariants(q,e)
    for r,((i,j),(k,l)) in enumerate(base.PAIRS):
        x=(s[i,j]+s[k,l])/2
        put(r,v[7]*x/4+v[10]/2+v[3]*x*x,O)
        put(r,v[4]*x*x,H)
    return tuple(out)


def oracle(a,b,h):
    angle=lambda i,j:base.bracket(a[i],a[j]);square=lambda i,j:base.bracket(b[i],b[j])
    inv=lambda i,j:angle(i,j)*square(i,j)
    plus=[i for i in range(4) if h[i]==1];minus=[i for i in range(4) if h[i]==-1];out=[Z]*3
    def put(r,c,v):out[r]=add(out[r],scale(c,v))
    if len(plus) in (0,4):
        C=angle if plus else square
        for (i,j),(k,l) in base.PAIRS:put(channel(i,j),(C(i,j)*C(k,l))**2*inv(i,j)**3,O)
    elif len(plus)==2:
        i,j=plus;k,l=minus;P=(angle(i,j)*square(k,l))**2;x,y,z=inv(i,j),inv(i,k),inv(i,l)
        put(channel(i,j),-P*x**3,A);put(channel(i,j),-P*x*y*z,B)
        put(channel(i,k),P*y**3/48,E[0]);put(channel(i,l),P*z**3/48,E[0])
    else:
        h3=base.spinor_oracle(a,b,h)[4]
        for r,((i,j),_) in enumerate(base.PAIRS):put(r,h3*inv(i,j)**2,H)
    return tuple(out)


def combine(values,coefs):
    out=Z
    for x,c in zip(values,coefs):out=add(out,scale(x,c))
    return out


def shifts(tau):
    assert 0<tau<1
    U=add(scale(Q(1,24),E[0]),scale(Q(1,60),E[4]))
    r=[Z]*12;l=[Z]*12
    r[0]=scale(tau**3/3,U);r[1]=scale(-tau**3/3,O)
    r[2]=scale(-tau*tau/2,FLOW[0]);r[5]=scale(tau,U);r[7]=scale(-tau/2,O)
    l[8:12]=[scale(-1,v) for v in FLOW]
    return tuple(r),tuple(l)


def mapped(values,p):
    out=[Z]*3
    for r,((i,j),_) in enumerate(base.PAIRS):out[channel(p[i],p[j])]=values[r]
    return tuple(out)


def tail_bound(N,a,tau):
    assert type(N) is int and N>=5 and 0<a and 2*a<tau<1
    r=2*a;k=N-4
    return Q(11,32)*r**5*(r/tau)**k/(k*(1-r/tau))


def validate(c):
    assert c['schema']=='marici.photon-general-degree5-window.v1' and c['owner']=='marici.Nima'
    assert c['bilinear_order']==list(cut.MONOMIALS)
    for k in ('general_regular_log_window_lift_constructed','single_minus_h5_scale_transport_derived',
              'six_source_coordinates_and_both_kernels_retained','two_variable_generated_difference_analytic'):
        assert c[k] is True,k
    for k in ('physical_couplings_selected','cut_readout_identifies_Born_source',
              'all_orders_or_full_IR_inventory_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c)
    parents=(cut.build(),local.build(),restricted.build());_,_,cases=cut.inventory()
    counts={k:0 for k in ('helicity','Bose','flow','R_restriction','Ward','forward_polynomial','forward_series','rim')}
    for cc,ss in ((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        a,b,q=base.cm(cc,ss);alpha=ss*ss
        for h in product((1,-1),repeat=4):
            e=base.polarizations(a,b,h);assert coefficients(q,e)==oracle(a,b,h);counts['helicity']+=1
        for i,h in enumerate(base.PHI):
            observed=coefficients(q,base.polarizations(a,b,h))[0]
            response=0 if i==0 else 1 if i==1 else 2 if i in (2,3) else 3
            angle=1-alpha if i==3 else alpha
            assert tuple(-x for x in observed)==tuple(cut.family.evaluate(case[response],angle) for case in cases)
    a,b,q=base.cm()
    for h in ((1,1,-1,-1),(1,1,1,1),(1,1,1,-1)):
        e=base.polarizations(a,b,h);v=coefficients(q,e)
        for p in permutations(range(4)):
            assert mapped(coefficients(tuple(q[i] for i in p),tuple(e[i] for i in p)),p)==v;counts['Bose']+=1
    comps={ix:coefficients(q,tuple(base.VECTOR_BASIS[i] for i in ix)) for ix in product(range(4),repeat=4)}
    kernel=base.nullspace(cut.coefficient_map(cases))
    assert base.nullspace(FLOW)==kernel and len(base.reduced_rows(FLOW)[1])==4
    for ix,C in comps.items():
        e=tuple(base.VECTOR_BASIS[i] for i in ix);v=local.covariants(q,e)
        assert add(add(C[0],C[1]),C[2])==combine(v[8:],FLOW);counts['flow']+=1
        assert tuple(dot(x,R) for x in C)==restricted.coefficients(q,e);counts['R_restriction']+=1
        for k in kernel:assert all(dot(x,k)==0 for x in C)
    for leg in range(4):
        for other in product(range(4),repeat=3):
            total=[Z]*3
            for k in range(4):
                ix=list(other);ix.insert(leg,k);v=comps[tuple(ix)];p=q[leg][k//2][k%2]
                total=[add(x,scale(p,y)) for x,y in zip(total,v)]
            assert total==[Z]*3;counts['Ward']+=18
    a,b,q=base.cm(Q(1),Q());C={};V={}
    for i,out in enumerate(cross.LABELS):
        for j,inc in enumerate(cross.LABELS):
            e=base.polarizations(a,b,inc+tuple(-h for h in out));C[i,j]=coefficients(q,e);V[i,j]=local.covariants(q,e)
    for k in range(6):
        Cs=[[C[i,j][0][k] for j in range(4)] for i in range(4)];Cu=[[C[i,j][2][k] for j in range(4)] for i in range(4)]
        assert Cu==cross.scale(-1,cross.gamma(Cs)) and all(C[i,j][1][k]==0 for i,j in C)
        absA=cross.scale(-1,Cs)
        for tau in (Q(1,4),Q(1,2),Q(3,4)):
            r,l=shifts(tau)
            assert tuple(dot(v,R) for v in r)==restricted.shifts(tau)[0]
            assert tuple(dot(v,R) for v in l)==restricted.shifts(tau)[1]
            for z in (Q(1,16),Q(-1,16),Q(1,9)):
                P=[[sum((V[i,j][n]*r[n][k]*z**local.DEGREES[n] for n in range(12)),Q()) for j in range(4)] for i in range(4)]
                assert P==sub.polynomial_part({5:absA},z,tau);counts['forward_polynomial']+=1
            L=[[combine(V[i,j],l)[k] for j in range(4)] for i in range(4)]
            assert sub.analytic_coefficient({5:absA},5,tau,Q(2))==sub.log_form(L,tau,Q(2))
            for m in range(1,6):
                expected=cross.scale(-1/(Q(m)*tau**m),cross.crossed_sum(absA,5+m))
                assert sub.analytic_coefficient({5:absA},5+m,tau,Q(1))==({None:expected} if expected!=sub.zero() else {});counts['forward_series']+=1
            for z in (tau/2,-tau/2,2*tau,-2*tau):
                expected=cross.scale(abs(z)**5,absA if z>0 else cross.scale(-1,cross.gamma(absA))) if abs(z)<tau else sub.zero()
                assert sub.residue_from_Cauchy({5:absA},z,tau)==expected;counts['rim']+=1
    assert FLOW[3][2]==-Q(1,80) and FLOW[3][5]==-Q(1,480)
    assert all(dot(v,R)==0 for v in (FLOW[3],))
    assert tail_bound(12,Q(1,16),Q(1,2))<Q(1,10**9)
    refused=['erase_induced_H5_scale_direction','quotient_source_kernel_as_Born_equivalence','confuse_local_forward_kernel_with_cut_source_kernel']
    for key in ('physical_couplings_selected','cut_readout_identifies_Born_source',
                'all_orders_or_full_IR_inventory_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported general-lift promotion: '+key)
    paths=set().union(*({ROOT/p for p in parent['source_sha256']} for parent in parents))
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    enc=lambda A:[[str(x) for x in row] for row in A]
    return {'schema':'marici.photon-general-degree5-window-receipt.v1','status':'pass',
        'scope':'general_real_parity_even_degree5_quadratic_two_photon_log_window_not_physical_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'bilinear_order':list(cut.MONOMIALS),'counts':counts,'scale_flow_G5_G5prime_F5_H5':enc(FLOW),
        'h5_scale_coefficient':'-h3*(6*g2+f2)/480','source_kernel':enc(kernel),
        'cut_source_dimension':6,'cut_readout_rank':4,'local_matching_dimension':12,'local_forward_kernel_dimension':6,
        'tail_bound_N12_a1_16_tau_half':str(tail_bound(12,Q(1,16),Q(1,2))),
        'general_identity_proofs_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale general degree-five window receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','counts','h5_scale_coefficient','cut_readout_rank','physical_couplings_selected')}))

if __name__=='__main__':main()
