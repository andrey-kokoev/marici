"""Complete finite policy census for the existing native Boolean instrument.

All reversible permutations of Vertex x Bool are tested, not just two
examples. Correct blank-register recording and repeatability of the measured
query are fixed. Additional protected readouts are explicit policies.
"""
from itertools import permutations, combinations
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
formal = ROOT/'agda/NativeTransitionInstrument.agda'
proof_path = ROOT/'results/agda-NativeTransitionInstrument.json'
proof = json.loads(proof_path.read_text(encoding='utf-8-sig'))
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256'] == hashlib.sha256(formal.read_bytes()).hexdigest()
text = (ROOT/'agda/NativeSeedTransitionProbe.agda').read_text(encoding='utf-8')
abc_dict = dict(re.findall(r'^abc ([ABCD]) = ([ABCD])$',text,re.M))
abc = tuple('ABCD'.index(abc_dict[x]) for x in 'ABCD')
states = tuple((x,b) for x in range(4) for b in range(2))
index = {s:i for i,s in enumerate(states)}
query = lambda x,target: int(abc[x]==target)
measured_target = 1  # B: the measured query singles out input A.
checks=[]


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def preserves(table, target):
    return all(query(states[table[i]][0],target)==query(x,target)
               for i,(x,b) in enumerate(states))


admissible=[]
for table in permutations(range(8)):
    correct = all(states[table[index[(x,0)]]][1] == query(x,measured_target) for x in range(4))
    if correct and preserves(table,measured_target):
        admissible.append(table)
check('complete-reversible-census', len(admissible)==36)

recorder = tuple(index[(x,b^query(x,measured_target))] for x,b in states)
check('native-recorder-in-class', recorder in admissible)

# Structural classification: true fiber is forced; false fiber has two
# independently permutable triples, one per memory input. This is 3!*3!.
false_states = tuple(x for x in range(4) if not query(x,measured_target))
reconstructed=set()
for p0 in permutations(false_states):
    for p1 in permutations(false_states):
        maps=[dict(zip(false_states,p0)),dict(zip(false_states,p1))]
        table=tuple(index[(x,1-b)] if query(x,measured_target)
                    else index[(maps[b][x],b)] for x,b in states)
        reconstructed.add(table)
check('classification-two-independent-permutations', reconstructed==set(admissible))

rows=[]
other_targets=tuple(t for t in range(4) if t!=measured_target)
for size in range(4):
    for protected in combinations(other_targets,size):
        candidates=[p for p in admissible if all(preserves(p,t) for t in protected)]
        expected={0:36,1:4,2:1,3:1}[size]
        check('protected-readout-count/'+str(protected),len(candidates)==expected)
        rows.append({'extra_target_queries':['ABCD'[t] for t in protected],
                     'admissible_instruments':len(candidates)})
        if size>=2:
            check('protected-readouts-select-recorder/'+str(protected),candidates==[recorder])

source_preserving=[p for p in admissible if all(states[p[i]][0]==x for i,(x,b) in enumerate(states))]
check('whole-source-protection-unique',source_preserving==[recorder])
check('chosen-policy-produces-no-source-recoil',all(states[recorder[i]][0]==x for i,(x,b) in enumerate(states)))
check('reused-register-does-not-grow-history',all(recorder[recorder[i]]==i for i in range(8)))

# A weak observation does not license erasure of the full input: each
# candidate remains exactly invertible despite potential source disturbance.
for n,p in enumerate(admissible):
    inverse=tuple(p.index(i) for i in range(8))
    check('full-state-recovery/'+str(n),all(inverse[p[i]]==i for i in range(8)))

result={
    'schema':'marici.nima.native-instrument-policy-classification.v1','status':'pass','checks':checks,
    'domain':'all 8! permutations of the actual four-vertex source times one Boolean memory register',
    'fixed_requirements':['correct answer on blank memory','preserve the measured query value','reversibility'],
    'admissible_count':36,
    'classification':'two independent S3 permutations of the false-answer fiber, one for each input memory value; true-answer fiber forced',
    'additional_protection_policies':rows,
    'unique_fully_protected_policy':'record-only (x,b)->(x,b XOR answer(x))',
    'physics_boundary':'uniqueness under full source protection selects zero source backaction, not charge/mass recoil. Nontrivial interaction requires an independently justified change-permission/control law.',
    'native_boundary':'finite permutations admit explicit inverse equivalences, but the 36-term census is Python verification; only the earlier recorder and rival were individually instantiated in Agda',
    'resource_boundary':'memory initialization, fresh-record allocation, physical implementation, energy and duration remain external',
    'formal_receipt_sha256':hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/native-instrument-policy-classification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} finite policy checks, exhaustive over 40320 reversible maps')
print('Only measured query protected: 36. One extra singleton query: 4. Two extra: 1.')
print('The unique fully protected instrument is the native zero-source-backaction recorder.')
