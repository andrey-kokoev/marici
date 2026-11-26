"""Retain the parent's integer weights on surviving blue demands. An added red edge removes demands containing both endpoints, and forbids supports containing both. Verify each inherited bound on the child's actual maximal supports."""
import json,collections,numpy as np
from ramsey_38_layer46 import P,E,key,unpack,ind
ok=set();seen=set();parents=[]
for f in ['ramsey_38_window_new_types.json','ramsey_38_degree3_weights.json','ramsey_38_degree4_weights.json']:parents.extend(json.loads((P/f).read_text()))
for row in parents:
 a=unpack(int(row['core'],16));I=ind(a);S=[s for s in I if not any(s!=t and s&t==s for t in I)];Q=np.array([int(q) for q in row['weights']]);Y=np.array(list(row['weights'].values()),dtype='int64');sizes=np.array([int(q).bit_count() for q in Q]);
 for i,j in E:
  if a[i]>>j&1 or a[i]&a[j]:continue
  edge=1<<i|1<<j;a[i]^=1<<j;a[j]^=1<<i;k=key(a);a[i]^=1<<j;a[j]^=1<<i;seen.add(k)
  if k in ok:continue
  w=Y*((Q&edge)!=edge);sup=[s for s in S if s&edge!=edge]+[s^(1<<h) for s in S if s&edge==edge for h in (i,j)];den=int(max(((Q[:,None]&np.array(sup))!=0).T@w));num=int(w@sizes)
  if num>7*den:ok.add(k)
print('inherited',len(ok),'of',len(seen));(P/'ramsey_38_layer46_inherited.json').write_text(json.dumps(dict(verified=len(ok),unresolved=sorted(map(hex,seen-ok))))+'\n')
