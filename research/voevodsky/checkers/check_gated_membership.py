from gated_membership import GatedMembership
from itertools import product
from random import Random
from pathlib import Path
import json
rng=Random(81);runs=checks=0
for n in range(4):
 for word in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   for reverse in (False,True):
    net=GatedMembership(word,i,j)
    while net.enabled():
     choices=net.enabled()
     for g in choices:
      if net.kind(g)=='GATE':
       assert not any(net.kind(x) in ('COPY','QB','QS','QR','EA') for x in net.types)
       assert net.answer(net.first_out)==(i<n and bool(word[i]))
     if net.gate_firings==0:
      assert net.kind(net.wires[net.second_out+'.p'].split('.')[0])=='GATE'
     net.step(rng.choice(choices) if reverse else choices[0]);checks+=1
    assert net.gate_firings==1 and net.acknowledged() and net.retained()==word
    assert net.answer(net.first_out)==(i<n and bool(word[i]))
    assert net.answer(net.second_out)==(j<n and bool(word[j]))
    assert net.steps==4*n+i+j+7
    runs+=1
report={'passed':True,'runs':runs,'rewrite_checks':checks,'seed':81,'scope':'Two calls, local GATE--DONE only; first-call cleanup checked at gate eligibility. Cyclic acknowledgment wiring, not covered by forest canonicalization.'}
out=Path(__file__).resolve().parents[1]/'results/gated-membership.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
