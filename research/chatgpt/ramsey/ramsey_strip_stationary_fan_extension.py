"""Condition reciprocal incidence dictionaries on B's alternating-walk value only. Count stationary fan images with/without compatibility with the proposed half-step."""
from collections import Counter
from itertools import permutations
from ramsey_strip_fan_dictionary_census import X,P,T,D,H,act
from ramsey_strip_all_corner_fans import images
B,via=images[1];Q,collision=images[4];assert collision==via;counts=Counter();compatible=Counter()
for p in permutations(range(6)):
    a=act(p);d=[a[x] for x in D]
    if d[B]!=via or any(d[d[i]]!=i for i in range(30)):continue
    counts[d[Q]]+=1
    if all(d[H[i]]==H[d[i]] for i in range(30)):compatible[d[Q]]+=1
assert H[B]==Q and H[via]==29 and compatible=={29:2};print('Q images given B -> through-R',dict(sorted(counts.items())),'commuting with H',dict(compatible))
