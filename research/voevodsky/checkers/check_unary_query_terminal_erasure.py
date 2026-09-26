"""Linear terminal and garbage rules for a destructive unary threshold skeleton.

Q.p--NIL.p has Q.a--other-head and Q.r--OUT: replace with
BOOL.p--OUT and ERASE.p--other-head. ERASE.p--UNIT.p reconnects
ERASE2.p to UNIT.a tail; ERASE.p--NIL.p disappears.
These are boundary templates plus a small-step abstract evaluator, not a
complete executable interaction-net graph engine.
"""
from pathlib import Path
import json

def wire(a,b):return frozenset((a,b))
def linear(ws):
    ports=[p for w in ws for p in w]
    assert all(len(w)==2 for w in ws) and len(ports)==len(set(ports))

before={wire('Q.p','N.p'),wire('Q.a','HEAD.p'),wire('Q.r','OUT.p')}
after={wire('BOOL.p','OUT.p'),wire('ERASE.p','HEAD.p')}
linear(before);linear(after)
assert {p for w in before for p in w if p in ('HEAD.p','OUT.p')}=={p for w in after for p in w if p in ('HEAD.p','OUT.p')}
linear({wire('ERASE.p','UNIT.p'),wire('UNIT.a','TAIL.p')})
linear({wire('ERASE2.p','TAIL.p')})
linear({wire('ERASE.p','NIL.p')})

def evaluate(count,k):
    assert count>=0 and k>=0
    c,b=count,k;interior=0
    while c and b:
        c-=1;b-=1;interior+=2
    answer=(b==0) # At simultaneous exhaustion, budget-NIL wins.
    erasures=c+b+1 # remaining UNIT/KUNIT nodes plus final NIL
    assert erasures>=1
    return answer,interior,erasures

cases=0
for c in range(65):
    for k in range(65):
        result,steps,garbage=evaluate(c,k)
        assert result==(c>=k) and steps==2*min(c,k)
        assert garbage==abs(c-k)+1
        cases+=1
report={'passed':True,'cases':cases,'terminal_rule':'Q--NIL -> BOOL at OUT plus ERASE at unconsumed opposite head','eraser_rules':'ERASE--UNIT -> ERASE at tail; ERASE--NIL -> empty','abstract_result':'one Boolean, 2min(c,k) interior phases, abs(c-k)+1 erasures','priority':'if both heads NIL, budget exhaustion means true','limitations':'Templates do not instantiate a globally wired graph; agent types and phase transitions at NIL not fully executable; no reusable state or confluence theorem.'}
out=Path(__file__).resolve().parents[1]/'results/unary-query-terminal-erasure.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
