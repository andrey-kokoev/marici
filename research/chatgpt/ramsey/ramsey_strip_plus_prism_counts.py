"""Count by rim runs, not by generating the ten strips. Fixed poles A,D; starts on either rim. Each internal midpoint B/C switches rims. On one square, a simple run between distinct corners uses 2, 3, or 4 corners."""
from collections import Counter
from ramsey_strip_prism_proof import labels
from ramsey_strip_mixed_mod_holdout import dist,rules
bridge=(0,15,9,29);marks=[{name for v,name in labels.items() if tuple(dist[v][j] for j in bridge) in rule} for rule in rules];assert marks==[{'a0','a1','B','C'},{'d0','d1','B','C'}];freq=Counter();ret=Counter()
# lower-case: corner on current rim; upper-case: midpoint; switching toggles rim.
for switch,word in [('B','AadcbBb{}dD'),('C','Aa{}cCcbadD'),('BC','AabBbcCcdD')]:
    opts={'B':'ac','C':'bd','BC':'-'}[switch];local=Counter()
    for opt in opts:
        w=word.format(opt);assert len(w)==10
        for i,c in enumerate(w,1):
            if c in 'aBC':freq[i]+=2;local[i]+=1
            if c in 'dBC':ret[i]+=2
    print(switch,'forward per entry rim',dict(sorted(local.items())))
assert [freq[i] for i in range(1,11)]==[ret[i] for i in range(10,0,-1)]==[0,10,0,2,4,4,2,6,0,0]
print('F',list(freq[i] for i in range(1,11)),'R',list(ret[i] for i in range(1,11)))
