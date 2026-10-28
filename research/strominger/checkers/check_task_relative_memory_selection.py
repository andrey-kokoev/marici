"""Exhaustive finite countermodel census; no physical interpretation."""
from pathlib import Path
from itertools import product
from collections import deque
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
CONTRACT = BASE / 'contracts/task-relative-memory-selection.v1.json'
OUT = BASE / 'results/task-relative-memory-selection'

def main():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    source = ROOT / 'research/nima/agda/ActualSeedEndpointTable.agda'
    native = BASE / 'agda/NativeExtensionFamilyAudit.agda'
    text = source.read_text(encoding='utf-8')
    nt = native.read_text(encoding='utf-8')
    edges = c['source']['edges']
    for name, s, t in edges:
        assert re.search(rf'^source {name} = {s}$', text, re.M)
        assert re.search(rf'^target {name} = {t}$', text, re.M)
        assert re.search(rf'^sigmaEdge {name} = {c["source"]["edge_swap"][name]}$', nt, re.M)
    names = [e[0] for e in edges]
    byname = {name:(s,t) for name,s,t in edges}
    vs = c['source']['vertex_swap']
    es = c['source']['edge_swap']
    for v,w in vs.items():
        assert re.search(rf'^sigma {v} = {w}$', nt, re.M)
    initial = tuple(c['task']['initial'])
    outgoing = {v:[e for e,s,t in edges if s==v] for v in vs}
    def step(p, state, e):
        v,b = state
        s,t = byname[e]
        assert v==s
        return t,b^p[names.index(e)]
    def run(p, word):
        q=initial
        for e in word:q=step(p,q,e)
        return q
    def reachable(p):
        seen={initial}; todo=[initial]
        for q in todo:
            for e in outgoing[q[0]]:
                r=step(p,q,e)
                if r not in seen:seen.add(r);todo.append(r)
        return seen
    def covariant(p):
        return all(step(p,(vs[s],b),es[e]) == (vs[t],step(p,(s,b),e)[1])
                   for e,s,t in edges for b in (0,1))
    def separating_word(p,q):
        todo=deque([(initial,initial,[])])
        seen={(initial,initial)}
        while todo:
            a,b,w=todo.popleft()
            if a!=b:return w
            for e in outgoing[a[0]]:
                x,y=step(p,a,e),step(q,b,e)
                if (x,y) not in seen:
                    seen.add((x,y));todo.append((x,y,w+[e]))
        return None
    all_p=list(product((0,1),repeat=6))
    cov=[p for p in all_p if covariant(p)]
    admitted=[p for p in cov if len(reachable(p))==8]
    assert len(all_p)==64 and len(cov)==8 and len(admitted)==4
    # All primitive Boolean permutations are reversible. Composition is the
    # exact word fold; paired-state reachability covers ALL finite contexts.
    pairs=[]
    for i,p in enumerate(admitted):
        for q in admitted[i+1:]:
            w=separating_word(p,q)
            assert w is not None
            pairs.append({'left':p,'right':q,'witness':w,'left_read':run(p,w),'right_read':run(q,w)})
    red=tuple(int(e in ('AB','BA')) for e in names)
    green=tuple(int(e in ('BC','AD')) for e in names)
    assert red in admitted and green in admitted
    prefix=['AB','BC','CA']; after=prefix+['AB']
    assert run(red,prefix)==run(green,prefix)==('A',1)
    assert run(red,after)==('B',0) and run(green,after)==('B',1)
    # Different implementations are conjugate under vertex-dependent frames,
    # but those maps change the frozen observation at intermediate vertices.
    gauges=[]
    for p in admitted:
        witnesses=[]
        for bits in product((0,1),repeat=3):
            h=dict(zip(('A','B','C','D'),(0,)+bits))
            if all(p[i]==(red[i]^h[s]^h[t]) for i,(e,s,t) in enumerate(edges)):
                witnesses.append(h)
        assert len(witnesses)==1
        gauges.append({'policy':p,'frame_from_red':witnesses[0]})
    files=[CONTRACT,Path(__file__).resolve(),source,native]
    report={'status':'pass','selection_claim':'refuted_at_frozen_task',
            'assignments':64,'covariant':8,'admitted_and_pairwise_contextually_distinct':4,
            'edge_order':names,'policies':admitted,'pairwise_separators':pairs,
            'same_present_record':{'prefix':prefix,'record':['A',1]},
            'future_separator':{'continuation':['AB'],'red':['B',0],'green':['B',1]},
            'vertex_frames_not_observation_preserving':gauges,
            'source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
            'boundary':'Finite exact census and paired transition reachability, not a physical experiment or unrestricted task impossibility.'}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'census.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('status','selection_claim','assignments','covariant','admitted_and_pairwise_contextually_distinct')}))

if __name__=='__main__':main()
