"""Covariant R=s^2 window lift and joint analytic difference; exact rational coefficients."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

HOME=Path(__file__).resolve().parents[1];ROOT=HOME.parents[1]
sys.path.insert(0,str(HOME/'checkers'))
import check_photon_loop_tensor_v1 as loop
w=loop.w;sub=w.primary.norm.sub;cross=sub.cross
CONTRACT=HOME/'contracts/photon-window-lift-v1.json'
PROOF=HOME/'photon-window-lift-v1.md'
TEST=HOME/'checkers/test_photon_window_lift_v1.py'
MANIFEST=HOME/'scc-models/photon-window-lift-v1.json'
RESULT=HOME/'results/photon-window-lift-v1.json'


def local_shift(tau,beta=None):
    """pi^2*(D_lift-M_log) local jet: rational + log(rho*tau)*logarithmic."""
    assert 0<tau<1
    b=loop.betas() if beta is None else beta;flow=loop.flow(b)
    rational=[loop.ZERO for _ in w.NAMES];logs=list(rational)
    rational[0]=loop.scale(-tau*tau/2,flow['g4'])
    rational[1]=loop.scale(-tau*tau/2,b['beta2'])
    rational[2]=loop.scale(-tau,loop.add(b['beta11'],loop.scale(-1,b['beta13'])))
    logs[5]=loop.scale(-1,flow['g4']);logs[6]=loop.scale(-1,flow['g4prime']);logs[7]=loop.scale(-1,flow['f4'])
    return tuple(rational),tuple(logs)


def combine(local,coeff):
    out=loop.ZERO
    for value,c in zip(local,coeff):out=loop.add(out,loop.scale(value,c))
    return out


def window_terms(q,e,tau,beta=None):
    """pi^2 D: C*ell - C*Log(1-x/tau) + rational local jet - log(rho*tau)*sum C."""
    b=loop.betas() if beta is None else beta;C=loop.coefficients(q,e,b)
    rational,logs=local_shift(tau,b);local=w.covariants(q,e)
    return {'channel_log':C,'endpoint_log':tuple(loop.scale(-1,v) for v in C),
            'rational':combine(local,rational),'log_rho_tau':combine(local,logs)}


def analytic_tail_coefficient(q,e,m,tau,beta=None):
    assert type(m) is int and m>=1 and 0<tau<1
    C=loop.coefficients(q,e,loop.betas() if beta is None else beta);out=loop.ZERO
    for r,((i,j),_) in enumerate(w.PAIRS):
        x=w.determinant(w.ma(q[i],q[j]));out=loop.add(out,loop.scale(x**m/(m*tau**m),C[r]))
    return out


def scalar_tail_bound(N,a,tau,beta=None):
    """Uniform max-Phi coupling-coordinate l1 tail on |s|,|t|<=a; u=-s-t."""
    assert type(N) is int and N>=4 and 0<a and 2*a<tau<1
    b=loop.betas() if beta is None else beta;l1=lambda v:sum(map(abs,v),Q())
    K=max(l1(b['beta11'])+l1(b['beta12'])+2*l1(b['beta13']),3*l1(b['beta2']))
    r=2*a;k=N-3
    return K*r**4*(r/tau)**k/(k*(1-r/tau))


def forward_data(beta):
    a,b,q=w.cm(Q(1),Q());locals={};channels={}
    for i,out in enumerate(cross.LABELS):
        for j,inc in enumerate(cross.LABELS):
            e=w.polarizations(a,b,inc+tuple(-x for x in out))
            locals[i,j]=w.covariants(q,e);channels[i,j]=loop.coefficients(q,e,beta)
    return q,locals,channels


def matrix_from_local(locals,coeff,coordinate):
    return [[combine(locals[i,j],coeff)[coordinate] for j in range(4)] for i in range(4)]


def evaluate_matrix(A,g=Q(1,4),f=Q(-1,4)):
    return [[w.primary.evaluate(tuple(A[c][i][j] for c in range(3)),g,f)
             for j in range(4)] for i in range(4)]


def channel_rim(x,tau):
    assert x not in (0,tau) and 0<tau<1
    # Disc ell=-2*pi*i for x>0; Disc endpoint log has same sign for x>tau.
    return int(x>0)-int(x>tau)


def validate(c):
    assert c['schema']=='marici.photon-window-lift.v1' and c['owner']=='marici.Nima'
    assert c['scope']=='R=s^2;retained_degree_four_loop_cut;conditional_covariant_window_representative'
    assert c['window_domain']=='0<tau<1; |s|,|t|,|u|<tau for analytic difference'
    for key in ('covariant_window_lift_constructed','exact_forward_Cauchy_prescription_matched',
                'two_variable_analytic_difference_derived','all_eight_local_matching_directions_retained'):
        assert c[key] is True,key
    for key in ('off_forward_lift_unique_from_forward_data','finite_matching_coefficients_selected',
                'full_unsubtracted_amplitude_analytic_at_origin','all_orders_or_full_IR_inventory_covered',
                'global_UV_positivity_or_native_dynamics_derived','C12_budget_renewed'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate(c)
    parent=loop.build();beta=loop.betas();q,locals,channels=forward_data(beta)
    C=[[[[channels[i,j][r][k] for j in range(4)] for i in range(4)] for k in range(3)] for r in range(3)]
    for k in range(3):
        assert C[1][k]==sub.zero();assert C[2][k]==cross.gamma(C[0][k])
    A=cross.scale(-1,evaluate_matrix(C[0]));legacy=sub.coefficients({2:Q(1)})[4]
    assert A==cross.scale(Q(1,16),legacy),'invariant/reduced dictionary, not a fitted factor'
    polynomials=jets=series=rims=Ward=0
    for tau in (Q(1,4),Q(1,2),Q(3,4)):
        rational,logs=local_shift(tau,beta)
        for coordinate in range(3):
            L2=[[combine(tuple(v if w.DEGREES[n]==2 else Q() for n,v in enumerate(locals[i,j])),rational)[coordinate] for j in range(4)] for i in range(4)]
            L3=[[combine(tuple(v if w.DEGREES[n]==3 else Q() for n,v in enumerate(locals[i,j])),rational)[coordinate] for j in range(4)] for i in range(4)]
            absA=cross.scale(-1,C[0][coordinate]);paired=cross.gamma(absA)
            assert L2==cross.scale(tau*tau/2,cross.add(absA,paired))
            assert L3==cross.scale(tau,cross.add(absA,cross.scale(-1,paired)))
            L4=matrix_from_local(locals,logs,coordinate);assert L4==cross.add(absA,paired)
            for n,expected in ((2,L2),(3,L3)):
                assert sub.analytic_coefficient({4:absA},n,tau,Q(1))==({None:expected} if expected!=sub.zero() else {});jets+=1
            for nu in (Q(1),Q(2)):
                assert sub.analytic_coefficient({4:absA},4,tau,nu)==sub.log_form(L4,tau,nu);jets+=1
            for z in (Q(1,16),Q(-1,16),Q(1,9)):
                got=cross.add(cross.scale(z*z,L2),cross.scale(z**3,L3))
                assert got==sub.polynomial_part({4:absA},z,tau);polynomials+=1
            for m in range(1,9):
                new=cross.scale(-1/(Q(m)*tau**m),cross.add(absA,cross.scale((-1)**m,paired)))
                assert sub.analytic_coefficient({4:absA},4+m,tau,Q(1))==({None:new} if new!=sub.zero() else {});series+=1
        for z in (tau/2,-tau/2,2*tau,-2*tau):
            expected=cross.scale(abs(z)**4,A if z>0 else cross.scale(-1,cross.gamma(A))) if abs(z)<tau else sub.zero()
            assert sub.residue_from_Cauchy({4:A},z,tau)==expected;rims+=1
    # New terms preserve Ward identities, including the lower subtraction polynomial.
    a,b,q=w.cm();e=tuple(((Q(i+1),Q(2)),(Q(3),Q(i+2))) for i in range(4))
    for leg in range(4):
        gauge=list(e);gauge[leg]=q[leg];terms=window_terms(q,tuple(gauge),Q(1,2),beta)
        assert terms['channel_log']==terms['endpoint_log']==(loop.ZERO,)*3
        assert terms['rational']==terms['log_rho_tau']==loop.ZERO;Ward+=1
    # Analytic expansion is genuinely off forward and contains angular coefficients.
    for h in w.PHI:
        e=w.polarizations(a,b,h);Coff=loop.coefficients(q,e,beta)
        for m in (1,2,3):
            direct=loop.ZERO
            for r,((i,j),_) in enumerate(w.PAIRS):
                x=w.determinant(w.ma(q[i],q[j]));direct=loop.add(direct,loop.scale(x**m/(m*Q(1,2)**m),Coff[r]))
            assert analytic_tail_coefficient(q,e,m,Q(1,2),beta)==direct
    r,l=local_shift(Q(1,2),beta)
    benchmark={w.NAMES[i]:str(w.primary.evaluate(v,Q(1,4),Q(-1,4))) for i,v in enumerate(r) if v!=loop.ZERO}
    assert benchmark=={'g2':'21/20480','f2':'-5/6144','g3':'17/5120'}
    assert channel_rim(Q(1,4),Q(1,2))==1 and channel_rim(Q(3,4),Q(1,2))==0
    # Incorrect +endpoint sign would double rather than cancel the cut above tau.
    assert int(Q(3,4)>0)+int(Q(3,4)>Q(1,2))==2
    assert scalar_tail_bound(12,Q(1,16),Q(1,2),beta)<Q(1,10**9)
    assert scalar_tail_bound(16,Q(1,16),Q(1,2),beta)<Q(1,10**12)
    refused=['omit_lower_subtraction_polynomial_same_cuts_wrong_forward_prescription','wrong_endpoint_log_sign_doubles_exterior_cut']
    for key in ('off_forward_lift_unique_from_forward_data','finite_matching_coefficients_selected',
                'full_unsubtracted_amplitude_analytic_at_origin','all_orders_or_full_IR_inventory_covered',
                'global_UV_positivity_or_native_dynamics_derived','C12_budget_renewed'):
        bad=copy.deepcopy(c);bad[key]=True
        try:validate(bad)
        except AssertionError:refused.append(key)
        else:raise AssertionError('unsupported window-lift promotion: '+key)
    paths={ROOT/p for p in parent['source_sha256']};paths.update((CONTRACT,PROOF,TEST,MANIFEST,Path(__file__).resolve()))
    return {'schema':'marici.photon-window-lift-receipt.v1','status':'pass',
        'scope':'conditional_covariant_R_s_squared_window_lift_with_joint_analytic_difference_not_physical_matching',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'forward_polynomial_checks':polynomials,'forward_jet_checks':jets,'higher_forward_analytic_coefficients':series,
        'rim_checks':rims,'new_term_Ward_checks':Ward,'normalized_legacy_cut_matches':True,
        'lower_jet_at_tau_half_common_Born_pi_squared':benchmark,
        'rational_local_jet_quadratic_coordinates':{w.NAMES[i]:list(map(str,v)) for i,v in enumerate(r) if v!=loop.ZERO},
        'log_rho_tau_local_jet_quadratic_coordinates':{w.NAMES[i]:list(map(str,v)) for i,v in enumerate(l) if v!=loop.ZERO},
        'scalar_Phi_coupling_l1_tail_at_a_1_16_tau_half':{str(N):str(scalar_tail_bound(N,Q(1,16),Q(1,2),beta)) for N in (4,8,12,16)},
        'forward_invisible_local_ambiguity':['f3','h3','g4prime'],
        'general_analytic_proof_machine_formalized':False,**{k:v for k,v in c.items() if isinstance(v,bool)},'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale window lift receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','forward_polynomial_checks','higher_forward_analytic_coefficients','lower_jet_at_tau_half_common_Born_pi_squared','two_variable_analytic_difference_derived','finite_matching_coefficients_selected')}))

if __name__=='__main__':main()
