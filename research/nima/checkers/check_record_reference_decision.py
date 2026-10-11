"""Constructive reference compatibility and conservative full-record decisions.
All norms are entrywise L1. Synthetic perturbations are not measured trials.
uv run --with sympy python research/nima/checkers/check_record_reference_decision.py
"""
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import runpy
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
CONTRACT = OWNER/'contracts/record-reference-decision.v1.json'
OUT = OWNER/'results/record-reference-decision.json'
MODELS = ('P', *(''.join(map(str,v)) for v in product((0,1),repeat=3)))
REFS = ('B','A','00','11')
CHECKS = []


def require(name, value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)


def clean(x):
    if isinstance(x,s.MatrixBase):
        return [[str(a) for a in row] for row in x.tolist()]
    if isinstance(x,s.Basic):
        return str(x)
    if isinstance(x,dict):
        return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [clean(v) for v in x]
    return x


def decode(x):
    return s.Matrix([[s.Rational(a) for a in row] for row in x])


def norm(M):
    return sum(abs(x) for x in M)


def valid(P,n):
    return P.shape == (n,1) and all(x.is_Rational and x >= 0 for x in P) and sum(P) == 1


def center(M):
    return M-(M*s.ones(3,1))*(s.ones(1,3)*M)


def reflect(M):
    return M-2*center(M)


def tensor(z,M,port):
    return s.Matrix([z[a]*M[r,b] if port == 'A' else z[b]*M[r,a]
                     for r,a,b in product(range(3),repeat=3)])


def views(data):
    def pair(P,port):
        return s.Matrix(3,3,lambda r,j:sum(P[9*r+3*j+k] if port=='A' else P[9*r+3*k+j] for k in range(3)))
    def marginal(P,port):
        return s.Matrix([sum(P[3*j+k] if port=='A' else P[3*k+j] for k in range(3)) for j in range(3)])
    MA,MB = pair(data['A'],'A'),pair(data['B'],'B')
    az = [marginal(data[k],'A') for k in ('00','11')]
    bz = [marginal(data[k],'B') for k in ('00','11')]
    return MA,MB,az,bz


def predict(data,model):
    MA,MB,az,bz = views(data)
    if model == 'P':
        return tensor(az[0],reflect(MB),'A'),tensor(bz[0],MA,'B')
    h,a,b = map(int,model)
    return (tensor(az[a],reflect(MB) if h ^ b else MB,'A'),
            tensor(bz[b],reflect(MA) if h ^ a else MA,'B'))


def closure_residuals(data):
    MA,MB,az,bz = views(data)
    return {'basis_00':norm(data['00']-s.kronecker_product(az[0],bz[0])),
            'basis_11':norm(data['11']-s.kronecker_product(az[1],bz[1])),
            'bypass_B':norm(data['B']-tensor(az[0],MB,'A')),
            'bypass_A':norm(data['A']-tensor(bz[0],MA,'B')),
            'herald_mean':norm((MA-MB)*s.ones(3,1))}


def compatible(data):
    """Necessary and sufficient EXACT test, with a nonunique channel witness."""
    if set(data) != set(REFS) or not all(valid(data[k],9 if k in ('00','11') else 27) for k in REFS):
        return {'status':'invalid_input'}
    residuals = closure_residuals(data)
    for gate,residual in residuals.items():
        if residual != 0:
            return {'status':'incompatible','gate':gate,'residual':residual}
    MA,MB,az,bz = views(data)
    H = center(MA).row_join(center(MB))
    rank = H.rank()
    if rank > 1:
        return {'status':'incompatible','gate':'shared_covariance_rank','rank':rank}
    for key,M in (('A',MA),('B',MB)):
        if any(x < 0 for x in reflect(M)):
            return {'status':'incompatible','gate':'negative_reflection_'+key,'reflection':reflect(M)}
    mu = MA*s.ones(3,1)
    na,nb = MA.T*s.ones(3,1),MB.T*s.ones(3,1)
    interval = None
    if rank == 0:
        u,va,vb = s.zeros(3,1),s.zeros(3,1),s.zeros(3,1)
    else:
        j = next(j for j in range(6) if H[:,j] != s.zeros(3,1))
        u0 = H[:,j]
        i = next(i for i in range(3) if u0[i] != 0)
        w = H[i,:].T/u0[i]
        nu = na.col_join(nb)
        require('zero-support-coefficient', all(w[k] == 0 for k in range(6) if nu[k] == 0))
        lower = max(abs(w[k])/nu[k] for k in range(6) if nu[k] != 0)
        upper = min(mu[k]/abs(u0[k]) for k in range(3) if u0[k] != 0)
        require('constructive-scale-interval', 0 < lower <= upper)
        interval = (lower,upper)
        u,va,vb = lower*u0,w[:3,0]/lower,w[3:,0]/lower
    channels = {'K':s.Matrix.hstack(mu+u,mu-u),
                'AX':s.Matrix.hstack(na-va,na+va),'BX':s.Matrix.hstack(nb-vb,nb+vb),
                'AZ':s.Matrix.hstack(az[1],az[0]),'BZ':s.Matrix.hstack(bz[1],bz[0])}
    require('witness-column-stochastic', all(s.ones(1,3)*R == s.ones(1,2) and all(x >= 0 for x in R) for R in channels.values()))
    return {'status':'compatible','rank':rank,'scale_interval':interval,'channels':channels}


