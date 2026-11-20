"""On ten literal 11-step strips, separately test a complete time-stamped switch log, equality of rim-corner visit counts without switches, and the 3/3 threshold after removing switch marks. Ground truth from closure census, not profile labels."""
from collections import Counter,defaultdict
from pathlib import Path
import json
from ramsey_strip_prism_proof import rep,labels
rows=[z for z in json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text()) if (z['path'][0],z['path'][-1])==(0,29)]
logs=defaultdict(Counter);out=Counter()
for z in rows:
 w=[labels[rep(x)] for x in z['path'][1:-1]];log=tuple((i,v) for i,v in enumerate(w,1) if v in ('B','C'));a=sum(v in ('a0','a1') for v in w);d=sum(v in ('d0','d1') for v in w);ok=z['closes'];assert [a+len(log),d+len(log)]==list(map(len,z['selected']));assert (a==d)==ok;assert all(i not in (3,8) for i,v in log);logs[log][ok]+=1;out[a,d,ok]+=1
assert len(rows)==10
print('log -> outcome',dict(logs));print('corner counts -> outcome',out)
