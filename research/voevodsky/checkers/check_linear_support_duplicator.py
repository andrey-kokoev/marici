"""Finite-signature linear local copier boundary rules for B0/B1/NIL chains.

COPY.p--Bv.p, COPY.a/b--LEFT/RIGHT, Bv.a--TAIL
  -> BvL.p--LEFT, BvR.p--RIGHT,
     BvL.a--COPY2.a, BvR.a--COPY2.b, COPY2.p--TAIL.
COPY.p--NIL.p -> NILL.p--LEFT, NILR.p--RIGHT.
This validates boundary rules and an abstract structural induction, not a
single executable wired multi-step graph.
"""
from itertools import product
from pathlib import Path
import json

def edge(a,b):return frozenset((a,b))
def ports_once(edges):
 ports=[p for e in edges for p in e]
 assert len(ports)==len(set(ports)) and all(len(e)==2 for e in edges)

def rule(bit):
 assert bit in (0,1)
 old={edge('COPY.p','B.p'),edge('COPY.a','LEFT.p'),edge('COPY.b','RIGHT.p'),edge('B.a','TAIL.p')}
 new={edge('BL.p','LEFT.p'),edge('BR.p','RIGHT.p'),edge('BL.a','COPY2.a'),edge('BR.a','COPY2.b'),edge('COPY2.p','TAIL.p')}
 ports_once(old);ports_once(new)
 assert {p for e in old for p in e if p in ('LEFT.p','RIGHT.p','TAIL.p')}=={p for e in new for p in e if p in ('LEFT.p','RIGHT.p','TAIL.p')}
 return True

def nil_rule():
 old={edge('COPY.p','N.p'),edge('COPY.a','LEFT.p'),edge('COPY.b','RIGHT.p')}
 new={edge('NL.p','LEFT.p'),edge('NR.p','RIGHT.p')}
 ports_once(old);ports_once(new)
 return True
assert rule(0) and rule(1) and nil_rule()

def duplicate(word):
 # Unwind local head rule once per bit; nil rule terminates both branches.
 if not word:return (),(),1
 l,r,steps=duplicate(word[1:])
 return (word[0],)+l,(word[0],)+r,steps+1
cases=0
for n in range(11):
 for word in product((0,1),repeat=n):
  l,r,steps=duplicate(word)
  assert l==r==word and steps==n+1
  cases+=1
report={'passed':True,'cases':cases,'finite_rules':'COPY--B0, COPY--B1, COPY--NIL; one fresh COPY per bit','port_invariant':'all old/new boundary ports linear and LEFT/RIGHT/TAIL each used once','structural_result':'two distinct equal bit strings after n+1 abstract local steps','limits':'Not an instantiated multi-step port graph; output wire orientation, garbage and concurrent query scheduling still need execution.'}
out=Path(__file__).resolve().parents[1]/'results/linear-support-duplicator.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
