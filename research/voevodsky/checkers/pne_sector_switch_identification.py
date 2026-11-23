"""Test fixed source operations and all their words. Use A=C0,B=M0,C=M1,D=C2 only to name a test edge; matching-order obstruction is invariant under every point renaming."""
from pathlib import Path
from collections import deque,Counter
import json
D=Path(__file__).resolve().parents[1];T={t['outer_arrow']:t['triangle'] for t in json.loads((D.parent/'nima/results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']};E=sorted(T);I=tuple(E);F={e:next(k for k in E if T[e][0]==T[k][0] and e[1]==k[0]) for e in E};S={e:e[::-1] for e in E};todo=deque([(I,'')]);words={}
while todo:
 p,w=todo.popleft()
 if p in words:continue
 words[p]=w
 for a,g in [('F',F),('S',S)]:todo.append((tuple(g[k] for k in p),w+a))
def md(e):return '|'.join(sorted([''.join(sorted(e)),''.join(sorted(set('ABCD')-set(e)))]))
def report(p,w):
 f=dict(zip(E,p));sq=all(f[f[e]]==e for e in E);m={k:sorted({md(f[e]) for e in E if md(e)==k}) for k in sorted(set(map(md,E)))};return dict(word=w or 'I',involutive=sq,matching_action=m,AB_image=f['AB'],sector=T[f['AB']])
rows=[report(p,w) for p,w in words.items()];assert len(rows)==12 and all(len(v)==1 for r in rows for v in r['matching_action'].values());y=[r for r in rows if r['matching_action'][md('AB')]==[md('BC')]];x=[r for r in rows if r['AB_image']=='DC'];assert len(x)==1 and x[0]['involutive'];o=dict(binding=dict(A='C0',B='M0',C='M1',D='C2'),rows=rows,words_to_NN=len(y),involutions_to_NN=sum(r['involutive'] for r in y),word_to_reversed_opposite=x[0]['word'],matching_actions=len({tuple(v[0] for v in r['matching_action'].values()) for r in rows}));print(o['word_to_reversed_opposite'],[(r['word'],r['AB_image']) for r in rows],o['words_to_NN'],o['involutions_to_NN']);(D/'results/pne_sector_switch_identification.json').write_text(json.dumps(o,indent=2)+'\n')
