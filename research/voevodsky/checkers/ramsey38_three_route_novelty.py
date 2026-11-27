"""Route novelty ignores ambient graph, row names, shelling order and within-step attachment order."""
from ramsey38_three_matched_holdout import P as previous,freeze,compare,graph,prev,json,sys
from ramsey38_novel_array_trial import perm_table
from functools import lru_cache
from collections import Counter
P=prev.out/'ramsey38_three_route_novelty_predictions.json';R=prev.out/'ramsey38_three_route_novelty_comparison.json';A=prev.out/'ramsey38_three_route_novelty_scores.json'
protocol='After 1854, fresh canonical eligible arrays through record 6000. Stop at two records with a predicted structurally novel route or 24 eligible records. No filling outcomes in selection. Compare all goals incl abstentions. Novel iff no one permutation of the seven columns preserves ordered edit columns and the three cumulative cell sets of either old route; outside edit rows are distinct and mapped by edit order. Ignore target names and within-stage order. Compare also mesh-only novelty.'
@lru_cache(None)
def signatures(edits,meshes):
    vals=[(bytes(edits).translate(t),tuple(bytes(sorted(bytes(s).translate(t))) for s in meshes)) for t in perm_table()];return repr(min(vals)),repr(min(v[1] for v in vals))
def sig(L,p):
    mask=lambda f:sum(1<<L.index(i) for i in f);assert len(set(x for x,v in p['moves']))==3;return signatures(tuple(mask([v]) for x,v in p['moves']),tuple(tuple(sorted(mask(t) for t in s['cells'])) for s in p['stages']))
def refs():
    marks=set();meshes=set()
    for e in json.loads(previous.read_text())['cases']:
        for p in e['plans']:
            a,b=sig(sorted(graph(e['word'])[e['u']]),p);marks.add(a);meshes.add(b)
    return marks,meshes
def run():
    marks,meshes=refs()
    def annotate(L,plans):
        for p in plans:
            a,b=sig(L,p);p.update(route_class=prev.sha(a.encode()),novel=a not in marks,novel_mesh=b not in meshes)
    def done(es):return len(es)>=24 or sum(any(p['novel'] for p in e['plans']) for e in es)>=2
    freeze(1854,(previous,),P,protocol,annotate,done)
def score():
    compare(P,R);data=json.loads(P.read_text());v=json.loads(R.read_text());counts=Counter();classes=set();examples=[]
    for e,z in zip(data['cases'],v['cases'],strict=True):
        assert e['record']==z['record'];ok=set(map(tuple,z['verified']))
        for p in e['plans']:
            if tuple(p['goal']) not in ok:continue
            counts['novel' if p['novel'] else 'known']+=1;counts['mesh_only_novel']+=p['novel_mesh']
            if p['novel']:classes.add(p['route_class']);examples.append([e['record'],p['goal'],p['moves'],[len(s['cells']) for s in p['stages']]])
    print(v['counts'],counts,len(classes),examples);prev.save(A,dict(verified_sha=prev.sha(R.read_bytes()),counts=dict(counts),new_classes=sorted(classes),examples=examples))
if __name__=='__main__':{'freeze':run,'compare':score}[sys.argv[1]]()
