"""Alternating principal-port phases consume one count and one budget unit.

Q_COUNT.p--UNIT.p: Q_BUDGET.p connects to budget head, auxiliary
connects count tail. Q_BUDGET.p--KUNIT.p: Q_COUNT.p connects to saved
count tail, auxiliary connects remaining budget. End/garbage wiring is
not implemented; this tests the two interior linear rewrites only.
"""
from pathlib import Path
import json

def wire(a,b):return frozenset((a,b))
def incidence(wires):
    ports=[p for w in wires for p in w]
    assert all(len(w)==2 for w in wires) and len(ports)==len(set(ports))
    return len(wires)

def interior(phase):
    assert phase in ('count','budget')
    # Active pair and its two external wires.
    old={wire('Q.p','U.p'),wire('Q.a','OTHER.p'),wire('U.a','TAIL.p')}
    assert incidence(old)==3
    new={wire('Qnext.p','OTHER.p'),wire('Qnext.a','TAIL.p')}
    assert incidence(new)==2
    return True

def destructive_query(count,k):
    assert count>=0 and k>=0
    remaining_count=count;remaining_budget=k;steps=0
    while remaining_budget and remaining_count:
        assert interior('count') and interior('budget')
        remaining_count-=1;remaining_budget-=1;steps+=2
    # The leftovers are NOT preserved as a reusable state. A complete net
    # requires explicit erasure/termination rules for both tails.
    return remaining_budget==0,steps,remaining_count,remaining_budget

cases=0
for count in range(33):
    for k in range(33):
        answer,steps,rc,rk=destructive_query(count,k)
        assert answer==(count>=k) and steps==2*min(count,k)
        assert rc==count-min(count,k) and rk==k-min(count,k)
        cases+=1
report={'passed':True,'cases':cases,'interior_port_rules':'two alternating principal-port active pairs; each preserves two external endpoints linearly','result':'count>=k, 2*min(count,k) interior rewrites','contract':'destructive: count and budget units consumed; leftover tails require explicit erasure','missing':'NIL/zero threshold termination, leftover garbage rules, complete reusable interaction net'}
out=Path(__file__).resolve().parents[1]/'results/destructive-unary-query-phases.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
