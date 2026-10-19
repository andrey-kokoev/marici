"""Structural/provenance checks for the local statistical successor net."""
import copy
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
PATH=ROOT/'research/sontag/contracts/optical-statistical-control-work-net.v1.json'
def validate(c):
    nodes={n['id']:n for n in c['nodes']}; arts={a['id']:a for a in c['artifacts']}
    if len(nodes)!=len(c['nodes']): raise ValueError('duplicate node')
    visiting=set(); done=set()
    def visit(i):
        if i not in nodes or i in visiting: raise ValueError('unknown dependency/cycle')
        if i in done:return
        visiting.add(i)
        for d in nodes[i]['depends_on']:visit(d)
        visiting.remove(i);done.add(i)
    for i,n in nodes.items():
        visit(i)
        if not n['scope'] or not n['acceptance']:raise ValueError('missing scope')
        if not set(n['evidence'])<=set(arts):raise ValueError('unknown evidence')
        if n['status']=='resolved':
            if not n['evidence'] or n['verdict'] not in ('constructed','rejected'):raise ValueError('unsupported resolution')
            if any(nodes[d]['status']!='resolved' for d in n['depends_on']):raise ValueError('premature resolution')
            if any(nodes[d]['verdict']!=v for d,v in n.get('required_verdicts',{}).items()):raise ValueError('nonpositive assembly')
        elif n['status'] not in ('open','deferred') or n['verdict']!='open':raise ValueError('bad status')
        elif n['status']=='deferred' and (not n.get('blocker') or not n.get('reopening_condition')):raise ValueError('untyped deferral')
    rival=nodes['mean-target-implies-precision']
    if rival['verdict']!='rejected' or not rival['counterexample']:raise ValueError('lost hostile')
    frontier=[i for i,n in nodes.items() if n['status']=='open' and all(nodes[d]['status']=='resolved' for d in n['depends_on'])]
    if c['frontier']!=frontier or (c['recommended_start'] not in frontier if frontier else c['recommended_start'] is not None):raise ValueError('stale frontier')
    if 'calibration-aware-binding' not in nodes['licensed-statistical-optical-binding']['depends_on']:raise ValueError('calibration bypass')
    if c['objective']['outcome'] is not None:raise ValueError('unlicensed root outcome')
    for a in arts.values():
        for p in a['paths']:
            if not (ROOT/p).is_file():raise ValueError('missing source')
            if p.endswith('.json') and json.loads((ROOT/p).read_text(encoding='utf-8')).get('passed') is not True:raise ValueError('failed receipt')
c=json.loads(PATH.read_text(encoding='utf-8'));validate(c)
rejected=[]
for name in ('cycle','calibration-bypass','lost-hostile','stale-frontier','premature-root'):
    b=copy.deepcopy(c); n={x['id']:x for x in b['nodes']}
    if name=='cycle':n['ideal-gain-dilation']['depends_on']=['licensed-statistical-optical-binding']
    elif name=='calibration-bypass':n['licensed-statistical-optical-binding']['depends_on'].remove('calibration-aware-binding')
    elif name=='lost-hostile':n['mean-target-implies-precision']['verdict']='constructed'
    elif name=='stale-frontier':b['frontier']=['ideal-gain-dilation']
    else:
        n['calibration-aware-binding'].update(status='open',verdict='open')
        n['licensed-statistical-optical-binding'].update(status='resolved',verdict='constructed',evidence=['gain'])
    try:validate(b)
    except ValueError:rejected.append(name)
    else:raise AssertionError('accepted '+name)
paths=[str(PATH.relative_to(ROOT))]+[p for a in c['artifacts'] for p in a['paths']]
out={'schema':'marici.sontag.optical-statistical-work-net-check.v1','passed':True,
 'frontier':c['frontier'],'rejected_controls':rejected,'scientific_suites_rerun':False,
 'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
 'shared_net_modified':False}
p=ROOT/'research/sontag/results/optical-statistical-work-net-validation-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'frontier':c['frontier'],'rejected_controls':len(rejected)},indent=2))
