"""Regular covariant degree-four photon log tensor; exact channel/coupling coefficients."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_local_ward_basis_v1 as w
import pentachoron_exact as exact
CONTRACT=HOME/'contracts/photon-loop-tensor-v1.json'
PROOF=HOME/'photon-loop-tensor-v1.md'
TEST=HOME/'checkers/test_photon_loop_tensor_v1.py'
MANIFEST=HOME/'scc-models/photon-loop-tensor-v1.json'
RESULT=HOME/'results/photon-loop-tensor-v1.json'
ZERO=(Q(),)*3


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def channel(i,j):
    I=tuple(sorted((i,j)));J=tuple(k for k in range(4) if k not in I)
    return next(n for n,(A,B) in enumerate(w.PAIRS) if {I,J}=={A,B})


def betas():
    return w.primary.parse_primary_betas(w.primary.load_primary()[2])


def coefficients(q,e,beta=None):
    """pi^2 M_log = sum_r coefficients[r] ell_r; each entry is (g^2,g*f,f^2)."""
    beta=betas() if beta is None else beta
    F,T=zip(*(w.fields(p,v) for p,v in zip(q,e)))
    s={(i,j):w.determinant(w.ma(q[i],q[j])) for i in range(4) for j in range(4) if i!=j}
    x=lambda i,j,k,l:(s[i,j]+s[k,l])/2
    cross=lambda i,j,k,l:(s[i,k]*s[i,l]+s[j,k]*s[j,l]+s[k,i]*s[k,j]+s[l,i]*s[l,j])/4
    out=[ZERO for _ in range(3)]
    def put(r,c,b):out[r]=add(out[r],scale(c,b))
    for i,j in combinations(range(4),2):
        k,l=tuple(a for a in range(4) if a not in (i,j));X=x(i,j,k,l)
        P=w.contract(F[i],F[j])*w.contract(T[k],T[l])
        put(channel(i,j),P*X*X,beta['beta11']);put(channel(i,j),P*cross(i,j,k,l),beta['beta12'])
        for a in (i,j):
            for b in (k,l):put(channel(a,b),P*s[a,b]*s[a,b]/2,beta['beta13'])
    # The F3 generator is needed for a regular all-same-helicity lift on S2=0.
    local_F2=Q();local_F3=Q();xs=[]
    for (i,j),(k,l) in w.PAIRS:
        X=x(i,j,k,l);xs.append(X)
        P=w.contract(F[i],F[j])*w.contract(F[k],F[l])+w.contract(T[i],T[j])*w.contract(T[k],T[l])
        local_F2+=P;local_F3+=X*P/3
    for r,X in enumerate(xs):put(r,local_F2*X*X/2+local_F3*X,beta['beta2'])
    return tuple(out)


def oracle(a,b,h,beta):
    A=lambda i,j:w.bracket(a[i],a[j]);B=lambda i,j:w.bracket(b[i],b[j]);inv=lambda i,j:A(i,j)*B(i,j)
    plus=[i for i in range(4) if h[i]==1];minus=[i for i in range(4) if h[i]==-1];out=[ZERO for _ in range(3)]
    def put(r,c,v):out[r]=add(out[r],scale(c,v))
    if len(plus) in (0,4):
        C=A if plus else B
        for (i,j),(k,l) in w.PAIRS:
            X=inv(i,j);P=C(i,j)*C(k,l);put(channel(i,j),P*P*X*X,beta['beta2'])
    elif len(plus)==2:
        i,j=plus;k,l=minus;P=(A(i,j)*B(k,l))**2;X,Y,Z=inv(i,j),inv(i,k),inv(i,l)
        put(channel(i,j),P*X*X,beta['beta11']);put(channel(i,j),P*Y*Z,beta['beta12'])
        put(channel(i,k),P*Y*Y,beta['beta13']);put(channel(i,l),P*Z*Z,beta['beta13'])
    return tuple(out)


def rows(c=Q(3,5),s=Q(4,5),beta=None):
    a,b,q=w.cm(c,s);beta=betas() if beta is None else beta
    return tuple(coefficients(q,w.polarizations(a,b,h),beta) for h in w.PHI)


def mapped_channels(values,p):
    result=[ZERO for _ in range(3)]
    for r,((i,j),_) in enumerate(w.PAIRS):result[channel(p[i],p[j])]=values[r]
    return tuple(result)


def flow(beta):
    return {'g4':add(beta['beta11'],beta['beta13']),
            'g4prime':add(beta['beta12'],scale(-2,beta['beta13'])),
            'f4':scale(Q(1,2),beta['beta2'])}


def complex_S2_control(beta):
    # omega^2+omega+1=0. No approximate complex numbers or square-root patch.
    om=(exact.parse('-1')+exact.parse('I')*exact.radical(3))/2;om2=om*om
    assert om2+om+1==0
    F=exact.F;a=((F(1),F()),(F(),F(1)),(F(1),F(1)),(F(1),-om))
    b=((F(1),F()),(F(),F(1)),(om2,om),(om,-om))
    q=tuple(w.outer(u,v) for u,v in zip(a,b));assert w.ma(w.ma(q[0],q[1]),w.ma(q[2],q[3]))==w.Z
    assert all(w.determinant(p)==0 for p in q)
    xs=tuple(w.determinant(w.ma(q[i],q[j])) for (i,j),_ in w.PAIRS)
    assert xs==(F(1),om,om2) and sum((x*x for x in xs),F())==0
    e=[]
    for u,v in zip(a,b):
        ref=w.reference(v);e.append(w.ms(exact.inverse(w.bracket(v,ref)),w.outer(u,ref)))
    ff,tt=zip(*(w.fields(p,v) for p,v in zip(q,e)))
    f2=sum((w.contract(ff[i],ff[j])*w.contract(ff[k],ff[l]) for (i,j),(k,l) in w.PAIRS),F())
    assert f2==0
    actual=coefficients(q,tuple(e),beta)
    assert actual[0]==(F(),-Q(5,48)*om,F()) and actual[0][1]!=0
    return {'invariants':['1','omega','omega^2'],'omega_minimal_polynomial':'omega^2+omega+1',
            'S2':'0','local_F2_helicity_projection':'0','s_log_gf_coefficient_in_Q_sqrt2_sqrt3_sqrt5_i':actual[0][1].encoded(),
            's_log_gf_coefficient':'-5*omega/48','regular_F2_only_scalar_lift_refuted':True}


def validate(c):
    assert c['schema']=='marici.photon-loop-tensor.v1' and c['owner']=='marici.Nima'
    assert c['logarithm_boundary']=='Log(-rho*s-i0)=log(rho*s)-i*pi; rho>0'
    assert c['quadratic_basis']==['g2_gamma^2','g2_gamma*f2_gamma','f2_gamma^2']
    for k in ('degree_four_log_tensor_constructed','all_helicities_and_channel_coefficients_matched',
              'no_rational_kinematic_denominators_introduced','all_eight_local_matching_coefficients_retained'):
        assert c[k] is True,k
    for k in ('window_shift_lift_constructed','full_amplitude_analytic_at_massless_origin',
              'finite_matching_coefficients_selected','native_preparation_or_physical_rates_derived','UV_completion_constructed'):
        assert c[k] is False,k


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c)
    upstream=w.build();beta=betas();w.primary.assert_primary_matches(beta)
    counts={k:0 for k in ('helicity','reference','Bose','Ward','Lorentz','parity','flow')}
    for cc,ss in ((Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(1),Q()),(Q(),Q(1))):
        a,b,q=w.cm(cc,ss)
        for h in product((1,-1),repeat=4):
            e=w.polarizations(a,b,h);value=coefficients(q,e,beta)
            assert value==oracle(a,b,h,beta);counts['helicity']+=1
            assert value==coefficients(q,w.polarizations(a,b,h,True),beta);counts['reference']+=1
    a,b,q=w.cm();f=flow(beta)
    for h in ((1,1,-1,-1),(1,1,1,1),(1,1,1,-1)):
        e=w.polarizations(a,b,h);value=coefficients(q,e,beta)
        for p in permutations(range(4)):
            moved=coefficients(tuple(q[i] for i in p),tuple(e[i] for i in p),beta)
            assert mapped_channels(moved,p)==value;counts['Bose']+=1
        for leg in range(4):
            gauge=list(e);gauge[leg]=q[leg];assert coefficients(q,tuple(gauge),beta)==(ZERO,)*3;counts['Ward']+=1
        assert coefficients(tuple(map(w.transpose,q)),tuple(map(w.transpose,e)),beta)==value;counts['parity']+=1
        L=((Q(1),Q(1)),(Q(),Q(1)));R=((Q(1),Q()),(Q(1),Q(1)))
        move=lambda M:w.mm(w.mm(L,M),w.transpose(R))
        assert coefficients(tuple(map(move,q)),tuple(map(move,e)),beta)==value;counts['Lorentz']+=1
    components={ix:coefficients(q,tuple(w.VECTOR_BASIS[i] for i in ix),beta) for ix in product(range(4),repeat=4)}
    constraints=0
    for leg in range(4):
        for other in product(range(4),repeat=3):
            total=[ZERO for _ in range(3)]
            for k in range(4):
                ix=list(other);ix.insert(leg,k);v=components[tuple(ix)];p=q[leg][k//2][k%2]
                total=[add(x,scale(p,y)) for x,y in zip(total,v)]
            assert total==[ZERO]*3;constraints+=9
    # Flow is checked on every uncontracted tensor component, not just physical polarizations.
    for ix,vs in components.items():
        local=w.covariants(q,tuple(w.VECTOR_BASIS[i] for i in ix))
        expected=add(add(scale(local[5],f['g4']),scale(local[6],f['g4prime'])),scale(local[7],f['f4']))
        assert add(add(vs[0],vs[1]),vs[2])==expected;counts['flow']+=1
    forward=rows(Q(1),Q(),beta);cut=tuple(-w.primary.evaluate(forward[i][0],Q(1,4),Q(-1,4)) for i in (0,1,2))
    assert cut==w.primary.forward_abs(beta,Q(1,4),Q(-1,4))
    bad=copy.deepcopy(beta);bad['beta12']=scale(2,bad['beta12'])
    assert rows(Q(1),Q(),bad)==forward
    delta=add(rows(beta=bad)[0][0],scale(-1,rows(beta=beta)[0][0]));assert delta==(Q(),Q(),Q(3,3125))
    assert all(x==ZERO for x in rows(beta=beta)[4]) # loop Phi5=0 does not constrain local h3
    control=complex_S2_control(beta)
    refused=['doubled_beta12_forward_only_comparison','opposite_logarithm_rim_sign','regular_F2_only_scalar_form_factor']
    for key in ('window_shift_lift_constructed','full_amplitude_analytic_at_massless_origin',
                'finite_matching_coefficients_selected','native_preparation_or_physical_rates_derived','UV_completion_constructed'):
        bad_c=copy.deepcopy(c);bad_c[key]=True
        try:validate(bad_c)
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported loop-tensor promotion: '+key)
    paths={ROOT/p for p in upstream['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve(),Path(exact.__file__).resolve()))
    return {'schema':'marici.photon-loop-tensor-receipt.v1','status':'pass',
        'scope':'regular_on_shell_local_plus_degree_four_log_tensor_with_source_cuts_not_window_matching_or_native_dynamics',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'counts':counts,'component_Ward_scalar_constraints':constraints,'formal_log_channel_count':3,'quadratic_coupling_count':3,
        'pi_squared_scale_flow':{k:list(map(str,v)) for k,v in f.items()},
        'pi_times_forward_absorptive_D_O_M_at_common_Born':list(map(str,cut)),
        'doubled_beta12_off_forward_f_squared_residual':str(delta[2]),'complex_S2_zero_control':control,
        **{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale loop tensor receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','counts','component_Ward_scalar_constraints','pi_squared_scale_flow','window_shift_lift_constructed')}))

if __name__=='__main__':main()