def reference_region(data,eps):
    """Sound outer tests, not a complete finite-radius feasibility solver."""
    exact = compatible(data)
    if exact['status'] == 'invalid_input':
        return {'status':'invalid_input','point':exact}
    limits = {'basis_00':3*eps['00'],'basis_11':3*eps['11'],
              'bypass_B':2*eps['B']+eps['00'],'bypass_A':2*eps['A']+eps['00'],
              'herald_mean':eps['A']+eps['B']}
    violations = [k for k,v in closure_residuals(data).items() if v > limits[k]]
    MA,MB,_,_ = views(data)
    for key,M in (('A',MA),('B',MB)):
        if 2*sum(-x for x in reflect(M) if x < 0) > 5*eps[key]:
            violations.append('negative_reflection_'+key)
    H = center(MA).row_join(center(MB))
    for rows,cols in product(combinations(range(3),2),combinations(range(6),2)):
        bound = 6*sum(eps['A' if j < 3 else 'B'] for j in cols)
        if abs(H.extract(rows,cols).det()) > bound:
            violations.append('shared_covariance_minor_'+str((rows,cols)))
    status = 'excluded' if violations else 'witnessed_feasible' if exact['status']=='compatible' else 'unresolved'
    return {'status':status,'point':exact,'violations':violations}


def prepare_rule(data,eps):
    if set(eps) != set(REFS) or any(not s.sympify(x).is_Rational or x < 0 for x in eps.values()):
        raise ValueError('nonnegative rational reference errors required')
    region = reference_region(data,eps)
    if region['status'] in ('excluded','invalid_input'):
        return {'reference_region':region,'models':{}}
    models = {}
    for m in MODELS:
        if m == 'P':
            dt,ds = eps['00']+5*eps['B'],eps['00']+eps['A']
        else:
            h,a,b = map(int,m)
            dt = eps['11' if a else '00']+(1+4*(h ^ b))*eps['B']
            ds = eps['11' if b else '00']+(1+4*(h ^ a))*eps['A']
        models[m] = {'prediction':predict(data,m),'reference_bounds':(dt,ds)}
    return {'reference_region':region,'models':models}


def evaluate(rule,trials,errors):
    if len(trials)!=2 or not all(valid(P,27) for P in trials):
        raise ValueError('two complete probability tables required')
    if len(errors)!=2 or any(not s.sympify(x).is_Rational or x < 0 for x in errors):
        raise ValueError('nonnegative rational test errors required')
    results = {}
    for m,row in rule['models'].items():
        residuals = [norm(P-Q) for P,Q in zip(trials,row['prediction'])]
        bounds = [x+y for x,y in zip(errors,row['reference_bounds'])]
        results[m] = {'residuals':residuals,'bounds':bounds,
                      'status':'rejected' if any(x > y for x,y in zip(residuals,bounds)) else 'not_excluded'}
    return {'reference_region_status':rule['reference_region']['status'],'candidates':results,
            'not_excluded':[m for m,row in results.items() if row['status']=='not_excluded']}


