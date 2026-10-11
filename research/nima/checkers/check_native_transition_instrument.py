"""Finite audit of the freshly formalized reversible native query instruments."""
from collections import deque
from itertools import product
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
src = ROOT/'agda/NativeTransitionInstrument.agda'
query = ROOT/'agda/NativeSeedTransitionProbe.agda'
proof_path = ROOT/'results/agda-NativeTransitionInstrument.json'
proof = json.loads(proof_path.read_text(encoding='utf-8-sig'))
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256'] == hashlib.sha256(src.read_bytes()).hexdigest()


def table(path, name):
    entries = dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$', path.read_text(encoding='utf-8'), re.M))
    assert set(entries) == set('ABCD')
    return tuple('ABCD'.index(entries[v]) for v in 'ABCD')


abc, adb, h = table(query,'abc'), table(query,'adb'), table(src,'h')
identity = tuple(range(4))
compose = lambda g,f: tuple(g[f[x]] for x in range(4))
words = {identity:()}
queue = deque([identity])
while queue:
    f = queue.popleft()
    for label,g in [('ABC',abc),('ADB',adb)]:
        gf = compose(g,f)
        if gf not in words:
            words[gf] = words[f]+(label,)
            queue.append(gf)
assert len(words)==12 and h in words
answer = lambda x: int(abc[x]==1)
record = lambda s: (s[0],s[1]^answer(s[0]))
rival = lambda s: (h[s[0]],s[1]^answer(s[0]))
states = list(product(range(4),range(2)))
checks=[]

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


check('rival-in-existing-cycle-group', h in words)
check('record-bijection', len({record(s) for s in states})==8)
check('rival-bijection', len({rival(s) for s in states})==8)
for s in states:
    check('record-involution/'+str(s), record(record(s))==s)
    check('same-record/'+str(s), record(s)[1]==rival(s)[1])
    check('query-preserved-by-rival/'+str(s), answer(rival(s)[0])==answer(s[0]))
for x in range(4):
    check('blank-memory-readout/'+str(x), record((x,0))[1]==rival((x,0))[1]==answer(x))
check('different-source-backaction', record((1,0)) != rival((1,0)))
check('record-written-on-true-query', record((0,0))==(0,1))
check('reuse-is-not-fresh-record', record(record((0,0)))==(0,0))
result={
    'schema':'marici.nima.native-transition-instrument.v1','status':'pass','checks':checks,
    'construction':'reversible XOR query recorder on actual Vertex x Bool; plus a query-preserving source transport rival',
    'rival_source_word':list(words[h]),
    'same_task_different_backaction':{'input':['B',False],'record_only':['B',False],'rival':['C',False]},
    'native_scope':'both operations have actual typed filler witnesses between their prepared source/target packages',
    'selection_boundary':'Boolean memory, initialized register and recording policy are supplied. Native admissibility and repeatable query values do not choose state backaction.',
    'resource_boundary':'no physical memory preparation cost, energy, charge coupling or duration inferred; bit reuse does not append a fresh record',
    'formal_receipt_sha256':hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (src,query)},
}
(ROOT/'results/native-transition-instrument.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} native instrument controls, with fresh formal receipt')
print('Query recording constructed; native-compatible backaction is not unique.')
print('Rival source-cycle word:',words[h])
