"""Exact four-state countermodel with a frame-invariant loop obstruction."""
from pathlib import Path
from itertools import product, permutations
import json
import hashlib

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
contract=BASE/'contracts/task-relative-four-state-selection.v1.json'
c=json.loads(contract.read_text(encoding='utf-8'))
source=ROOT/c['source_contract']
s=json.loads(source.read_text(encoding='utf-8'))['source']
edges=s['edges']; names=[e[0] for e in edges]
byname={e:(a,b) for e,a,b in edges}
outgoing={v:[e for e,a,b in edges if a==v] for v in s['vertices']}
def policy(a,b,c):return dict(zip(names,(a,b,c,b,c,a)))
def step(p,state,e):
    v,b=state; a,t=byname[e]; assert a==v
    return t,(b+p[e])%4
def run(p,word,start=('A',0)):
    for e in word:start=step(p,start,e)
    return start
def reachable(p):
    seen={('A',0)}; todo=[('A',0)]
    for state in todo:
        for e in outgoing[state[0]]:
            q=step(p,state,e)
            if q not in seen:seen.add(q);todo.append(q)
    return seen
all_p=[policy(*a) for a in product(range(4),repeat=3)]
for p in all_p:
    for e,a,b in edges:
        assert sorted((x+p[e])%4 for x in range(4))==list(range(4))
        assert p[e]==p[s['edge_swap'][e]]
        for x in range(4):
            assert step(p,(s['vertex_swap'][a],x),s['edge_swap'][e]) == (s['vertex_swap'][b],(x+p[e])%4)
admitted=[p for p in all_p if len(reachable(p))==16]
assert len(admitted)==32
p=policy(1,1,1);q=policy(0,1,0)
assert p in admitted and q in admitted
loop=['AB','BA']; prefix=['AB','BC','CA']*2
assert run(p,prefix)==run(q,prefix)==('A',2)
assert run(p,prefix+loop)==('A',0)
assert run(q,prefix+loop)==('A',2)
p_loop=[run(p,loop,('A',x))[1] for x in range(4)]
q_loop=[run(q,loop,('A',x))[1] for x in range(4)]
assert p_loop==[2,3,0,1] and q_loop==[0,1,2,3]
# Any vertexwise transition intertwiner must intertwine this A-return loop.
frames=[h for h in permutations(range(4)) if all(h[p_loop[x]]==q_loop[h[x]] for x in range(4))]
assert not frames
report={'status':'pass','selection_claim':'refuted_even_up_to_vertex_state_frames',
        'covariant_shift_policies':64,'reachable_policies':32,
        'first_policy':p,'second_policy':q,'common_prefix':prefix,'same_present_record':['A',2],
        'separating_return_continuation':loop,'first_later':['A',0],'second_later':['A',2],
        'loop_permutations':[p_loop,q_loop],'permutations_tested':24,'intertwining_frames':0,
        'proof':'The AB;BA action is a fixed-point-free shift by two in one model and identity in the other. Conjugacy cannot change identity into that permutation.',
        'source_hashes':{str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (contract,source,Path(__file__).resolve())},
        'scope':'Exact finite task countermodel; no new original-rule Agda binding for the four-state instance and no physical assertion.'}
out=BASE/'results/task-relative-memory-selection/four-state.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ('status','selection_claim','covariant_shift_policies','reachable_policies','intertwining_frames')}))
