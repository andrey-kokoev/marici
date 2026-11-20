"""Encode the upper triangle in balanced row order; test every possible anchor."""
import csv
import json
from itertools import combinations
from pathlib import Path

root = Path(__file__).parent
with (root/'ramsey_balanced_order_20.csv').open(newline='') as f:
    h,*rows = list(csv.reader(f))
labels = list(map(int,h[1:]))
assert len(set(labels)) == len(labels) == 20 and labels == [int(r[0]) for r in rows]
m = [list(map(int,r[1:])) for r in rows]
assert all(len(r)==20 and set(r)<={0,1} for r in m)
assert all(m[i][i]==0 and all(m[i][j]==m[j][i] for j in range(20)) for i in range(20))
pairs = list(combinations(range(20),2)); bits = [m[i][j] for i,j in pairs]
delta = [a^b for a,b in zip(bits,bits[1:])]

def decode(delta, anchor, value):
    x = [0]*(len(delta)+1); x[anchor] = value
    for t in range(anchor,len(delta)): x[t+1] = x[t]^delta[t]
    for t in range(anchor-1,-1,-1): x[t] = x[t+1]^delta[t]
    return x

for t,b in enumerate(bits):
    assert decode(delta,t,b)==bits
    assert decode(delta,t,1-b)==[1-v for v in bits]
(root/'ramsey_relative_chain_20.json').write_text(json.dumps({'address_order':labels,'pair_order':'strict upper triangle, row by row','different_from_next':''.join(map(str,delta))},indent=2)+'\n')
print(len(delta),'comparisons;',len(bits),'anchors verified;',sum(bits),'present links')
