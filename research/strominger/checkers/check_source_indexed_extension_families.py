"""Fresh native E/Pi closure with incidence-derived index families."""
from itertools import product
from pathlib import Path
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
sources=[BASE/'agda/SourceIndexedExtensionFamilies.agda',
         BASE/'agda/negative/SourceBadEndpointExtension.agda',
         BASE/'agda/NativeExtensionFamilyAudit.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
         ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
positive=subprocess.run(common+['--ignore-interfaces',str(sources[0])],capture_output=True,text=True,timeout=300)
text=positive.stdout+positive.stderr
(BASE/'results/source-indexed-extension-families-positive.log').write_text(text,encoding='utf-8')
assert positive.returncode==0,text[-5000:]
assert 'UnsupportedIndexedMatch' not in text,text[-5000:]
negative=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(sources[1])],capture_output=True,text=True,timeout=120)
text=negative.stdout+negative.stderr
(BASE/'results/source-indexed-extension-families-negative.log').write_text(text,encoding='utf-8')
assert negative.returncode!=0 and 'Edge C D' in text and 'CA' in text,text
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
names='ABCD';registry={label:(s,t) for label,s,t in PACKETS}
out={v:tuple(label for label,(s,t) in registry.items() if s==v) for v in names}
sigma=dict(zip(names,'BADC'))
edge_by_ends={ends:label for label,ends in registry.items()}
move={label:edge_by_ends[(sigma[s],sigma[t])] for label,(s,t) in registry.items()}
def act(state):
    start,word=state
    return sigma[start],tuple(move[e] for e in word)
def endpoint(state):return registry[state[1][-1]][1] if state[1] else state[0]
states=[(v,()) for v in names];levels=[]
for n in range(7):
    assert len(states)==len(set(states))
    assert {act(state) for state in states}==set(states)
    for state in states:
        assert act(act(state))==state
        assert endpoint(act(state))==sigma[endpoint(state)]
    extensions=[(start,word+(e,)) for start,word in states for e in out[endpoint((start,word))]]
    for extended in extensions:
        parent=(extended[0],extended[1][:-1]);last=extended[1][-1]
        assert parent in states and registry[last][0]==endpoint(parent)
        moved=act(extended)
        assert (moved[0],moved[1][:-1])==act(parent)
    histogram={k:sum(len(out[endpoint(state)])==k for state in states) for k in (1,2)}
    orbits={min(state,act(state)) for state in states}
    levels.append({'depth':n,'states':len(states),'source_symmetry_orbits':len(orbits),
                   'extension_fiber_histogram':histogram,'next_states':len(extensions)})
    states=extensions
assert [x['states'] for x in levels]==[4,6,10,16,26,42,68]
# Two deterministic policies respect both incidence and seed symmetry; the
# complete family constructor does not choose either of them.
selectors=[]
for choices in product(*(out[v] for v in names)):
    f={v:registry[e][1] for v,e in zip(names,choices)}
    if all(f[sigma[v]]==sigma[f[v]] for v in names):selectors.append(f)
assert len(selectors)==2
for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
        'negative_diagnostic':text.strip(),'source_policy':'Graph-retaining vertex-pointed seeds from NativeExtensionFamilyAudit',
        'declared_constructor_task':'All finite incidence-compatible attachments; no chosen outgoing selector or physical schedule',
        'levels':levels,'equivariant_deterministic_selectors':selectors,
        'formal_scope':['All finite depth source index equivalence and endpoint covariance',
                        'Universal dependent-pair mapping property for compatible extensions',
                        'Actual E and Pi derivations under unchanged native rules',
                        'E interpreted carrier equivalent to source path index',
                        'Actual native comparisons between source-transported E packages',
                        'Exact whole-history reification recovery and distinct depth-one values'],
        'limits':['Index recursion is source-type-level, not an autonomous feedback procedure on prior reified histories',
                  'Task and structural depth remain explicit; native signature does not uniquely choose them',
                  'No event issuance, physical time, preferred branch, universal higher filling or intended T9 identification'],
        'source_hashes':hashes}
(BASE/'results/source-indexed-extension-families.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
                  'state_counts':[x['states'] for x in levels],'equivariant_single_successor_policies':len(selectors)}))
