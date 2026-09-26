from strict_query_chain import StrictQueryChain
from itertools import product
from random import Random
from pathlib import Path
import json
rng=Random(84);runs=steps=releases=0
for n in range(3):
 for word in product((0,1),repeat=n):
  for count in range(5):
   for indices in product((0,1,3),repeat=count):
    net=StrictQueryChain(word,indices)
    while net.enabled():
     choices=net.enabled()
     for g in choices:
      if net.kind(g)=='GATE':
       assert g==net.gates[net.gate_firings]
       assert not any(net.kind(x) in ('COPY','QB','QS','QR','EA') for x in net.types)
       for o,i in zip(net.outputs[:net.gate_firings+1],indices):assert net.answer(o)==(i<n and bool(word[i]))
     assert not net.acknowledged()
     a=rng.choice(choices);releases+=net.kind(a)=='GATE';net.step(a)
    assert net.acknowledged() and net.retained()==word
    assert tuple(net.answer(o) for o in net.outputs)==tuple(i<n and bool(word[i]) for i in indices)
    assert net.gate_firings==max(0,count-1)
    assert net.steps==sum(2*n+i+3 for i in indices)+max(0,count-1)
    runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'ordered_gate_releases':releases,'seed':84,'scope':'Finite sequences up to four queries, words n<=2 and indices0,1,3; random individual reductions, not exhaustive schedules. Empty and single-call cases included.'}
out=Path(__file__).resolve().parents[1]/'results/strict-query-chain.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
