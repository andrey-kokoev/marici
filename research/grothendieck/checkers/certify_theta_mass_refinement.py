"""Fresh higher-order theta integration; unchanged projection and frozen task."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
q=module('quadrature',HERE/'refine_theta_mass_quadrature.py');t=module('task',HERE/'three_channel_source_task.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ends(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def ball(x):return arb(x.numerator)/x.denominator
def interval(d):return ball(Q(d['lower'])).union(ball(Q(d['upper'])))
def enc(x):
    a,b=ends(x);return {'lower':str(a),'upper':str(b),'display':x.str(24)}
parent_path=OUT/'three-channel-source-task-calibration-projection272.json'
report_path=OUT/'projection-resolution-conjecture-attack.json'
protected=[parent_path,report_path,OUT/'calibration-refinement-frozen-inputs.json',OUT/'three-channel-source-task-fixtures.json',
           OUT/'time-bin-cubic-observer.json',OUT/'three-channel-cubic-protocol.json']
hashes={p.name:sha(p) for p in protected};parent=t.SourceTask(parent_path)
old=json.loads(report_path.read_text(encoding='utf-8'));assert old['calibration_sha256']==sha(parent_path)
ctx.prec=192
C=interval(old['C_after']);H=interval(old['h']);L=interval(old['L'])
windows={};checks={}
for name,A,p in (('A1',2,2),('B1',12,5)):
    a=q.window(A,p,1024);b=q.window(A,p,2048)
    for key in ('X','mu'):
        previous=tuple(Q(old['windows'][name][key][k]) for k in ('lower','upper'))
        new=ends(a[key]);fine=ends(b[key])
        assert previous[0]<new[0]<new[1]<previous[1]
        assert max(new[0],fine[0])<=min(new[1],fine[1])
    # The two computations must overlap; neither is substituted as a sampled
    # estimate. Keep the 1024-cell certified enclosure as the declared method.
    assert all(upper<lower for upper,lower in zip(b['quadrature_remainder_bounds'],a['quadrature_remainder_bounds']))
    windows[name]=a
    checks[name]={'cells':2048,'X':enc(b['X']),'mu':enc(b['mu']),
                  'quadrature_remainder_bounds':[enc(x) for x in b['quadrature_remainder_bounds']]}
A=windows['A1'];B=windows['B1'];assert A['mu']-L>0 and B['mu']-L>0
G=2*A['X']*B['X']*(C+H*(A['mu']-L))*(C+H*(B['mu']-L));gain=ends(G)
alpha=H*(A['mu']-L);beta=H*(B['mu']-L)
threshold=ball(Q(old['threshold']))
critical=-(alpha+beta)/2+(((alpha-beta)/2)**2+threshold/(2*A['X']*B['X'])).sqrt()
assert C.lower()<critical.lower()<critical.upper()<C.upper()
cal=copy.deepcopy(parent.cal);cal['parent_calibration_file']=parent_path.name;cal['parent_calibration_sha256']=sha(parent_path)
for mode in ('private','reuse'):
    before=parent.calibrations(mode)['positive'];assert before[0]<gain[0]<gain[1]<before[1]
    cal['diagonal_refinements'][mode]['positive']={'lower':[str(gain[0].numerator),str(gain[0].denominator)],
                                                'upper':[str(gain[1].numerator),str(gain[1].denominator)]}
cal['refinement_evidence']={**parent.cal['refinement_evidence'],
 'method':'fourth-order-Taylor-remainder-theta-integration','theta_cells':1024,'theta_bits':192,
 'quadrature_code_sha256':sha(HERE/'refine_theta_mass_quadrature.py'),'parent_projection_report_sha256':sha(report_path)}
path=OUT/'three-channel-source-task-calibration-theta-taylor.json'
path.write_text(json.dumps(cal,indent=2)+'\n',encoding='utf-8');engine=t.SourceTask(path)
frozen=json.loads(protected[2].read_text(encoding='utf-8'));prior=json.loads(protected[3].read_text(encoding='utf-8'))
results={}
for mode in ('private','reuse'):
    cases=dict(frozen['cases'][mode]);cases.update({n:prior[mode][n] for n in ('feasible','infeasible')})
    results[mode]={}
    for name,data in cases.items():
        before=parent.certify(data);after=engine.certify(data)
        if before['status']!='UNRESOLVED':assert after['status']==before['status']
        if before.get('nonvacuous_positive_task_certificate'):assert after['nonvacuous_positive_task_certificate']
        results[mode][name]={'before':before,'after':after}
assert hashes=={p.name:sha(p) for p in protected}
report={'passed':True,'protected_file_hashes':hashes,'calibration_file':path.name,'calibration_sha256':sha(path),
 'quadrature_code_sha256':sha(HERE/'refine_theta_mass_quadrature.py'),
 'windows':{n:{**{k:enc(a[k]) for k in ('X','mu','scaled_integral','centered_integral','tail_bound')},
                'quadrature_remainder_bounds':[enc(x) for x in a['quadrature_remainder_bounds']],
                'omitted_atom_integrals':[enc(x) for x in a['omitted_atom_integrals']]} for n,a in windows.items()},
 'independent_mesh_replay':checks,'gain_after':enc(G),'critical_C':enc(critical),'threshold':old['threshold'],'cases':results,
 'scope':'Certified fourth-derivative bounds on whole cells; unchanged fixed detector, projection, data and prior. Mesh overlap is a regression, not the quadrature proof.'}
(OUT/'theta-mass-refinement.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'gain':G.str(24),'middle_statuses':{m:r['middle_threshold']['after']['status'] for m,r in results.items()}},indent=2))
