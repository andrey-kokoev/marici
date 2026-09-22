"""Exact replay/export plus analytical quadrature-kernel regression tests."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy,tempfile,subprocess,sys
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
q=module('quad',HERE/'refine_theta_mass_quadrature.py');t=module('task',HERE/'three_channel_source_task.py')
vp=HERE.parent/'certificates'/'verify_source_task_transition.py';v=module('verifier',vp)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ends(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def bounds(d):return tuple(Q(d[k]) for k in ('lower','upper'))
ctx.prec=192;ctx.cap=5
for degree in range(5):
    for sign in (-1,1):
        values,errors=q.integrate_cell(lambda x:(sign*x**degree,),arb(0),arb(1))
        lo,hi=ends(values[0]);assert lo<=Q(sign,degree+1)<=hi
        if degree<4:assert errors[0]==0
        else:assert ends(errors[0])[0]<=Q(1,80)<=ends(errors[0])[1]
# Known analytic integral, independent of mesh convergence.
value=arb(0)
for j in range(16):value+=q.integrate_cell(lambda x:(x.exp(),),arb(j)/16,arb(j+1)/16)[0][0]
ctx.prec=384;truth=arb(1).exp()-1
assert ends(value)[0]<=ends(truth)[0]<=ends(truth)[1]<=ends(value)[1]
report=v.load(OUT/'theta-mass-refinement.json');old=v.load(OUT/'projection-resolution-conjecture-attack.json')
for name,h in report['protected_file_hashes'].items():assert sha(OUT/name)==h
assert report['quadrature_code_sha256']==sha(HERE/'refine_theta_mass_quadrature.py')
path=OUT/report['calibration_file'];assert sha(path)==report['calibration_sha256']
engine=t.SourceTask(path);parent=t.SourceTask(OUT/engine.cal['parent_calibration_file'])
assert engine.cal['refinement_evidence']['theta_cells']==1024
for key in ('C_bin_lower','C_bin_upper','projection_dimension','projection_bits'):
    assert engine.cal['refinement_evidence'][key]==parent.cal['refinement_evidence'][key]
reductions={}
for name in ('A1','B1'):
    for key in ('X','mu'):
        a=bounds(old['windows'][name][key]);b=bounds(report['windows'][name][key])
        assert a[0]<b[0]<b[1]<a[1]
        reductions[name+'_'+key]=str((a[1]-a[0])/(b[1]-b[0]))
    for key in ('lower','upper'):assert report['windows'][name]['tail_bound'][key]==old['windows'][name]['tail_bound'][key]
# Exact Cartesian arithmetic diagnoses the remaining C uncertainty.
C=bounds(old['C_after']);H=bounds(old['h']);L=bounds(old['L'])
xa=bounds(report['windows']['A1']['X']);xb=bounds(report['windows']['B1']['X'])
ma=bounds(report['windows']['A1']['mu']);mb=bounds(report['windows']['B1']['mu'])
assert min(C+H+xa+xb)>0 and ma[0]>L[1] and mb[0]>L[1]
def extreme(c,high):
    k=int(high);ell=1-k
    return 2*xa[k]*xb[k]*(c+H[k]*(ma[k]-L[ell]))*(c+H[k]*(mb[k]-L[ell]))
gain=bounds(report['gain_after']);threshold=Q(old['threshold'])
assert gain[0]<=extreme(C[0],False)<=extreme(C[1],True)<=gain[1]
assert extreme(C[0],True)<threshold<extreme(C[1],False)
critical=bounds(report['critical_C']);assert Q(report['threshold'])==threshold
assert C[0]<critical[0]<critical[1]<C[1]
assert extreme(critical[0],True)<=threshold<=extreme(critical[1],False)
# Thus the mass-only obstruction is removed. The allowed C endpoints now
# force opposite outcomes uniformly over the other retained boxes.
a=bounds(old['gain_after']);reductions['positive_gain']=str((a[1]-a[0])/(gain[1]-gain[0]))
frozen=v.load(OUT/'calibration-refinement-frozen-inputs.json');prior=v.load(OUT/'three-channel-source-task-fixtures.json')
folder=OUT/'portable-source-task-transitions';produced=[]
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode]);cases.update({n:prior[mode][n] for n in ('feasible','infeasible')})
    for name,data in cases.items():
        before=parent.certify(data);after=engine.certify(data)
        if name=='middle_threshold':
            assert t.interval(data['raw']['vacuum'])==(Q(1,100),Q(1,100))
            assert t.interval(data['raw']['crossed'])==(Q(0),Q(0))
            cap=(Q(data['budget'])-8*2**16*Q(1,100))/(32*2**16)
            assert threshold==t.interval(data['raw']['positive'])[0]/cap
        assert {'before':before,'after':after}==report['cases'][mode][name]
        if before['status']!='UNRESOLVED':assert after['status']==before['status']
        if before.get('nonvacuous_positive_task_certificate'):assert after['nonvacuous_positive_task_certificate']
        if before['status']!='CERTIFIED_INFEASIBLE' and after['status']!='CERTIFIED_INFEASIBLE':
            for target,b in after['aggregate_readout_enclosures'].items():
                a=before['aggregate_readout_enclosures'][target]
                assert Q(a['lower_rational'])<=Q(b['lower_rational'])<=Q(b['upper_rational'])<=Q(a['upper_rational'])
        chain=v.load(folder/f'{mode}-{name}-projection272.json');v.verify(chain)
        oldnode=chain['nodes'][-1];new=copy.deepcopy(oldnode)
        assert oldnode['evidence']['calibration']==engine.cal['parent_calibration_sha256']
        assert oldnode['raw']=={n:list(map(str,t.interval(data['raw'][n]))) for n in t.NAMES}
        assert oldnode['gains']=={n:list(map(str,b)) for n,b in parent.calibrations(mode).items()}
        assert oldnode['sigma']=={n:list(map(str,b)) for n,b in engine.sigma.items()}
        assert Q(oldnode['tail_multiplier'])==engine.tail_multiplier
        assert Q(oldnode['budget'])==Q(data.get('budget',t.DEFAULT_BUDGET))
        new['gains']={n:list(map(str,b)) for n,b in engine.calibrations(mode).items()};new['evidence']['calibration']=sha(path)
        c={'version':1,'problem_sha256':v.sha(new),'status':after['status'],'necessary_cost':after['necessary_moment_cost_lower_bound']}
        if c['status']!='CERTIFIED_INFEASIBLE':
            c['aggregate_bounds']={n:[after['aggregate_readout_enclosures'][key][end] for end in ('lower_rational','upper_rational')]
                                   for n,key in (('vacuum','vacuum'),('residual','residual_per_w_squared'))}
            c['positive_task']=after['nonvacuous_positive_task_certificate']
        if c['status']=='CERTIFIED_FEASIBLE':
            witness=after['witness_check'] if after.get('witness_check',{}).get('accepted') else after['automatic_witness_search']
            c['witness']=witness['coefficients_at_A2']
        chain['edges'].append({'version':1,'kind':'identity-calibration-refinement','old_sha256':v.sha(oldnode),'new_sha256':v.sha(new)})
        chain['nodes'].append(new);chain['certificates'].append(c);v.verify(chain)
        out=folder/f'{mode}-{name}-theta-taylor.json';out.write_text(json.dumps(chain,indent=2)+'\n',encoding='utf-8');produced.append(out)
with tempfile.TemporaryDirectory() as directory:
    d=Path(directory);(d/vp.name).write_bytes(vp.read_bytes())
    for path in produced:
        (d/'chain.json').write_bytes(path.read_bytes())
        result=subprocess.run([sys.executable,'-I',str(d/vp.name),str(d/'chain.json')],cwd=d,capture_output=True,text=True)
        assert result.returncode==0,result.stderr
for name,h in report['protected_file_hashes'].items():assert sha(OUT/name)==h
result={'passed':True,'polynomial_cases':10,'analytic_exponential_integral_checked':True,
        'width_reduction_factors':reductions,'mass_only_floor_removed':True,
        'remaining_C_endpoint_test':{'low_C_gain_upper':str(extreme(C[0],True)),
                                     'high_C_gain_lower':str(extreme(C[1],False)),'threshold':str(threshold)},
        'portable_chains':[p.name for p in produced],'isolated_verification':True,
        'scope':'Quadrature proof uses whole-cell fourth derivatives, not test agreement. Middle cases remain unresolved; next bottleneck is C, not physical ambiguity.'}
(OUT/'theta-mass-refinement-tests.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: Taylor remainder tests, exact bottleneck comparison, ten nested portable chains and isolated verification')
