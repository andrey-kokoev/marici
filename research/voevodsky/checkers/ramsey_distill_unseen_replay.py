"""Replay held-out SAT decisions by enumerating all maximal-support multisets. Test all size-class ablations across the full census, including the discovery data."""
import json,numpy as np
from itertools import combinations_with_replacement
from ramsey_retention_slice import D,check
P=D.parent;old=json.loads((P/'ramsey_test_distillation.json').read_text());rows=json.loads((P/'ramsey_distill_unseen.json').read_text())['rows'];stats={s:old['counts'][str(s)].copy() for s in range(16)};bad=[]
for i,r in enumerate(rows):
 a=r['g'];assert check(a,2047,3,5);Q=[q for q in range(1,2048) if all(not(q>>j&1 and q&v) for j,v in enumerate(a))];S=[s for s in Q if not any(s!=u and s&u==s for u in Q)];M=np.array(list(combinations_with_replacement(range(len(S)),5)));sig=np.full(len(M),15,dtype=np.uint8)
 for q in Q:
  k=q.bit_count();sig[np.array([bool(s&q) for s in S])[M].sum(axis=1)<k]&=15^(1<<(k-1))
 h=np.bincount(sig,minlength=16)
 for s in stats:stats[s].append(int(sum(h[v] for v in range(16) if v&s==s)))
 assert bool(stats[12][-1])==r['34'][0] and bool(stats[15][-1])==r['1234'][0]
 if stats[12][-1] and not stats[15][-1]:bad.append(dict(row=i,multisets=len(M),partial=stats[12][-1],full=0))
def minimal(options):return [s for s in options if not any(t!=s and s&t==t for t in options)]
out=dict(counterexamples=bad,minimal_verdict= minimal([s for s,x in stats.items() if list(map(bool,x))==list(map(bool,stats[15]))]),minimal_witness=minimal([s for s,x in stats.items() if x==stats[15]]));print(out);(P/'ramsey_distill_unseen_replay.json').write_text(json.dumps(out,indent=1)+'\n')
