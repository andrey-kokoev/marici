"""Fresh proof-relevant covariance closure and symbolic finite controls.

Opaque input-witness tags test non-erasure in this regression model. They do not
assert a cardinality theorem for native indexed derivation fibers.
"""
from dataclasses import dataclass
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
sources=[BASE/'agda/RetainedFeedbackCovariance.agda',
         BASE/'agda/negative/FeedbackBadEdgeTransport.agda',
         BASE/'agda/RetainedPackageFeedback.agda',
         BASE/'agda/SourceIndexedExtensionFamilies.agda',
         BASE/'agda/NativeExtensionFamilyAudit.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
         ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
positive=subprocess.run(common+['--ignore-interfaces',str(sources[0])],capture_output=True,text=True,timeout=300)
log=positive.stdout+positive.stderr
(BASE/'results/retained-feedback-covariance-positive.log').write_text(log,encoding='utf-8')
assert positive.returncode==0 and 'UnsupportedIndexedMatch' not in log,log[-6000:]
negative=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(sources[1])],capture_output=True,text=True,timeout=120)
log=negative.stdout+negative.stderr
(BASE/'results/retained-feedback-covariance-negative.log').write_text(log,encoding='utf-8')
assert negative.returncode!=0 and 'expression AB' in log and 'Edge' in log,log
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
registry={label:(s,t) for label,s,t in PACKETS}
out={v:tuple(e for e,(s,t) in registry.items() if s==v) for v in 'ABCD'}
sigma=dict(zip('ABCD','BADC'))
by_edge={ends:label for label,ends in registry.items()}
move_edge={e:by_edge[(sigma[s],sigma[t])] for e,(s,t) in registry.items()}

@dataclass(frozen=True)
class Node:
    start: str
    witness: tuple
    word: tuple

def endpoint(c):return registry[c.word[-1]][1] if c.word else c.start

def step(c,e):
    if e not in out[endpoint(c)]:raise ValueError('Incorrect extension boundary')
    return Node(c.start,c.witness,c.word+(e,))

def transport_witness(w,direction):
    inverse='back' if direction=='forward' else 'forward'
    if w[0]==inverse:return w[1]
    return direction,w

def move(c,direction='forward'):
    return Node(sigma[c.start],transport_witness(c.witness,direction),tuple(move_edge[e] for e in c.word))

def native(c):
    proof=('initial',c.start,c.witness)
    port=c.start
    for e in c.word:
        proof=('E',e,tuple((choice,('reflexivity',proof)) for choice in out[port]))
        port=registry[e][1]
    return port,proof

def peel(proof):return dict(proof[2])[proof[1]][1]

states=[Node(v,('opaque',tag),()) for v in 'ABCD' for tag in ('u','v')]
levels=[];squares=0;composite_squares=0
for n in range(7):
    levels.append({'depth':n,'symbolic_cases_with_two_input_tags':len(states)})
    extended=[]
    for c in states:
        assert move(move(c),'back')==c and move(move(c,'back'))==c
        for e in out[endpoint(c)]:
            left=move(step(c,e));right=step(move(c),move_edge[e])
            assert left==right and native(left)==native(right)
            assert peel(native(left)[1])==native(move(c))[1]
            squares+=1
            for f in out[endpoint(step(c,e))]:
                assert move(step(step(c,e),f))==step(step(move(c),move_edge[e]),move_edge[f])
                composite_squares+=1
            extended.append(step(c,e))
    states=extended
assert [x['symbolic_cases_with_two_input_tags'] for x in levels]==[8,12,20,32,52,84,136]
a=Node('A',('opaque','u'),())
try:step(move(a),'AB')
except ValueError:pass
else:raise AssertionError('Unmoved edge admitted at moved boundary')
# Replacing input evidence by a fresh seed token would fail this distinction.
b=Node('A',('opaque','v'),())
assert move(a)!=move(b) and native(move(a))!=native(move(b))
assert sum(len(out[registry[e][1]]) for e in out['A'])==3
for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
        'negative_diagnostic':log.strip(),'levels':levels,'symbolic_extension_squares':squares,
        'symbolic_two_extension_squares':composite_squares,'two_task_fiber_at_A':3,
        'formal_results':['Arbitrary initial indexed derivation transported along a univalent endpoint-package path',
                          'Distinct backward transport proves two-sided recovery of whole retained payload',
                          'Extension square for full retained chains and actual native histories',
                          'Dependent two-extension fiber transport and composition square',
                          'Equality of actual Ready output records, including canonical admission evidence'],
        'scope':['Fixed source comparison and outgoing-edge task policy',
                 'No collapse of indexed seed proofs or assumed proof irrelevance',
                 'Forward lift squared is not claimed identity; backward lift is its proved inverse',
                 'No global source-isomorphism functor or all higher coherence theorem',
                 'Opaque symbolic tags are regression parameters, not enumerated native proof inhabitants'],
        'source_hashes':hashes}
(BASE/'results/retained-feedback-covariance.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','fresh_agda_exit','negative_exit',
    'symbolic_extension_squares','symbolic_two_extension_squares','two_task_fiber_at_A')}))
