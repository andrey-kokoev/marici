"""What do switch marks encode beyond the closure bit? In the folded moving prism, independently enumerate residual matchings and check the edge-type budget for all 96 reflected routes. Compare information present in published mark totals vs time-stamped common marks."""
from collections import Counter
from pathlib import Path
import json
from ramsey_strip_prism_proof import V,E,labels,rep

def match(left):
    if not left:yield ();return
    x=min(left)
    for y in sorted(left-{x}):
        if tuple(sorted((x,y))) in E:
            for rest in match(left-{x,y}):yield ((x,y),)+rest
rows=json.loads(Path(__file__).with_name('ramsey_strip_length_control.json').read_text());hist=Counter();n=0
for r in rows:
    path=r['path'];w=[labels[rep(x)] for x in path[1:-1]];L=r['length'];k=sum(len(x)==1 for x in w[1:-1]);rem=V-set(w);ms=list(match(rem));assert bool(ms)==r['closes'];
    for m in ms:
        vertical=sum(any(len(x)==1 for x in pair) for pair in m);horizontal=len(m)-vertical;assert (vertical,horizontal)==(2-k,(9+2*k-L)//2);n+=1
    left,right=w[0].lower(),w[-1].lower();a={i for i,x in enumerate(w) if x[0]==left and len(x)==2};d={i for i,x in enumerate(w) if x[0]==right and len(x)==2};switch={i for i,x in enumerate(w) if len(x)==1 and 0<i<len(w)-1};assert not a&d and [len(t|switch) for t in (a,d)]==r['counts']
    if L==11 and (path[0],path[-1])==(0,29):hist[k,r['closes'],tuple(sorted(rem))]+=1
print('routes:',len(rows),'folded completions:',n,'literal L11 (k,closes,remaining):',dict(hist))
