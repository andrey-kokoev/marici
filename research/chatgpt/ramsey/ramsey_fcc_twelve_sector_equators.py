"""One FCC tour, with an explicit comparison rule on marked faces (not native spin holonomy)."""
import json
from pathlib import Path
from itertools import permutations
D=json.loads((Path(__file__).resolve().parents[2]/'strominger/results/fcc-first-transport.json').read_text());U=set('1234');V={''.join(p) for p in __import__('itertools').combinations('1234',2)}
walk='13 14 24 23 13 12 14 34 23 12 24 34 13'.split();blocks=[[0,1,2,3],[5,6,7,8],[4,9,10,11]]
def move(x,y):return (int(next(iter(set(x)-set(y))))-1,int(next(iter(set(y)-set(x))))-1)
steps=[move(x,y) for x,y in zip(walk,walk[1:])];assert set(steps)==set(permutations(range(4),2)) and len(steps)==12
site={tuple(v['barycentric']):v['id'] for v in D['vertices']};E={(m['source'],tuple(m['sector']),m['target']) for m in D['directed_moves']};cells=0
for c in D['coarse_cells']:
    if not c['id'].startswith('oct-'):continue
    base=list(map(min,zip(*c['vertices'])));pos={x:tuple(base[i]+(str(i+1) in x) for i in range(4)) for x in V};assert set(pos.values())==set(map(tuple,c['vertices']));assert all((site[pos[x]],s,site[pos[y]]) in E for x,s,y in zip(walk,steps,walk[1:]));cells+=1
mark={'12','13','14'}
for ids in blocks:
    cycle=[walk[j] for j in ids];assert all(walk[j+1]==cycle[(k+1)%4] for k,j in enumerate(ids));p,q=sorted(V-set(cycle));assert set(p)|set(q)==U and not(set(p)&set(q));mark={q if x==p else p if x==q else x for x in mark};print('closed at step',max(ids)+1,'normal pair',p,q,'mark',sorted(mark))
assert mark=={'34','24','23'};print('verified all 12 directed sectors in',cells,'cells')
