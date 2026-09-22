"""Check algebra, tail recurrence, exact source replay and portable exports."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,isqrt
import importlib.util,json,hashlib,copy,tempfile,subprocess,sys
import sympy as S
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
vp=HERE.parent/'certificates'/'verify_source_task_transition.py';v=module('verify',vp);t=module('task',HERE/'three_channel_source_task.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(d):return tuple(Q(d[k]) for k in ('lower','upper'))
# Exact identities bind the direct kernels to the OLD response transforms.
s,q,u=S.symbols('s q u',positive=True);Ds,Dq=S.symbols('Ds Dq')
Ls=Ds+1/s+1/(s-1);Lq=Dq+1/q+1/(q-1)
oldplus=(Ls+Lq)/(s+q-1)-1/(s*(q-1))-1/((s-1)*q)
oldminus=(Ls-Lq)/(q-s)-1/((s-1)*(q-1))-1/(s*q)
assert S.cancel(oldplus-(Ds+Dq)/(q+s-1))==0
assert S.cancel(oldminus-(Ds-Dq)/(q-s))==0
kp=S.exp(-s*u)/(q+s-1)-S.exp((s-1)*u)*S.exp(-(q+s-1)*u)/(q+s-1)
km=-S.exp(-s*u)*(S.exp((s-q)*u)-1)/(s-q)
assert S.simplify(kp-(S.exp(-s*u)-S.exp(-q*u))/(q+s-1))==0
assert S.simplify(km+(S.exp(-s*u)-S.exp(-q*u))/(q-s))==0
# Partial summation majorant: differentiate its proposed integral exactly.
n=S.symbols('n',positive=True)
for power in (S.Rational(3,2),S.Rational(7,2)):
    f=2*S.log(2)*power/(power-1)*n**(1-power)+n**(-power)*(S.log(n)+1/power+S.log(2))
    assert S.simplify(S.diff(f,n)+power*(2*S.log(2)*n+S.log(n)+S.log(2))*n**(-power-1))==0
# Integer checks of the binomial recurrence used in the universal proof.
primes=[p for p in range(2,257) if all(p%d for d in range(2,isqrt(p)+1))]
for n in range(2,257):
    half=(n+1)//2
    for p in primes:
        if p>n:break
        power=p;required=valuation=0
        while power<=n:
            required+=int(power>half)
            valuation+=n//power-(n//2)//power-half//power
            power*=p
        assert required<=valuation
    assert comb(n,n//2)<=2**n
    total=0;k=n
    while k>1:total+=k;k=(k+1)//2
    assert total<=2*n+(n-1).bit_length()
report=v.load(OUT/'signed-pairing-task-refinement.json');theta=v.load(OUT/'theta-mass-refinement.json')
for name,h in report['protected_file_hashes'].items():assert sha(OUT/name)==h
path=OUT/report['calibration_file'];assert sha(path)==report['calibration_sha256']
engine=t.SourceTask(path);parent=t.SourceTask(OUT/engine.cal['parent_calibration_file'])
assert engine.cal['refinement_evidence']['pairing_code_sha256']==sha(HERE/'certify_signed_fixed_hat_pairing.py')
assert engine.cal['refinement_evidence']['quadrature_code_sha256']==sha(HERE/'refine_theta_mass_quadrature.py')
assert report['pairing']['analytic_parameters']=={'s':'7/2','beta':'3/2','lambda':'4','d':'2'}
assert report['pairing']['N']==1000000 and report['independent_cutoff_mesh_replay']['N']==500000
assert report['pairing']['bits']==192 and report['independent_cutoff_mesh_replay']['bits']==224
C=bounds(report['pairing']['C']);gain=bounds(report['gain_after']);critical=bounds(theta['critical_C']);threshold=Q(theta['threshold'])
assert C[1]<critical[0] and gain[1]<threshold
assert report['resolved'] is True
frozen=v.load(OUT/'calibration-refinement-frozen-inputs.json');prior=v.load(OUT/'three-channel-source-task-fixtures.json')
folder=OUT/'portable-source-task-transitions';produced=[];middle_costs={}
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode]);cases.update({n:prior[mode][n] for n in ('feasible','infeasible')})
    for name,data in cases.items():
        before=parent.certify(data);after=engine.certify(data)
        assert report['cases'][mode][name]=={'before':before,'after':after}
        if before['status']!='UNRESOLVED':assert before['status']==after['status']
        if before.get('nonvacuous_positive_task_certificate'):assert after['nonvacuous_positive_task_certificate']
        if before['status']!='CERTIFIED_INFEASIBLE' and after['status']!='CERTIFIED_INFEASIBLE':
            for target,b in after['aggregate_readout_enclosures'].items():
                a=before['aggregate_readout_enclosures'][target]
                assert Q(a['lower_rational'])<=Q(b['lower_rational'])<=Q(b['upper_rational'])<=Q(a['upper_rational'])
        if name=='middle_threshold':
            assert before['status']=='UNRESOLVED' and after['status']=='CERTIFIED_INFEASIBLE'
            assert t.interval(data['raw']['crossed'])==(Q(0),Q(0)) and t.interval(data['raw']['vacuum'])==(Q(1,100),Q(1,100))
            cap=(Q(data['budget'])-8*2**16*Q(1,100))/(32*2**16)
            assert threshold==t.interval(data['raw']['positive'])[0]/cap
            assert Q(after['necessary_moment_cost_lower_bound'])>Q(data['budget'])
            middle_costs[mode]=str(Q(after['necessary_moment_cost_lower_bound'])/2**16)
        chain=v.load(folder/f'{mode}-{name}-theta-taylor.json');v.verify(chain)
        old=chain['nodes'][-1];new=copy.deepcopy(old)
        assert old['evidence']['calibration']==engine.cal['parent_calibration_sha256']
        assert old['raw']=={n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES}
        assert old['gains']=={n:list(map(str,b)) for n,b in parent.calibrations(mode).items()}
        assert old['sigma']=={n:list(map(str,b)) for n,b in engine.sigma.items()}
        assert Q(old['tail_multiplier'])==engine.tail_multiplier and Q(old['budget'])==Q(data.get('budget',t.DEFAULT_BUDGET))
        new['gains']={n:list(map(str,b)) for n,b in engine.calibrations(mode).items()};new['evidence']['calibration']=sha(path)
        c={'version':1,'problem_sha256':v.sha(new),'status':after['status'],'necessary_cost':after['necessary_moment_cost_lower_bound']}
        if c['status']!='CERTIFIED_INFEASIBLE':
            c['aggregate_bounds']={n:[after['aggregate_readout_enclosures'][key][end] for end in ('lower_rational','upper_rational')]
                                   for n,key in (('vacuum','vacuum'),('residual','residual_per_w_squared'))}
            c['positive_task']=after['nonvacuous_positive_task_certificate']
        if c['status']=='CERTIFIED_FEASIBLE':
            witness=after['witness_check'] if after.get('witness_check',{}).get('accepted') else after['automatic_witness_search']
            c['witness']=witness['coefficients_at_A2']
        chain['edges'].append({'version':1,'kind':'identity-calibration-refinement','old_sha256':v.sha(old),'new_sha256':v.sha(new)})
        chain['nodes'].append(new);chain['certificates'].append(c);v.verify(chain)
        out=folder/f'{mode}-{name}-signed-pairing.json';out.write_text(json.dumps(chain,indent=2)+'\n',encoding='utf-8');produced.append(out)
# Rebound semantic corruptions, not just stale hashes.
chain=v.load(folder/'private-middle_threshold-signed-pairing.json');rejected=[]
for name,change in (
 ('understated necessary cost',lambda c:c['certificates'][-1].__setitem__('necessary_cost','0')),
 ('weakened prior',lambda c:c['nodes'][-1].__setitem__('budget',str(Q(c['nodes'][-1]['budget'])+100))),
 ('altered raw evidence',lambda c:c['nodes'][-1]['raw']['positive'].__setitem__(0,'0'))):
    bad=copy.deepcopy(chain);change(bad);h=v.sha(bad['nodes'][-1])
    bad['certificates'][-1]['problem_sha256']=h;bad['edges'][-1]['new_sha256']=h
    try:v.verify(bad)
    except ValueError:rejected.append(name)
    else:raise AssertionError('Corruption accepted: '+name)
with tempfile.TemporaryDirectory() as directory:
    d=Path(directory);(d/vp.name).write_bytes(vp.read_bytes())
    for path in produced:
        (d/'chain.json').write_bytes(path.read_bytes())
        p=subprocess.run([sys.executable,'-I',str(d/vp.name),str(d/'chain.json')],cwd=d,capture_output=True,text=True)
        assert p.returncode==0,p.stderr
for name,h in report['protected_file_hashes'].items():assert sha(OUT/name)==h
result={'passed':True,'response_transform_identities':2,'kernel_Laplace_identities':2,
 'tail_antiderivatives':2,'binomial_recurrence_integer_cases':255,
 'C_margin_below_critical':str(critical[0]-C[1]),'gain_margin_below_threshold':str(threshold-gain[1]),
 'normalized_necessary_costs':middle_costs,'portable_chains':[p.name for p in produced],
 'rejected_corruptions':rejected,'isolated_verification':True,
 'scope':'Analytical pairing validity is justified by the accompanying kernel and tail proof. Exact task checks certify incompatibility only within the declared source family, error enclosures and unchanged prior.'}
(OUT/'signed-pairing-task-tests.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: signed transform/tail identities, both middle contradictions, ten portable chains, corruption rejection and isolated verification')