def separation_certificate(rule,errors,target='P'):
    if target not in rule['models']:
        return {'all_rivals_separated':False,'gaps':{}}
    base = rule['models'][target]
    gaps = {}
    for m,row in rule['models'].items():
        if m == target:
            continue
        gap = sum(norm(P-Q) for P,Q in zip(base['prediction'],row['prediction']))
        threshold = 2*sum(errors)+sum(base['reference_bounds'])+sum(row['reference_bounds'])
        gaps[m] = {'gap':gap,'threshold':threshold,'separated':bool(gap > threshold)}
    return {'all_rivals_separated':all(v['separated'] for v in gaps.values()),'gaps':gaps}


def iid_radius(d,n,alpha):
    if not isinstance(d,int) or d < 1 or not isinstance(n,int) or n < 1 or not 0 < alpha < 1:
        raise ValueError('positive cell/trial counts and alpha in (0,1) required')
    return s.Min(2,d*s.sqrt(s.log(2*d/alpha)/(2*n)))


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    contract = json.loads(CONTRACT.read_text())
    paths = {k:REPO/p for k,p in contract['source'].items()}
    inputs = [Path(__file__).resolve(),CONTRACT,*paths.values()]
    before = {p:p.read_bytes() for p in inputs}
    parent = json.loads(paths['receipt'].read_text())
    require('current-source-bound-parent', parent['status']=='pass' and all(
        hashlib.sha256((REPO/p).read_bytes()).hexdigest()==h for p,h in parent['source_sha256'].items()))
    old = runpy.run_path(str(paths['checker']))
    ideals = {k:decode(row['records']) for k,row in parent['native_ideal_packets'].items()}
    def native(ch,key,model='P'):
        basis = key in ('00','11')
        axes = ('X','Z') if key in ('A','S0','SP') else ('Z','Z') if basis else ('Z','X')
        h,a,b = (0,0,0) if model=='P' or key in REFS else tuple(map(int,model))
        A,B = ch['A'+axes[0]]*old['J']**a,ch['B'+axes[1]]*old['J']**b
        L = s.kronecker_product(A,B) if basis else s.kronecker_product(ch['K']*old['J']**h,A,B)
        return L*ideals[key]
    def calibration(ch):
        return {k:native(ch,k) for k in REFS}
    def probes(ch,m):
        return (native(ch,'TP'),native(ch,'SP')) if m=='P' else (native(ch,'T0',m),native(ch,'S0',m))
    def perturbed(P,index,t):
        e = s.zeros(P.rows,1); e[index % P.rows] = 1
        return (1-t)*P+t*e
    zero = dict.fromkeys(REFS,s.S.Zero)
    t = s.Rational(contract['perturbation']['strength'])
    budget = s.Rational(contract['perturbation']['uniform_error_budget'])
    require('preregistered-perturbation-envelope', budget == 2*t)
    cases = []; true_model_tests = 0; comparison_tests = 0
    for case_index,row in enumerate(parent['census']):
        data = {k:decode(P) for k,P in row['calibration'].items()}
        actual = {'P':tuple(decode(P) for P in row['projective_probes'])}
        actual.update({''.join(map(str,v['mask'])):(decode(v['twist']),decode(v['swap'])) for v in row['actions']})
        exact = prepare_rule(data,zero)
        require('all-strata-compatible', exact['reference_region']['status']=='witnessed_feasible')
        ch = exact['reference_region']['point']['channels']
        require('witness-reconstructs-full-references', calibration(ch) == data)
        for m in MODELS:
            require('witness-reconstructs-source-probes', probes(ch,m) == actual[m] == predict(data,m))
            require('independent-predictor-binding', predict(data,m)==old['predictions'](old['references'](data['B'],data['A'],data['00'],data['11']),None if m=='P' else tuple(map(int,m))))
        estimate = {k:perturbed(data[k],case_index+j,t) for j,k in enumerate(REFS)}
        eps = dict.fromkeys(REFS,budget)
        noisy = prepare_rule(estimate,eps)
        require('true-reference-region-not-excluded', noisy['reference_region']['status'] not in ('excluded','invalid_input'))
        require('calibration-envelope', all(norm(estimate[k]-data[k]) <= eps[k] for k in REFS))
        for m in MODELS:
            require('prediction-envelope', all(norm(x-y)<=b for x,y,b in zip(predict(estimate,m),actual[m],noisy['models'][m]['reference_bounds'])))
        certificate = separation_certificate(noisy,(budget,budget))
        if all(row['channel_flags'].values()):
            require('reference-only-separation-certificate', certificate['all_rivals_separated'])
        trials_saved = []
        for j,m in enumerate(MODELS):
            trials = tuple(perturbed(P,case_index+j+k,t) for k,P in enumerate(actual[m]))
            decision = evaluate(noisy,trials,(budget,budget))
            require('true-model-never-rejected', m in decision['not_excluded'])
            exact_decision = evaluate(exact,actual[m],(0,0))
            require('exact-decision-is-table-equality', exact_decision['not_excluded']==[n for n in MODELS if actual[n]==actual[m]])
            if all(row['channel_flags'].values()):
                require('informative-perturbed-selection', decision['not_excluded']==[m])
            true_model_tests += 1; comparison_tests += len(MODELS)
            trials_saved.append({'true_model':m,'estimated_trials':trials,'decision':decision})
        cases.append({'channel_flags':row['channel_flags'],'reference_witness':exact['reference_region']['point'],
                      'estimated_references':estimate,'estimated_reference_status':noisy['reference_region'],
                      'reference_error_budget':eps,'trial_error_budget':(budget,budget),
                      'reference_only_separation':certificate,'trials':trials_saved})

    full = next(row for row in parent['census'] if all(row['channel_flags'].values()))
    channels = {k:decode(R) for k,R in full['channels'].items()}
    data = calibration(channels)
    boundary = {'K':s.Matrix([[1,0],[0,1],[0,0]]),
                **{k:s.Matrix([[1,0],[0,0],[0,1]]) for k in ('AX','AZ','BX','BZ')}}
    witness = compatible(calibration(boundary))
    require('zero-support-boundary-witness', witness['status']=='compatible' and calibration(witness['channels'])==calibration(boundary))
    hostile_results = []
    def hostile(name,bad,gate):
        result = compatible(bad)
        require(name, result['status']=='incompatible' and result['gate']==gate)
        require(name+'-zero-radius-region', reference_region(bad,zero)['status']=='excluded')
        hostile_results.append({'name':name,'tables':bad,'result':result})
    bad = dict(data); delta = s.Rational(1,10000)
    bad['00'] = data['00']+delta*s.Matrix([1,-1,0,-1,1,0,0,0,0])
    hostile('basis-correlation-hidden-from-marginals',bad,'basis_00')
    partial_eps = dict(zero); partial_eps['00']=4*delta
    require('incompatible-point-not-incompatible-region', reference_region(bad,partial_eps)['status']=='unresolved')
    bad = dict(data)
    direction = s.Matrix([1,-1,0])
    bad['B'] = data['B']+s.kronecker_product(direction,direction,direction)/100000
    hostile('bypass-correlation-hidden-from-pair-marginals',bad,'bypass_B')
    _,_,az,bz = views(data)
    def artificial(MA,MB):
        return {'A':tensor(bz[0],MA,'B'),'B':tensor(az[0],MB,'A'),'00':data['00'],'11':data['11']}
    mu = s.ones(3,1)/3
    u,v = s.Matrix([1,-1,0])/12,s.Matrix([0,1,-1])/12
    MA,MB = mu*mu.T+u*u.T,mu*mu.T+v*u.T
    require('individual-positive-reflections', all(x >= 0 for M in (MA,MB) for x in reflect(M)) and center(MA).rank()==center(MB).rank()==1)
    hostile('incompatible-shared-herald-direction',artificial(MA,MB),'shared_covariance_rank')
    hostile('different-herald-means',artificial(s.Matrix([s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)])*mu.T,mu*mu.T),'herald_mean')
    badM = s.diag(s.Rational(9,10),s.Rational(1,10),0)
    hostile('positive-table-negative-reflection',artificial(badM,badM),'negative_reflection_A')
    require('negative-reflection-retained', min(reflect(badM)) == -s.Rational(2,25))
    for invalid in (s.zeros(27,1),s.Matrix([-1,2]+[0]*25)):
        bad = dict(data); bad['B']=invalid
        require('malformed-input-not-repaired', prepare_rule(bad,zero)['reference_region']['status']=='invalid_input')
    negative_retained = False
    boundary_data = calibration(boundary)
    for key in ('A','B'):
        for index in range(27):
            estimate = dict(boundary_data); estimate[key]=perturbed(estimate[key],index,t)
            if any(x < 0 for M in views(estimate)[:2] for x in reflect(M)):
                eps = dict(zero); eps[key]=budget
                rule = prepare_rule(estimate,eps)
                require('negative-estimate-region-not-excluded', rule['reference_region']['status'] in ('unresolved','witnessed_feasible'))
                decision = evaluate(rule,probes(boundary,'P'),(0,0))
                require('negative-estimate-true-model-retained', 'P' in decision['not_excluded'])
                negative_retained = any(x < 0 for m in rule['models'].values() for P in m['prediction'] for x in P)
                if negative_retained:
                    break
        if negative_retained:
            break
    require('unclipped-negative-prediction-tested', negative_retained)

    curve = []; test_eps = s.Rational(contract['near_blind']['probe_error_budget'])
    for raw in contract['near_blind']['theta']:
        theta = s.Rational(raw); ch = dict(channels)
        plus,minus = channels['BZ'][:,1],channels['BZ'][:,0]
        ch['BZ']=s.Matrix.hstack(plus+theta*(minus-plus),plus)
        cal = calibration(ch); rule = prepare_rule(cal,zero); trial = probes(ch,'P')
        gap = sum(norm(x-y) for x,y in zip(trial,probes(ch,'001')))
        require('near-blind-exact-linear-gap', gap==theta*norm(minus-plus)==theta)
        decision = evaluate(rule,trial,(test_eps,test_eps))
        require('strict-near-blind-error-boundary', decision['not_excluded']==(['P','001'] if theta<=test_eps else ['P']))
        exact = evaluate(rule,trial,(0,0))
        require('nonzero-not-uniformly-separated', exact['not_excluded']==(['P','001'] if theta==0 else ['P']))
        curve.append({'theta':theta,'channels':ch,'calibration':cal,'trials':trial,'gap_to_001':gap,'decision':decision})

    # Distribution-free Lipschitz chains are proved in the companion derivation;
    # test their intermediate inequalities on every census table perturbation.
    for row in parent['census']:
        original = views({k:decode(P) for k,P in row['calibration'].items()})[:2]
        for M in original:
            Q = (1-t)*M+t*s.diag(1,0,0)
            e = norm(Q-M)
            require('center-and-reflection-envelopes', norm(center(Q)-center(M))<=3*e and norm(reflect(Q)-reflect(M))<=5*e)
    alpha = s.Rational(1,600)
    radii = {str(d):iid_radius(d,100000000,alpha) for d in (9,27)}
    require('iid-radius-symbolic-identity', radii['27']==27*s.sqrt(s.log(32400)/200000000))
    for n in (0,-1):
        try:
            iid_radius(27,n,alpha)
        except ValueError:
            pass
        else:
            raise AssertionError('empty-sample-accepted')
    require('source-inputs-preserved', all(p.read_bytes()==raw for p,raw in before.items()))
    result = {'schema':'marici.nima.record-reference-decision-result.v1','status':'pass',
              'classification':'constructive-reference-consistency-and-conservative-nine-model-uncertainty-rule',
              'checks_passed':len(CHECKS),'true_model_perturbation_tests':true_model_tests,
              'perturbed_candidate_comparisons':comparison_tests,'strata':len(cases),'cases':cases,
              'zero_support_witness':witness,'hostiles':hostile_results,'negative_predictions_retained':negative_retained,
              'near_blind_curve':curve,'iid_radius_examples':radii,'scope':contract['scope'],
              'physical_admission_required':False,'measured_records':False,
              'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(raw).hexdigest() for p,raw in before.items()}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(clean(result),indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','classification','checks_passed','true_model_perturbation_tests','perturbed_candidate_comparisons','strata','negative_predictions_retained')},indent=2))


if __name__ == '__main__':
    main()
