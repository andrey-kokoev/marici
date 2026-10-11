"""Bind the freshly formalized native query to the existing probe table.

The query is selected by a stated task. Its availability does not authorize
exchange dynamics, a physical preparation, counting measure or detector.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
src = ROOT/'agda/NativeSeedTransitionProbe.agda'
receipt = ROOT/'results/agda-NativeSeedTransitionProbe.json'
proof = json.loads(receipt.read_text(encoding='utf-8-sig'))
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256'] == hashlib.sha256(src.read_bytes()).hexdigest()
with redirect_stdout(io.StringIO()):
    previous = runpy.run_path(str(HERE/'check_source_group_probe_selection.py'))

text = src.read_text(encoding='utf-8')
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def table(name):
    entries = dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$',text,re.M))
    assert set(entries) == set('ABCD')
    return tuple('ABCD'.index(entries[v]) for v in 'ABCD')

check('formal-ABC-matches-seed-cycle', table('abc') == previous['generator'](previous['triangles'][0]))
check('formal-ADB-matches-seed-cycle', table('adb') == previous['generator'](previous['triangles'][1]))
probe = previous['probe']
for g in previous['full']:
    for label,(s,t) in previous['registry'].items():
        si,ti = 'ABCD'.index(s),'ABCD'.index(t)
        edge = probe.edges.index((si,ti))
        entry = probe.transition[edge].get(probe.group.index(g),0)
        check('native-transition-table/'+str(g)+'/'+label, entry == int(g[si]==ti))

# The identity counterexample is on every off-diagonal seed role, rather
# than just on a selected numerical coefficient or a later detector model.
for label,(s,t) in previous['registry'].items():
    edge = probe.edges.index(('ABCD'.index(s),'ABCD'.index(t)))
    identity_index = probe.group.index(previous['identity'])
    check('fixed-query-rejected-for-transition-task/'+label,
          probe.fixed[edge].get(identity_index,0)==1
          and probe.transition[edge].get(identity_index,0)==0)

result = {
    'schema':'marici.nima.native-seed-transition-probe.v1','status':'pass','checks':checks,
    'native_operation':'evaluate a supplied retained vertex equivalence at its marked source and compare with the queried target',
    'formal':'actual native-table filler bridge, retained-filler recovery, composition and six seed-edge cycle attachments',
    'task_relative_selection':'the existing directed-transition dictionary is the query table; endpoint-fixing answers a different question',
    'pointed_boundary':'fillers go from prepared x to prepared g(x); not all g are automorphisms of one fixed pointed package',
    'unselected':['whether this is the physical task','counting/energy pairing','excited preparation',
                  'exchange event law','physical charge and mass','duration and detector calibration'],
    'formal_receipt_sha256':hashlib.sha256(receipt.read_bytes()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/native-seed-transition-probe.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} source-table bindings; fresh safe-Cubical native query proof verified')
print('Directed-transition query now attached to actual retained/native fillers for a stated task.')
print('No physical interaction, preparation or exchange law selected by query evaluation.')
