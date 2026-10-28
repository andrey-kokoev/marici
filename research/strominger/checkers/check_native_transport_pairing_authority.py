"""Audit the exact additional premise needed to select the pairing."""
from pathlib import Path
from fractions import Fraction as F
import contextlib
import hashlib
import io
import json
import re
import runpy

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]
with contextlib.redirect_stdout(io.StringIO()):
    p = runpy.run_path(str(BASE/'checkers/check_native_query_pairing_selection.py'))
group, compose, inverse = p['group'], p['compose'], p['inverse']
source = ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda'
text = source.read_text(encoding='utf-8')
def table(name):
    rows=dict(re.findall(r'^'+name+r' ([ABCD]) = ([ABCD])$',text,re.M))
    assert set(rows)==set('ABCD')
    return tuple('ABCD'.index(rows[v]) for v in 'ABCD')
generators=[table('abc'),table('adb')]
assert generators==p['generators']
# Equal weights along these edges are exactly the diagonal-metric generator
# isometry constraints. Their connected graph has a one-dimensional solution.
seen={p['identity']};todo=list(seen)
for g in todo:
    for h in generators:
        hg=compose(h,g)
        if hg not in seen: seen.add(hg);todo.append(hg)
assert seen==set(group)
# Query composition remains true regardless of either chosen pairing.
count=0
for h in group:
    for g in group:
        for a in range(4):
            for b in range(4):
                assert int(compose(h,g)[a]==b)==sum(int(g[a]==v)*int(h[v]==b) for v in range(4))
                count+=1
f_ab=tuple(F(g[0]==1) for g in group)
h=generators[1]
left_f=tuple(f_ab[group.index(compose(inverse(h),g))] for g in group)
assert left_f==tuple(F(g[0]==0) for g in group)
w=tuple(F(2 if g!=p['identity'] and compose(g,g)==p['identity'] else 1,4) for g in group)
before=p['dot'](f_ab,f_ab,w);after=p['dot'](left_f,left_f,w)
assert before==1 and after==F(3,4)
files=[source,Path(__file__).resolve(),BASE/'native-transport-pairing-authority-v1.md']
report={'status':'pass','native_generators':generators,'composition_checks':count,
        'weight_constraint_connected_components':1,'weight_constraint_rank':11,
        'witness':{'transport':'ADB acting by left pullback','query_before':'A to B','query_after':'A to A',
                   'squared_norm_before':str(before),'squared_norm_after':str(after)},
        'finding':'Native equivalence and query composition do not imply isometry of the independently attached pairing.',
        'conditional_repair':'Requiring both native triangle left actions to preserve the diagonal carrier pairing forces uniform weights.',
        'scope':'Exact finite replay plus written general argument, not fresh Agda closure or physical authority.',
        'sha256':{str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=BASE/'results/native-query-pairing-selection/transport-authority.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','composition_checks','weight_constraint_rank','witness')}))
