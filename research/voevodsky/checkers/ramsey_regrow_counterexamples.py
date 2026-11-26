"""Replay each exceptional induced core, enumerate ALL restoring neighborhoods and classify by the corners they join."""
import json,collections,gzip
from ramsey_retention_slice import D,CAT,decode,check
P=D.parent;rows=[r for r in json.loads((P/'ramsey_regrow_all27.json').read_text())['illegal'] if not r[-2]];ids={r[0] for r in rows};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[]
for ix,s,t,x,y,dl,*_ in rows:
 a=A[ix];mask=((1<<27)-1)^(1<<dl);I=[0];
 for i,v in enumerate(a):
  if i!=dl:I.extend([q|1<<i for q in I if not q&v]);
 U=mask&~(a[s]|a[t]|a[x]|a[y]);Q=[q for q in I if not q&~U and q.bit_count()==5];assert any(all(all(a[v]&a[c]&mask for c in (s,t,x,y)) for v in range(27) if q>>v&1) for q in Q);sevens=[q for q in I if q.bit_count()==7];ok=[z for z in I if all(q&z for q in sevens)];assert a[dl] in ok
 for z in ok:
  assert (z&(1<<s|1<<t)).bit_count()==(z&(1<<x|1<<y)).bit_count()==1
  b=[(v&mask)|((z>>j&1)<<dl) for j,v in enumerate(a)];b[dl]=z;assert check(b,(1<<27)-1,3,8)
 out.append(dict(row=ix,dl=dl,c=[s,x,t,y],quintuples=Q,regrowth=ok));
print('parents',len(ids),'distinct deletions',len({(r['row'],r['dl']) for r in out}),'regrowth',collections.Counter(len(r['regrowth']) for r in out),'bad Q',collections.Counter(len(r['quintuples']) for r in out));print(out[0]);(P/'ramsey_regrow_counterexamples.json').write_text(json.dumps(out)+'\n')
