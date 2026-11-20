"""Read visits in order, flip a bit on a non-endpoint column. No mark profiles, edge matching or future visit used by the reader. Compare at closure; test shorter and longer routes separately."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
from ramsey_strip_prism_proof import labels,rep,V
rows=json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text());stats=Counter();res=Counter();sample=[]
for z in rows:
 w=[labels[rep(i)] for i in z['path'][1:-1]];col=lambda v:v[0].upper();ends={col(w[0]),col(w[-1])};bit=0
 for v in w:bit^=int(col(v) not in ends)
 ok=z['closes'];stats[len(w),ok,bit]+=1
 if len(w)==10:
    unused=V-set(w);off=sum(col(v) not in ends for v in unused);assert bit==off%2 and ok==(bit==0);res[off,ok]+=1
    if (z['path'][0],z['path'][-1])==(0,29):sample.append((w,ok))
# Is another column-only toggle set equally predictive, starting at 0, even=close?
codes=[frozenset(c) for k in range(5) for c in combinations('ABCD',k) if all((sum(col(v) in c for v in w)%2==0)==ok for w,ok in sample)];print('classification:',sorted(stats.items()),'unused off-end counts:',res,'literal toggle masks:',codes)
