"""Explicit linear port-boundary rewrite for ACC--BIT0/BIT1 insertion.

ACC principal meets BIT principal. ACC aux is connected to unary-head
principal; BIT aux is connected to the next-input principal. On BIT1,
new UNIT principal/aux is inserted between ACC aux and the old head.
The query is deliberately NOT implemented by this checker.
"""
from pathlib import Path
import json

def pair(a,b):return frozenset((a,b))

def check(wires,ports):
    assert len(wires)==len({p for w in wires for p in w})//2
    assert all(len(w)==2 for w in wires)
    assert {p for w in wires for p in w}==ports

def rewrite(bit,head_is_nil=False):
    assert bit in (0,1)
    head='N.p' if head_is_nil else 'U0.p'
    ports={'A.p','A.a','B.p','B.a',head,'NEXT.p'}
    before={pair('A.p','B.p'),pair('A.a',head),pair('B.a','NEXT.p')}
    check(before,ports)
    # Active pair consumes old A and B. Recreate A2; connect its principal
    # to NEXT.p. For 1, insert a fresh unary UNIT between A2.a and head.
    if bit:
        after={pair('A2.p','NEXT.p'),pair('A2.a','Unew.p'),pair('Unew.a',head)}
        after_ports={'A2.p','A2.a','Unew.p','Unew.a',head,'NEXT.p'}
    else:
        after={pair('A2.p','NEXT.p'),pair('A2.a',head)}
        after_ports={'A2.p','A2.a',head,'NEXT.p'}
    check(after,after_ports)
    assert sum(head in w for w in after)==1 and sum('NEXT.p' in w for w in after)==1
    return len(after),len(after_ports)

assert rewrite(0)==(2,4) and rewrite(1)==(3,6)
assert rewrite(0,True)==(2,4) and rewrite(1,True)==(3,6)
report={'passed':True,'local_rules':'ACC.p--BIT.p; BIT0 reconnect A2.a to head, BIT1 inserts fresh UNIT on unary head wire; A2.p reconnects next','linearity':'all pre/post ports occur on exactly one wire; external head/next each once','tested':'BIT0/BIT1 for empty (NIL) and nonempty (UNIT) unary heads','not_implemented':'END/QUERY active pairs, reusable threshold readout, garbage handling, full net reduction/confluence'}
out=Path(__file__).resolve().parents[1]/'results/linear-unary-insertion-ports.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
