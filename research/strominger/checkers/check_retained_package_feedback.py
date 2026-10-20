"""Fresh kernel closure and finite control for retained-package feedback."""
from pathlib import Path
from dataclasses import dataclass
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
sources=[BASE/'agda/RetainedPackageFeedback.agda',
         BASE/'agda/negative/FeedbackBadAttachment.agda',
         BASE/'agda/SourceIndexedExtensionFamilies.agda',
         BASE/'agda/NativeExtensionFamilyAudit.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',
         ROOT/'research/nima/checkers/check_natural_tower_return.py',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
positive=subprocess.run(common+['--ignore-interfaces',str(sources[0])],capture_output=True,text=True,timeout=300)
log=positive.stdout+positive.stderr
(BASE/'results/retained-package-feedback-positive.log').write_text(log,encoding='utf-8')
assert positive.returncode==0,log[-6000:]
assert 'UnsupportedIndexedMatch' not in log,log[-6000:]
negative=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(sources[1])],capture_output=True,text=True,timeout=120)
log=negative.stdout+negative.stderr
(BASE/'results/retained-package-feedback-negative.log').write_text(log,encoding='utf-8')
assert negative.returncode!=0 and 'Edge NativeExtensionFamilyAudit.A D' in log and 'expression CA' in log,log
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS
registry={label:(s,t) for label,s,t in PACKETS}
out={v:tuple(label for label,(s,t) in registry.items() if s==v) for v in 'ABCD'}

@dataclass(frozen=True)
class Node:
    port: str
    edge: str | None
    parent: object
    derivation: tuple

seed_calls=0
def initial(v):
    global seed_calls
    seed_calls+=1
    return Node(v,None,None,('seed',v))

def step(node,edge):
    assert edge in out[node.port]
    # Actual reference to previous evidence, not a new seed lookup. The E
    # premise family consists of the same reflexive branch at every index.
    reflexive=('reflexivity',node.derivation)
    premises=tuple((e,reflexive) for e in out[node.port])
    return Node(registry[edge][1],edge,node,('E',edge,premises))

def peel_twice(node):
    tag,selected,premises=node.derivation
    assert tag=='E'
    branch=dict(premises)[selected]
    assert branch[0]=='reflexivity'
    return branch[1]

states=[initial(v) for v in 'ABCD'];levels=[]
for depth in range(7):
    levels.append({'depth':depth,'packages':len(states),
                   'task_fiber_sizes':sorted({len(out[s.port]) for s in states})})
    next_states=[]
    for node in states:
        for edge in out[node.port]:
            child=step(node,edge)
            assert child.parent is node
            assert peel_twice(child) is node.derivation
            assert child.port==registry[edge][1]
            next_states.append(child)
    states=next_states
assert seed_calls==4
assert [x['packages'] for x in levels]==[4,6,10,16,26,42,68]
# Endpoint return does not discard the retained record or native premises.
a=Node('A',None,None,('seed','A'))
returned=step(step(a,'AB'),'BA')
assert returned.port==a.port and returned!=a
assert returned.parent.parent is a
for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
        'negative_diagnostic':log.strip(),'levels':levels,'initial_seed_calls':seed_calls,
        'formal_results':['Tasks decoded from admitted reified payload',
                          'Native E/reflexivity premises consume retained previous derivation',
                          'Native output premises recover prior complete endpoint and derivation',
                          'Output has explicit admission evidence and can be used by run again',
                          'Decoded complete previous payload retained; no source restart',
                          'Two first-stage interpreted values are provably distinct'],
        'scope':['Declared typed Chain interface and outgoing-edge task policy',
                 'Recovery concerns decoded payload and native history, not arbitrary admission-path proofs',
                 'No generic decoder for arbitrary Complete values',
                 'No new theorem transporting arbitrary initial native derivations under source symmetry',
                 'Fixed wrapper universe over finite retained chains, not universe self-containment',
                 'No privileged task/edge selection, physical time or universal higher filling'],
        'source_hashes':hashes}
(BASE/'results/retained-package-feedback.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
                  'package_counts':[x['packages'] for x in levels],'seed_calls':seed_calls}))
