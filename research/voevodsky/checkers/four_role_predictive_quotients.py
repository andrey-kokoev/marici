"""One common test: coarsest equivalence preserving observations after every allowed move word. Closed deterministic systems only; assembly is explicitly finite one-query control. Fixed frame operations; do not identify underlying state spaces."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1];R=D.parent/'chatgpt/ramsey';load=lambda p:json.loads(p.read_text());
def label(xs):
 m={};return [m.setdefault(x,len(m)) for x in xs]
def refine(obs,trans):
 c=label(obs);curve=[len(set(c))]
 while True:
  z=label([(c[i],tuple(c[t] for t in a)) for i,a in enumerate(trans)]);n=len(set(z))
  if n==curve[-1]:break
  curve.append(n);c=z
 return dict(classes=curve[-1],depth_curve=curve,sizes=sorted(Counter(c).values()),state_classes=c)
P=list(permutations(range(4)));K=lambda a,b:tuple(map(int,f'{999*a+90*b:04d}'));gap=lambda y:(max(y)-min(y),sorted(y)[2]-sorted(y)[1]);G=[(a,b) for a in range(10) for b in range(a+1)];Ys=[K(*g) for g in G];matching=lambda y:tuple(sorted({tuple(sorted((tuple(sorted([p[0],p[3]])),tuple(sorted([p[1],p[2]]))))) for p in P if [y[j] for j in p]==sorted(y)}));kap=refine(list(map(matching,Ys)),[[G.index(gap(y))] for y in Ys]);kap['gap_order']=G
r=load(R/'ramsey_seven_all_wirings.json');S=r['address_masks'];E=list(map(tuple,r['edge_order']));W=sorted(r['wirings']);actions=[]
for swaps in [[(0,1),(2,3)],[(0,1),(4,5)],[(2,4),(3,5)],[(2,5),(3,4)]]:
 p=list(range(7))
 for u,v in swaps:p[u],p[v]=p[v],p[u]
 m=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];e=[E.index(tuple(sorted((m[a],m[b])))) for a,b in E];actions.append([W.index(sum((w>>j&1)<<k for j,k in enumerate(e))) for w in W])
obs=list(map(tuple,load(R/'ramsey38_relative_query.json')['per_input']));ram=refine(obs,list(zip(*actions)));c=ram['state_classes'];ram['actions_on_classes']=[[sorted({c[g[i]] for i in range(8) if c[i]==k}) for k in range(ram['classes'])] for g in actions];p=load(D/'results/ramsey_native_reader_pn_exit.json');ex=[p[k][-1] for k in 'AB'];asm=dict(histories=2,continuations=['NE'],exists_classes=len(set(not s.get('blocked') for s in ex)),face_classes=len({tuple(sorted(s['face'])) for s in ex}),slot_classes=len({tuple(s['packet']['slots']) for s in ex}));o=dict(kaprekar=kap,ramsey=ram,assembly=asm);print(kap['depth_curve'],ram,asm);(D/'results/four_role_predictive_quotients.json').write_text(json.dumps(o,indent=2)+'\n')
