from retained_union import UnionSet
from itertools import product
from check_port_multigraph_forest import forest
from pathlib import Path
import json

def reference(a,b):return tuple(int((i<len(a) and a[i]) or (i<len(b) and b[i])) for i in range(max(len(a),len(b))))
def merge(a,b):
 before=a.steps;n=len(a.retained());m=len(b.retained());a.union_from(b)
 assert b.retained()==()
 while a.enabled():
  assert len(a.enabled())==1 and forest(a)
  a.step(a.enabled()[0])
 assert forest(a) and a.steps-before==(2*n+1 if n<=m else 2*m+2)
 return a.retained()
words=[w for n in range(5) for w in product((0,1),repeat=n)]
cases=queries=0
for a,b in product(words,repeat=2):
 x=UnionSet(a);y=UnionSet(b)
 oldx=x.start(0);x.run();oldy=y.start(0);y.run()
 expected=reference(a,b);assert merge(x,y)==expected
 assert x.answer(oldx)==bool(a and a[0]) and y.answer(oldy)==bool(b and b[0])
 for i in range(len(expected)+2):
  out=x.start(i);x.run();assert x.answer(out)==(i<len(expected) and bool(expected[i]));assert x.retained()==expected;queries+=1
 i=len(expected)+1;x.insert(i);x.run();assert x.retained()==expected+(0,1)
 assert merge(UnionSet(b),UnionSet(a))==expected
 assert merge(UnionSet(a),UnionSet(a))==a
 cases+=1
small=[w for n in range(3) for w in product((0,1),repeat=n)]
triples=0
for a,b,c in product(small,repeat=3):
 x=UnionSet(a);merge(x,UnionSet(b));left=merge(x,UnionSet(c))
 y=UnionSet(b);merge(y,UnionSet(c));right=merge(UnionSet(a),y)
 assert left==right==reference(reference(a,b),c);triples+=1
same=UnionSet((1,))
try:same.union_from(same)
except AssertionError:pass
else:raise AssertionError('alias accepted')
report={'passed':True,'word_pairs':cases,'membership_queries_after_union':queries,'associativity_triples':triples,'checks':['empty donor','old answers unchanged','union word','commutativity','idempotence','associativity','subsequent insertion','forest each union step','exact union count','self-alias rejected'],'steps':'2*n+1 if n<=m else 2*m+2','scope':'Destructive donor move via host interface; nine fixed local union rules. No concurrent or internally sequenced calls.'}
out=Path(__file__).resolve().parents[1]/'results/retained-union.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
