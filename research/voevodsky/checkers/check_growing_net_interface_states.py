"""Uniform local XOR rule; continuation-state size depends on permitted probes."""
from itertools import product
from pathlib import Path
import json

def fold(bits):
    # Active pair ACC(p) -- BIT(b) -> ACC(p xor b), with the remaining
    # wire reconnected to the next BIT. Only this rule is used for every n.
    state=0
    for bit in bits:
        assert bit in (0,1)
        state ^= bit
    return state

def compose(left_state,right_state):return left_state ^ right_state

sizes=[]
for n in range(1,9):
    words=list(product((0,1),repeat=n))
    assert all(fold(a+b)==compose(fold(a),fold(b)) for a in words for b in ((),(0,),(1,)))
    parity_signatures={fold(w) for w in words}
    # If future contexts include a port-addressed probe READ(i), every
    # distinct word is distinguishable by at least one admitted probe.
    addressed_signatures={tuple(w[i] for i in range(n)) for w in words}
    assert len(parity_signatures)==2 and len(addressed_signatures)==2**n
    for a in words:
        for b in words:
            if a!=b:
                i=next(i for i in range(n) if a[i]!=b[i])
                assert a[i]!=b[i]
    sizes.append({'n':n,'parity_states':2,'addressed_probe_states':2**n})
report={'passed':True,'local_rule':'ACC(p)--BIT(b) -> ACC(p xor b), uniform in n','composition':'xor of segment summaries','parity_only':'two sufficient states for arbitrary finite n','addressed_read':'2^n distinguishable histories; at least n bits of sufficient state','sizes':sizes,'qualification':'READ(i) assumes access to retained indexed ports; XOR folding alone discards them. This is an interface-policy comparison, not a complete interaction-net encoding or model of Nima E/E_B.'}
out=Path(__file__).resolve().parents[1]/'results/growing-net-interface-states.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
