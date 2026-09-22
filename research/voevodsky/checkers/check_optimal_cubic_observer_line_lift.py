"""Audit the old graded-line lift against the full matched norming observer.

Rebuild only its exact combinatorial matching, not the expensive Acb norm
certificate. Arbitrary path outputs are resolved in true analytical blocks.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import defaultdict,deque
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
a=runpy.run_path(str(ROOT/'research/grothendieck/checkers/audit_cubic_analytical_shapes.py'))
f=a['f'];columns=a['columns'];rows=a['shape_rows']
support={sh for sh,sg,w in columns[18]['entries']}
J={sh:sg for sh,sg,w in columns[18]['entries']}
reserve=next(e for e in columns[0]['entries'] if len(rows[e[0]])==1 and e[2]==((0,1),(3,7)))
for j,col in enumerate(columns):
    if j==18:continue
    private=defaultdict(deque)
    for sh,sg,w in col['entries']:
        if len(rows[sh])==1 and sh!=reserve[0]:private[w].append((sh,sg))
    for sh,sg,w in col['entries']:
        if sh in support:
            repl,rsg=private[w].popleft()
            assert repl not in J
            J[repl]=-J[sh]*sg*rsg
assert len(J)==448 and reserve[0] not in J

def raw3(column):
    out=defaultdict(int)
    for (word,marks),c in column.items():
        states=[0]
        for p in word:states.append(states[-1]|(1<<p))
        for cuts in combinations(range(len(word)),3):
            seams=tuple(('e',states[k],states[k+1],marks[k]) for k in cuts)
            bounds=(-1,)+cuts+(len(word),)
            buffers=[tuple((states[k],states[k+1]) for k in range(lo+1,hi) if marks[k])
                     for lo,hi in zip(bounds,bounds[1:])]
            shape=(seams,tuple(map(len,buffers)))
            windows=[]
            for i,k in enumerate(cuts):
                windows.extend(buffers[i])
                if marks[k]:windows.append((states[k],states[k+1]))
            windows.extend(buffers[-1])
            out[shape,tuple(windows)]+=c
    return {k:c for k,c in out.items() if c}

v2=f['chain_product']([f['relation']((0,1),1),f['relation']((2,3),0)])
contexts=[]
for word in permutations((4,5)):
    for marks in product((0,1),repeat=2):
        image=raw3(f['multiply'](v2,{(word,marks):1}))
        # Test exact tensors before scalar norming: no positivity assumptions.
        terms={key:c for key,c in image.items() if key[0] in J or key[0]==reserve[0]}
        assert not terms,(word,marks,terms)
        contexts.append((word,marks))
result={'passed':True,'full_norming_blocks':len(J)+1,'contexts_checked':len(contexts),
 'all_selected_analytical_blocks_vanish_on_old_line_contexts':True,
 'scope':'Exact support of the specified matched-private optimum. This extends the old graded-line lift and adjacent nullhomotopy to its source-action correction. It does not reverify the all-prime numerical norm enclosure or supply physical implementation budgets.'}
out=ROOT/'research/voevodsky/results/optimal-cubic-observer-line-lift.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
