"""Exact-representation controls and freshly checked mixed native closure."""
from pathlib import Path
from itertools import product
import hashlib
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
LIB=Path.home()/'tools/cubical-agda/cubical-0.9'
EXE=shutil.which('agda')
assert EXE and LIB.is_dir()
sources=[BASE/'agda/ExactSourceAdmission.agda',BASE/'agda/MixedSourceAdmissionClosure.agda',
         BASE/'agda/negative/MixedBadBoundaryAfterComparison.agda',
         BASE/'agda/RetainedFeedbackCovariance.agda',BASE/'agda/NativeExtensionFamilyAudit.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
         ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
pos=subprocess.run(common+['--ignore-interfaces',str(sources[1])],capture_output=True,text=True,timeout=300)
log=pos.stdout+pos.stderr
(BASE/'results/mixed-source-admission-positive.log').write_text(log,encoding='utf-8')
assert pos.returncode==0 and 'UnsupportedIndexedMatch' not in log,log[-5000:]
neg=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(sources[2])],capture_output=True,text=True,timeout=120)
log=neg.stdout+neg.stderr
(BASE/'results/mixed-source-admission-negative.log').write_text(log,encoding='utf-8')
assert neg.returncode!=0 and 'expression CA' in log and 'Edge' in log,log
# Enumerate candidate decoders, preserving actual witness identities rather
# than asking only whether every target has some realization.
profiles=0
for m in range(1,4):
    for n in range(5):
        for decode in product(range(m),repeat=n):
            exact=len(set(decode))==n and set(decode)==set(range(m))
            for t_size in range(3):
                inverse_counts={request:0 for request in product(range(m),repeat=t_size)}
                for f in product(range(n),repeat=t_size):
                    inverse_counts[tuple(decode[i] for i in f)]+=1
                if t_size:assert all(c==1 for c in inverse_counts.values())==exact
            profiles+=1
assert profiles==157
assert tuple([0].count(w) for w in range(2))==(1,0)
assert tuple([0,0,1,1].count(w) for w in range(2))==(2,2)
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
edges={label:(s,t) for label,s,t in PACKETS}
out={v:tuple(label for label,(s,t) in edges.items() if s==v) for v in 'ABCD'}
sigma=dict(zip('ABCD','BADC'));by_edge={edge:label for label,edge in edges.items()}
move_edge={e:by_edge[(sigma[s],sigma[t])] for e,(s,t) in edges.items()}
# Symbolic evidence transport has a distinct inverse; forward squared is not
# silently equated to identity on initial proof parameters.
def evidence(w,back=False):
    tag='back' if back else 'forward';other='forward' if back else 'back'
    return w[1] if w[0]==other else (tag,w)
def port(a):
    if a[0]=='initial':return a[1]
    if a[0]=='certify':return port(a[1])
    return edges[a[2]][1]
def tasks(a):return ('identity',)+out[port(a)]
def run(a,t):
    if t=='identity':return 'certify',a
    assert t in out[port(a)]
    return 'attach',a,t
def move(a,back=False):
    if a[0]=='initial':return 'initial',sigma[a[1]],evidence(a[2],back)
    if a[0]=='certify':return 'certify',move(a[1],back)
    return 'attach',move(a[1],back),move_edge[a[2]]
def native(a):
    if a[0]=='initial':return ('seed-evidence',a[1],a[2])
    if a[0]=='certify':return ('identity-rule',native(a[1]))
    return ('E-rule',a[2],tuple((e,('reflexivity-rule',native(a[1]))) for e in out[port(a[1])]))
def peel(a):
    d=native(a)
    return d[1] if a[0]=='certify' else dict(d[2])[d[1]][1]
levels=[];squares=0
states=[('initial',v,('opaque',v)) for v in 'ABCD']
for depth in range(6):
    levels.append({'depth':depth,'retained_mixed_assemblies':len(states)})
    next_states=[]
    for a in states:
        assert move(move(a),True)==a and move(move(a,True))==a
        for task in tasks(a):
            b=run(a,task);moved_task='identity' if task=='identity' else move_edge[task]
            assert move(b)==run(move(a),moved_task)
            assert native(move(b))==native(run(move(a),moved_task))
            assert peel(b)==native(a)
            squares+=1;next_states.append(b)
    states=next_states
assert [x['retained_mixed_assemblies'] for x in levels]==[4,10,26,68,178,466]
a=('initial','A',('opaque','a'))
assert run(run(a,'AB'),'identity')!=run(run(a,'identity'),'AB')
for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':pos.returncode,'negative_exit':neg.returncode,
        'negative_diagnostic':log.strip(),'exactness_candidate_decoders':profiles,
        'selected_only_request_fibers':[1,0],'duplicated_request_fibers':[2,2],
        'levels':levels,'mixed_transport_squares':squares,
        'formal_results':['Exact parameterized realization forces the specified decoder to be an equivalence',
            'Canonical outgoing-incidence family satisfies exactness',
            'Native E attachment and identity comparison close under arbitrary finite alternation',
            'Actual previous native derivation recovered in either constructor',
            'Whole mixed histories have source transport and a proved inverse',
            'Task/run transport square includes actual native derivations',
            'Distinct mixed constructor orders are not literal equal packages'],
        'scope':['Exactness is an explicit requirement of the all-attachments contract, not a consequence of bare retention',
            'The two-task signature is declared, not a discovered universal menu',
            'Comparison here is native identity comparison, not arbitrary comparison or higher-filler admission',
            'No interchange equality, arbitrary source-isomorphism coherence, physical scheduling or forward-squared history identity'],
        'source_hashes':hashes}
(BASE/'results/mixed-source-admission.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','fresh_agda_exit','negative_exit','exactness_candidate_decoders','mixed_transport_squares')}))
