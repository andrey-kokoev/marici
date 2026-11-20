"""Do three marked position-pairs determine the chosen Hall matching among all 288? The observation is the actual matched edge at each position, not its profile. Test both alternating choices, both bridge readings, and every three-position control. Each matched incidence selects a unique Kneser deletion."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
from ramsey_strip_bridge_profiles import rows,profiles,out as prof,ds,ms
H=Path(__file__).parent;tables=[]
def gen(m,used):
    if len(m)==15:
        tables.append(tuple([15+j for j in m]+[m.index(j) for j in range(15)]));return
    for j,t in enumerate(ms):
        if ds[len(m)] in t and j not in used:gen(m+[j],used|{j})
gen([],set());assert len(tables)==288
bits={(u,v):sum(1<<i for i,t in enumerate(tables) if t[u]==v) for u in range(30) for v in set(t[u] for t in tables)};full=(1<<288)-1;hist=Counter();control=Counter();singles=Counter();minimal=Counter();half=Counter();handoff=Counter()
for row,p in zip(rows,profiles):
    C=row['cycle'];chosen=[tuple(i for i in range(1,11) if p[i-1] in rule) for rule in prof['whole']['examples']];assert all(len(s)==3 for s in chosen)
    for parity in (0,1):
        def obs(i):return bits[C[i],C[(i+(1 if i%2==parity else -1))%22]]
        def fit(T,both=True):
            m=full
            for i in T:m&=obs(i);m=m&obs(22-i) if both else m
            return m.bit_count()
        # The cycle alone may admit multiple completions off-strip, an important ceiling.
        ceiling=fit(range(1,11));singles[ceiling]+=1
        for s in chosen:
            m=full
            for i in s:m&=obs(i)&obs(22-i)
            if m.bit_count()==2:handoff[((m&obs(0)).bit_count(),(m&obs(11)).bit_count(),(m&obs(0)&obs(11)).bit_count())]+=1
            n=fit(s);hist[n]+=1;half[fit(s,False)]+=1;minimal[min(k for k in range(1,4) if any(fit(sub)==n for sub in combinations(s,k)))]+=1
        for t in combinations(range(1,11),3):control[fit(t)]+=1
print('handoff candidates for the ambiguous tests:',handoff);print('chosen',hist,'half',half,'control',control,'all visit pairs',singles,'minimum to equal chosen',minimal);(H/'ramsey_strip_three_readings.json').write_text(json.dumps(dict(handoff={str(k):v for k,v in handoff.items()},chosen=hist,one_side=half,controls=control,all_pairs=singles,minimum_to_match_chosen=minimal),indent=2)+'\n')
