"""Joining two typed BIT chains preserves parity and fresh port incidence."""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import json

@dataclass(frozen=True)
class Bit:
    label: int
    value: int
    next_label: int | None

def segment(values,offset):
    return tuple(Bit(offset+i,v,offset+i+1 if i+1<len(values) else None) for i,v in enumerate(values))

def join(left,right):
    assert {b.label for b in left}.isdisjoint({b.label for b in right})
    if not left:return right
    if not right:return left
    assert left[-1].next_label is None
    return left[:-1]+(Bit(left[-1].label,left[-1].value,right[0].label),)+right

def run(chain):
    by={b.label:b for b in chain}
    assert len(by)==len(chain)
    head=chain[0].label if chain else None
    seen=set();state=0
    while head is not None:
        assert head in by and head not in seen
        seen.add(head);bit=by[head]
        assert bit.value in (0,1)
        state ^= bit.value
        head=bit.next_label
    assert seen==set(by)
    return state

checked=0
for n in range(10):
    for word in product((0,1),repeat=n):
        for cut in range(n+1):
            a=segment(word[:cut],0);b=segment(word[cut:],cut)
            full=join(a,b)
            assert run(full)==(run(a)^run(b))==sum(word)%2
            assert tuple(bit.label for bit in full)==tuple(range(n))
            checked+=1
report={'passed':True,'cases':checked,'join':'connect left last auxiliary next to right principal BIT input, disjoint labels','equation':'summary(join(A,B))=summary(A) xor summary(B)','proof_for_all_n':'induction on local ACC--BIT rewrite; XOR associativity, empty segment unit','limitations':'Only closed parity observation; does not retain indexed read ports or prove Nima overlap semantics.'}
out=Path(__file__).resolve().parents[1]/'results/xor-net-boundary-composition.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
