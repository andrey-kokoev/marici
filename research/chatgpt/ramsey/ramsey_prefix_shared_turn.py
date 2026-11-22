"""Two-flag incidence rule, before receipt; subsequent path as control."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter,defaultdict
import json
D=Path(__file__).parent;load=lambda p:json.loads(p.read_text());X=list(combinations(range(1,5),2));P=list(combinations(range(6),2));V=set(range(1,5));seed=load(D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json');E=set(map(tuple,seed['arrows']));rim={e for e in E if e[::-1] not in E};seam={v for a,b in E-rim for v in (a,b)};turns={(a,b,c) for a,b in rim for x,c in rim if x==b and a in seam and c in seam};paths=load(D/'ramsey_boundary_role_table.json');trip={};raw=[]
for z in paths:
    w=z['path'];e,f=map(set,[X[k] for k in P[w[0]]]);b,=e&f;q,=V-e-f;tips=e^f;score={t:sum(t in X[k] for k in P[w[2]]) for t in tips};x,=[t for t in tips if score[t]==max(score.values())];common,=set(P[w[0]])&set(P[w[4]]);assert set(X[common])=={b,x};other,=set(P[w[0]])-{common};assert set(X[other])&set(X[common])=={b};trip[tuple(w[:3])]=(b,x,q);raw.append(dict(prefix=w[:3],scores=score,triple=[b,x,q]));
# Identify old row prefixes by their input marks, not emitted arrows.
ps=[(0,16,13),(0,17,12)];cases=[]
for p in permutations('ABCD'):
    tr=[tuple(p[i-1] for i in trip[s]) for s in ps];
    if {tr[0][0],tr[0][2]}!=seam:continue
    forward=[t in turns for t in tr];assert forward[0]!=forward[1];cases.append(dict(binding=''.join(p),triples=tr,forward=forward,predict_stationary=forward))
obs=load(D/'ramsey_execution_rim_bit.json')['rows'];scores=Counter()
for z in cases:
    for i,guess in enumerate(z['predict_stationary']):
        row,=[r for r in obs if r['binding']==z['binding'] and r['row']==i];actual=row['first'][1]==z['binding'][0];scores[guess==actual]+=1;assert guess==actual
out=dict(source_outer_paths=list(sorted(turns)),prefix_results=raw,cases=cases,correct=scores[True],forward_row_zero=[z['binding'] for z in cases if z['forward'][0]],reverse_row_zero=[z['binding'] for z in cases if not z['forward'][0]]);print(out);(D/'ramsey_prefix_shared_turn.json').write_text(json.dumps(out,indent=2)+'\n')
