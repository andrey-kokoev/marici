"""Regular odd-degree R2/R3 log/window tensor, with all local matching retained."""
import argparse
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_local_degree5_v1 as local
import check_photon_degree5_cut_v1 as audit
import check_photon_window_lift_v1 as prev
base=local.base;sub=prev.sub;cross=sub.cross;channel=prev.loop.channel
CONTRACT=HOME/'contracts/photon-degree5-window-v1.json';PROOF=HOME/'photon-degree5-window-v1.md'
TEST=HOME/'checkers/test_photon_degree5_window_v1.py';MANIFEST=HOME/'scc-models/photon-degree5-window-v1.json'
RESULT=HOME/'results/photon-degree5-window-v1.json'
FLOW=(Q(-1,120),Q(1,320),Q(65,3072),Q()) # G5,G5prime,F5,H5


def coefficients(q,e):
    F,T=zip(*(base.fields(p,v) for p,v in zip(q,e)))
    sij={(i,j):base.determinant(base.ma(q[i],q[j])) for i in range(4) for j in range(4) if i!=j}
    out=[Q()]*3
    for i,j in combinations(range(4),2):
        k,l=tuple(a for a in range(4) if a not in (i,j));x=(sij[i,j]+sij[k,l])/2
        w=(sij[i,k]*sij[i,l]+sij[j,k]*sij[j,l]+sij[k,i]*sij[k,j]+sij[l,i]*sij[l,j])/4
        P=base.contract(F[i],F[j])*base.contract(T[k],T[l])
        out[channel(i,j)]-=P*(9*x**3+x*w)/1280
        for a in (i,j):
            for b in (k,l):out[channel(a,b)]+=P*sij[a,b]**3/1536
    v=local.covariants(q,e)
    for r,((i,j),(k,l)) in enumerate(base.PAIRS):
        x=(sij[i,j]+sij[k,l])/2
        out[r]+=Q(13,1536)*(v[7]*x/4+v[10]/2+v[3]*x*x)
    return tuple(out)


def oracle(a,b,h):
    A=lambda i,j:base.bracket(a[i],a[j]);B=lambda i,j:base.bracket(b[i],b[j]);s=lambda i,j:A(i,j)*B(i,j)
    plus=[i for i in range(4) if h[i]==1];minus=[i for i in range(4) if h[i]==-1];out=[Q()]*3
    if len(plus) in (0,4):
        C=A if plus else B
        for (i,j),(k,l) in base.PAIRS:out[channel(i,j)]+=Q(13,1536)*(C(i,j)*C(k,l))**2*s(i,j)**3
    elif len(plus)==2:
        i,j=plus;k,l=minus;P=(A(i,j)*B(k,l))**2;x,y,z=s(i,j),s(i,k),s(i,l)
        out[channel(i,j)]-=P*(9*x**3+x*y*z)/1280
        out[channel(i,k)]+=P*y**3/768;out[channel(i,l)]+=P*z**3/768
    return tuple(out)


def shifts(tau):
    assert 0<tau<1
    r=[Q()]*12;l=[Q()]*12
    r[0]=11*tau**3/5760;r[1]=-13*tau**3/4608;r[2]=tau*tau/240
    r[5]=11*tau/1920;r[7]=-13*tau/3072
    l[8:12]=[-x for x in FLOW]
    return tuple(r),tuple(l)


def combine(values,coeff):return sum((x*y for x,y in zip(values,coeff)),Q())


def window_terms(q,e,tau):
    C=coefficients(q,e);r,l=shifts(tau);v=local.covariants(q,e)
    return C,tuple(-x for x in C),combine(v,r),combine(v,l)


def mapped(values,p):
    out=[Q()]*3
    for r,((i,j),_) in enumerate(base.PAIRS):out[channel(p[i],p[j])]=values[r]
    return tuple(out)


def tail_bound(N,a,tau):
    assert type(N) is int and N>=5 and 0<a and 2*a<tau<1
    r=2*a;k=N-4;K=Q(13,512)
    return K*r**5*(r/tau)**k/(k*(1-r/tau))


