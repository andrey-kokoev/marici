"""Delete vertices of a fixed 22-witness. Count all admissible new red-neighbor masks, equally labeled rather than quotienting. Also test two deletions to detect variation before terminality."""
import itertools,json,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';edges=json.loads((D/'ramsey_37_dual_stars.json').read_text())['red_edges'];N=[0]*22
for a,b in edges:N[a]|=1<<b;N[b]|=1<<a
I=[]
def grow(mask,c):
 I.append(mask)
 while c:
  b=c&-c;c^=b;grow(mask|b,c&~N[b.bit_length()-1])
grow(0,(1<<22)-1);F=[s for s in I if s.bit_count()==6];rows=[]
for k in (1,2):
 for ds in itertools.combinations(range(22),k):
  m=sum(1<<i for i in ds);req=[t for t in F if not t&m];allowed=[s for s in I if not s&m and all(s&t for t in req)];degs=sorted((n&~m).bit_count() for i,n in enumerate(N) if not (1<<i)&m);rows.append(dict(deleted=ds,degrees=degs,obligations=len(req),choices=len(allowed),sizes=dict(collections.Counter(s.bit_count() for s in allowed))))
print('single',[(x['deleted'],x['choices']) for x in rows[:22]]);g=collections.defaultdict(list)
for x in rows[22:]:g[tuple(x['degrees'])].append(x)
for v in g.values():print(len(v),[(x['deleted'],x['choices'],x['obligations']) for x in (min(v,key=lambda z:z['choices']),max(v,key=lambda z:z['choices']))]);
(D/'ramsey_37_card_decision_counts.json').write_text(json.dumps(rows,indent=2)+'\n')
