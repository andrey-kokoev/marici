"""Aligned moving window (known visit index), on five opposite-row strips. Report the first width retaining the same observed next options as a whole prefix. No jumps between strips."""
from collections import defaultdict
from ramsey_strip_next_row_restart import first
for width in range(1,12):
    lost=[]; forks=[]
    for i in range(11):
        prefix=defaultdict(set);frame=defaultdict(set)
        for p in first:
            prefix[p[:i+1]].add(p[i+1]);frame[p[max(0,i-width+1):i+1]].add(p[i+1])
        for h,choices in prefix.items():
            if choices!=frame[h[-width:]]:lost.append((i,h,choices,frame[h[-width:]]))
            if len(choices)>1:forks.append((i,h,sorted(choices)))
    print('width',width,'contexts mixing extra next moves',len(lost));
    if not lost:break
print('observed full-prefix forks:',sorted(forks))
