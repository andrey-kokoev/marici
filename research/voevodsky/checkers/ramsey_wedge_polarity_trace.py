"""Test all involutions exchanging singles and triples and reversing the C3 action. Ask which incidence records on the eight-clique exclude each candidate."""
from pathlib import Path
from collections import Counter
import json,itertools
from ramsey_retention_slice import D,decode
P=D.parent;rows=json.loads((P/'ramsey_wedge_join_reversal.json').read_text());g=decode(next(z['graph6'] for z in json.loads(D.read_text()) if (z['l'],z['k'])==(3,9)));saturated={v for row in json.loads((P/'ramsey_square_edge_families.json').read_text()) for v in row[3]};out=[]
for row in rows:
 r={int(i):j for i,j in row['rotation'].items()};Q=set(r);s,t=row['singles'];q=sum(1<<i for i in Q);a=min(Q-{s,t});A=[a,r[a],r[r[a]]];B=Q-{s,t}-set(A);ext=[g[j]&q for j in range(len(g)) if j not in Q];fam=[v&q for v in saturated if v!=q];items=[]
 for b in sorted(B):
  f={s:t,t:s,**dict(zip(A,[b,r[r[b]],r[b]]))};f.update({j:i for i,j in list(f.items())});assert all(f[r[f[i]]]==r[r[i]] for i in Q)
  def im(m):return sum(1<<f[i] for i in Q if m>>i&1)
  def diff(V):return {k:sum((Counter(v for v in V if v.bit_count()==k)-Counter(im(v) for v in V if v.bit_count()==k)).values()) for k in sorted({v.bit_count() for v in V})}
  items.append(dict(image=b,exterior=diff(ext),saturated=diff(fam)))
 print(row['wedge'],items);out.append(dict(wedge=row['wedge'],items=items))
(P/'ramsey_wedge_polarity_trace.json').write_text(json.dumps(out,indent=1)+'\n')
