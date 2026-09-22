"""Signed fixed-hat pairing -> unchanged frozen source task, with replay."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r=module('signed',HERE/'certify_signed_fixed_hat_pairing.py');t=module('task',HERE/'three_channel_source_task.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ends(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def enc(x):
    a,b=ends(x);return {'lower':str(a),'upper':str(b),'display':x.str(24)}
def ball(q):return arb(q.numerator)/q.denominator
def interval(d):return ball(Q(d['lower'])).union(ball(Q(d['upper'])))
parent_path=OUT/'three-channel-source-task-calibration-theta-taylor.json'
theta_path=OUT/'theta-mass-refinement.json';projection_path=OUT/'projection-resolution-conjecture-attack.json'
protected=[parent_path,theta_path,projection_path,OUT/'calibration-refinement-frozen-inputs.json',
 OUT/'three-channel-source-task-fixtures.json',OUT/'time-bin-cubic-observer.json',OUT/'three-channel-cubic-protocol.json']
hashes={p.name:sha(p) for p in protected}
parent=t.SourceTask(parent_path);theta=json.loads(theta_path.read_text(encoding='utf-8'));projection=json.loads(projection_path.read_text(encoding='utf-8'))
assert theta['calibration_sha256']==sha(parent_path)
C,report=r.compute(N=1000000,bits=192,mesh_divisions=32)
other,replay=r.compute(N=500000,bits=224,mesh_divisions=64)
ctx.prec=192
c=ends(C);alt=ends(other);old=tuple(Q(projection['C_after'][k]) for k in ('lower','upper'))
assert max(c[0],alt[0])<min(c[1],alt[1])
assert old[0]<c[0]<c[1]<old[1]
assert report['filter_sha256']==hashes['time-bin-cubic-observer.json']
assert max(ends(interval(report['h']))[0],ends(interval(projection['h']))[0])<=min(ends(interval(report['h']))[1],ends(interval(projection['h']))[1])
corrections=[]
for new,previous in zip(report['bulk_pairings'],projection['projection_diagnostics']):
    exact=interval(new);center=arb(previous['pairing_center']);prior=arb(previous['response'])
    assert prior.lower()<exact.lower()<exact.upper()<prior.upper()
    corrections.append(enc(exact-center))
X=[interval(theta['windows'][name]['X']) for name in ('A1','B1')]
mu=[interval(theta['windows'][name]['mu']) for name in ('A1','B1')]
H=interval(projection['h']);L=interval(projection['L']);assert min(X)>0 and min(mu)>L and H>0
G=2*X[0]*X[1]*(C+H*(mu[0]-L))*(C+H*(mu[1]-L));gain=ends(G)
# Outcome is computed, not obtained by assuming the conjecture succeeded.
cal=copy.deepcopy(parent.cal);cal['parent_calibration_file']=parent_path.name;cal['parent_calibration_sha256']=sha(parent_path)
for mode in ('private','reuse'):
    a,b=parent.calibrations(mode)['positive'];assert a<gain[0]<gain[1]<b
    cal['diagonal_refinements'][mode]['positive']={'lower':[str(gain[0].numerator),str(gain[0].denominator)],'upper':[str(gain[1].numerator),str(gain[1].denominator)]}
cal['refinement_evidence']={**parent.cal['refinement_evidence'],
 'method':'signed-digamma-Mangoldt-fixed-hat-pairing',
 'projection_role':'unchanged comparison baseline, not used to bound the new bulk pairings','pairing_code_sha256':sha(HERE/'certify_signed_fixed_hat_pairing.py'),
 'quadrature_code_sha256':sha(HERE/'refine_theta_mass_quadrature.py'),
 'C_bin_lower':[str(c[0].numerator),str(c[0].denominator)],'C_bin_upper':[str(c[1].numerator),str(c[1].denominator)],
 'prime_power_cutoff':1000000,'pairing_bits':192}
path=OUT/'three-channel-source-task-calibration-signed-pairing.json';path.write_text(json.dumps(cal,indent=2)+'\n',encoding='utf-8')
engine=t.SourceTask(path);frozen=json.loads(protected[3].read_text(encoding='utf-8'));prior=json.loads(protected[4].read_text(encoding='utf-8'))
cases={}
for mode in ('private','reuse'):
    inputs=dict(frozen['cases'][mode]);inputs.update({n:prior[mode][n] for n in ('feasible','infeasible')})
    cases[mode]={}
    for name,data in inputs.items():
        before=parent.certify(data);after=engine.certify(data)
        if before['status']!='UNRESOLVED':assert before['status']==after['status']
        if before.get('nonvacuous_positive_task_certificate'):assert after['nonvacuous_positive_task_certificate']
        cases[mode][name]={'before':before,'after':after}
assert hashes=={p.name:sha(p) for p in protected}
result={'passed':True,'conjecture':'Direct signed pairing resolves the middle without enlarging the projection',
 'resolved':all(cases[m]['middle_threshold']['after']['status']!='UNRESOLVED' for m in cases),
 'protected_file_hashes':hashes,'calibration_file':path.name,'calibration_sha256':sha(path),
 'pairing':report,'independent_cutoff_mesh_replay':replay,'signed_projection_corrections':corrections,
 'C_width_reduction':str((old[1]-old[0])/(c[1]-c[0])),'gain_after':enc(G),'cases':cases,
 'scope':'Same fixed detector, data, source family and prior. Direct signed pairing with rigorous tails, not a new acquisition or projection enlargement. Infeasibility is relative to the declared source model and budget.'}
(OUT/'signed-fixed-hat-pairing.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
(OUT/'signed-pairing-task-refinement.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'C':C.str(24),'gain':G.str(24),'statuses':{m:c['middle_threshold']['after']['status'] for m,c in cases.items()}},indent=2))
