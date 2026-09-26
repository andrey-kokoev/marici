"""Explicit principal/auxiliary-port chain for a local XOR net rewrite.

ACC has principal output and an auxiliary boundary port; BIT has principal
input and auxiliary next. An active pair is ACC.out -- BIT.in; rewrite replaces
both agents with ACC(p xor b), reconnecting its out to BIT.next.
This is a typed port-graph fragment, not a full interaction-net formalization.
"""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import json

@dataclass(frozen=True)
class Bit:
    label: int
    value: int
    next_label: int | None

@dataclass(frozen=True)
class State:
    acc: int
    head: int | None
    bits: tuple[Bit,...]
    consumed: tuple[int,...]=()

def check(s):
    labels={b.label for b in s.bits}
    assert len(labels)==len(s.bits) and s.acc in (0,1)
    assert s.head is None or s.head in labels
    assert all(b.value in (0,1) and (b.next_label is None or b.next_label in labels) for b in s.bits)
    seen=set();head=s.head;by_label={b.label:b for b in s.bits}
    while head is not None:
        assert head not in seen
        seen.add(head);head=by_label[head].next_label
    assert seen==labels

def step(s):
    check(s)
    if s.head is None:return s
    bit=next(b for b in s.bits if b.label==s.head)
    out=State(s.acc ^ bit.value,bit.next_label,tuple(b for b in s.bits if b.label!=bit.label),s.consumed+(bit.label,))
    check(out)
    return out

def make(word):
    s=State(0,0 if word else None,tuple(Bit(i,v,i+1 if i+1<len(word) else None) for i,v in enumerate(word)))
    check(s);return s

def run(word):
    s=make(word)
    while s.head is not None:s=step(s)
    assert s.consumed==tuple(range(len(word))) and not s.bits
    return s.acc

for n in range(9):
    for word in product((0,1),repeat=n):
        assert run(word)==sum(word)%2
report={'passed':True,'port_rule':'ACC.out--BIT.in active pair rewrites to ACC(xor), connects out to BIT.next','graph_invariant':'unique typed labels, acyclic connected chain, no dangling internal next','exhaustive':'all bit words length 0..8','boundary':'closed chain exposes only final parity; indexed bit reads require extra retained ports','limits':'Not a generic interaction-net implementation; overlapping redexes and Nima E/E_B operations unmodelled.'}
out=Path(__file__).resolve().parents[1]/'results/port-chain-xor-net.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