def validate(c):
    assert c['schema']=='marici.photon-degree5-window.v1' and c['owner']=='marici.Nima'
    assert c['scope']=='coefficient_lambda_gamma_squared_r0_r1_only;R2_R3_interference'
    for k in ('regular_degree5_log_window_tensor_constructed','odd_forward_crossing_retained',
              'full_twelve_parameter_local_jet_retained','two_variable_generated_difference_analytic'):
        assert c[k] is True,k
    for k in ('general_dim10_Born_cut_inventory_derived','interference_cut_assumed_positive',
              'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c)
    parents=(local.build(),audit.build(),prev.build());cut=audit.reconstruct(audit.project(audit.born_polynomials()))
    counts={k:0 for k in ('helicity','Bose','flow','forward_polynomial','forward_series','rim','Ward')}
    for cc,ss in ((Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))):
        a,b,q=base.cm(cc,ss)
        for h in product((1,-1),repeat=4):
            e=base.polarizations(a,b,h);assert coefficients(q,e)==oracle(a,b,h);counts['helicity']+=1
        phis=[coefficients(q,base.polarizations(a,b,h))[0] for h in base.PHI]
        alpha=ss*ss;D,O,M=cut
        assert tuple(-x for x in phis)==(audit.evaluate(D,alpha),audit.evaluate(O,alpha),audit.evaluate(M,alpha),audit.evaluate(M,1-alpha),Q())
    a,b,q=base.cm()
    for h in ((1,1,-1,-1),(1,1,1,1),(1,1,1,-1)):
        e=base.polarizations(a,b,h);v=coefficients(q,e)
        for p in permutations(range(4)):
            assert mapped(coefficients(tuple(q[i] for i in p),tuple(e[i] for i in p)),p)==v;counts['Bose']+=1
    # Full component Ward and scale-flow checks, not just helicity projections.
    comps={ix:coefficients(q,tuple(base.VECTOR_BASIS[i] for i in ix)) for ix in product(range(4),repeat=4)}
    for ix,C in comps.items():
        v=local.covariants(q,tuple(base.VECTOR_BASIS[i] for i in ix))
        assert sum(C)==combine(v[8:],FLOW);counts['flow']+=1
    for leg in range(4):
        for other in product(range(4),repeat=3):
            total=[Q()]*3
            for k in range(4):
                ix=list(other);ix.insert(leg,k);p=q[leg][k//2][k%2]
                total=[x+p*y for x,y in zip(total,comps[tuple(ix)])]
            assert total==[Q()]*3;counts['Ward']+=3
    a,b,q=base.cm(Q(1),Q());C={};V={}
    for i,out in enumerate(cross.LABELS):
        for j,inc in enumerate(cross.LABELS):
            e=base.polarizations(a,b,inc+tuple(-h for h in out));C[i,j]=coefficients(q,e);V[i,j]=local.covariants(q,e)
    Cs=[[C[i,j][0] for j in range(4)] for i in range(4)];Cu=[[C[i,j][2] for j in range(4)] for i in range(4)]
    assert all(v[1]==0 for v in C.values()) and Cu==cross.scale(-1,cross.gamma(Cs))
    wrong=cross.add(Cs,cross.gamma(Cs));assert wrong[0][1]==Q(13,768)
    A=cross.scale(-1,Cs);assert A[0][0]==Q(9,1280) and A[0][1]==-Q(13,1536) and A[2][2]==-Q(1,768)
    for tau in (Q(1,4),Q(1,2),Q(3,4)):
        r,l=shifts(tau)
        for z in (Q(1,16),Q(-1,16),Q(1,9)):
            P=[[sum((V[i,j][k]*r[k]*z**local.DEGREES[k] for k in range(12)),Q()) for j in range(4)] for i in range(4)]
            assert P==sub.polynomial_part({5:A},z,tau);counts['forward_polynomial']+=1
        L=[[combine(V[i,j],l) for j in range(4)] for i in range(4)]
        for nu in (Q(1),Q(2)):
            assert sub.analytic_coefficient({5:A},5,tau,nu)==sub.log_form(L,tau,nu)
        for m in range(1,8):
            E=cross.scale(-1/(Q(m)*tau**m),cross.crossed_sum(A,5+m))
            assert sub.analytic_coefficient({5:A},5+m,tau,Q(1))==({None:E} if E!=sub.zero() else {});counts['forward_series']+=1
        for z in (tau/2,-tau/2,2*tau,-2*tau):
            expected=cross.scale(abs(z)**5,A if z>0 else cross.scale(-1,cross.gamma(A))) if abs(z)<tau else sub.zero()
            assert sub.residue_from_Cauchy({5:A},z,tau)==expected;counts['rim']+=1
    assert tail_bound(12,Q(1,16),Q(1,2))<Q(1,10**10)
    assert coefficients(q,base.polarizations(a,b,base.PHI[4]))==(Q(),)*3
    refused=['even_crossing_sign_produces_forbidden_forward_O_flow','reuse_degree4_lower_polynomial','discard_h3_h5_from_zero_family_cut']
    for key in ('general_dim10_Born_cut_inventory_derived','interference_cut_assumed_positive',
                'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
        try:validate({**c,key:True})
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported degree-five window promotion: '+key)
    paths=set().union(*({ROOT/p for p in parent['source_sha256']} for parent in parents))
    paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    r,l=shifts(Q(1,2))
    return {'schema':'marici.photon-degree5-window-receipt.v1','status':'pass',
        'scope':'regular_R2_R3_interference_log_and_window_not_general_dim10_Born_inventory',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'counts':counts,'scale_flow_G5_G5prime_F5_H5':list(map(str,FLOW)),
        'even_sign_forbidden_forward_O_flow':'13/768',
        'lower_jet_at_tau_half':{local.NAMES[i]:str(v) for i,v in enumerate(r) if v},
        'log_rho_tau_jet':{local.NAMES[i]:str(v) for i,v in enumerate(l) if v},
        'tail_bound_at_N12_a1_16_tau_half':str(tail_bound(12,Q(1,16),Q(1,2))),
        'general_analytic_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale degree-five window receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','counts','scale_flow_G5_G5prime_F5_H5','lower_jet_at_tau_half','general_dim10_Born_cut_inventory_derived')}))

if __name__=='__main__':main()
