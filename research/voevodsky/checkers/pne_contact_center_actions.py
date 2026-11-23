"""P/N/E input only: induce steps by disjointness in one column. Test viewpoint exchange by a single coefficient renaming and column swap, distinct from relational composition."""
import json,itertools
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'pne_four_cover_realizations.json').read_text());out=[]
for index,r in {v['index']:v for v in rows}.items():
 cs=list(map(tuple,r['contacts']));actions=[];graphs=[{i:{j for j,b in enumerate(cs) if set(a[k]).isdisjoint(b[k])} for i,a in enumerate(cs)} for k in range(2)];assert all(set.union(*(g[j] for j in g[i]))==set(g)-g[i] for g in graphs for i in g)
 for p in itertools.permutations('01234'):
  ren=lambda a:''.join(sorted(p[int(x)] for x in a));new=[(ren(b),ren(a)) for a,b in cs];
  if set(new)!=set(cs):continue
  f=[cs.index(x) for x in new];actions.append(dict(rename=''.join(p),mapping=f,fixed=[i for i,j in enumerate(f) if i==j]));assert all({f[j] for j in graphs[k][i]}==graphs[1-k][f[i]] for k in (0,1) for i in graphs[k])
 out.append(dict(index=index,actions=actions,first=cs[0],one=sorted(graphs[0][0]),two=sorted(set(range(10))-graphs[0][0]),directTickEdges=[[2*i+1 in g[2*i] for i in range(5)] for g in graphs]))
print([(v['index'],len(v['actions']),v['directTickEdges']) for v in out]);(D/'pne_contact_center_actions.json').write_text(json.dumps(out,indent=2)+'\n')
