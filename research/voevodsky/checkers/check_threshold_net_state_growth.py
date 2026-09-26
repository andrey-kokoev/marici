"""Fixed threshold vocabulary has bounded monoid; variable thresholds require counts."""
from itertools import product
from pathlib import Path
import json

def capped(word,K):
    state=0
    for bit in word:state=min(K,state+bit)
    return state

def merge(a,b,K):return min(K,a+b)

K=3;checks=0
for n in range(11):
    for word in product((0,1),repeat=n):
        for cut in range(n+1):
            assert capped(word,K)==merge(capped(word[:cut],K),capped(word[cut:],K),K)
            checks+=1
    assert len({capped(w,K) for m in range(n+1) for w in product((0,1),repeat=m)})==min(K,n)+1
# For all words of exact length n, their numbers of ones 0..n are
# distinguishable by an allowed threshold query at the next larger count.
for n in range(1,17):
    representatives=[(1,)*c+(0,)*(n-c) for c in range(n+1)]
    signatures={tuple(sum(w)>=k for k in range(1,n+1)) for w in representatives}
    assert len(signatures)==n+1
report={'passed':True,'fixed_threshold_K':K,'fixed_states':K+1,'split_checks':checks,'composition':'min(K,a+b)','variable_thresholds':'n+1 distinguishable count states on length n for probes k=1..n','size_note':'state count grows linearly; binary storage needs ceiling(log2(n+1)) bits','limits':'Threshold index supplied by observation interface; schematic local counter rule, not Nima overlap model.'}
out=Path(__file__).resolve().parents[1]/'results/threshold-net-state-growth.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
