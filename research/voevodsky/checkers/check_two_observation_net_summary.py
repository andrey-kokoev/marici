"""Extend the same port-chain accumulator to parity and has-one readouts."""
from itertools import product
from pathlib import Path
import json

def summary(word):
    p=h=0
    for bit in word:
        assert bit in (0,1)
        # Principal ACC(p,h)--BIT(bit) local rewrite.
        p ^= bit;h |= bit
    return p,h

def join(a,b):return a[0]^b[0],a[1]|b[1]

cases=0
for n in range(11):
    words=list(product((0,1),repeat=n))
    for w in words:
        for cut in range(n+1):
            assert summary(w)==join(summary(w[:cut]),summary(w[cut:]))
            cases+=1
assert {summary(w) for n in range(3) for w in product((0,1),repeat=n)}=={(0,0),(1,1),(0,1)}
assert summary((1,1))==summary(())[:1]+(1,) and summary((1,1))!=summary(())
# These three states are distinguishable by the immediate two-bit readout.
report={'passed':True,'checked_word_splits':cases,'rule':'ACC(p,h)--BIT(b) -> ACC(p xor b,h or b)','reachable_states':[[0,0],[1,1],[0,1]],'composition':'componentwise XOR/OR; empty (0,0) unit','minimality':'three reachable states have distinct immediate (parity,has-one) readouts','limits':'Uniform for these two readouts only; indexed reads or Nima overlap data not modelled.'}
out=Path(__file__).resolve().parents[1]/'results/two-observation-net-summary.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
