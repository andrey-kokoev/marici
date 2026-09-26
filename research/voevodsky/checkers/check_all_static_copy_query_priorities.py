"""Check every static priority ordering of four rewrite families on tiny nets."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product,permutations
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin
orders=tuple(permutations(range(4)))
cases=0;signatures=set();max_steps=0
for n in range(4):
 for bits in product((0,1),repeat=n):
  for i in range(n+2):
   for j in range(n+2):
    expected=(i<n and bool(bits[i]),j<n and bool(bits[j]))
    outputs=set()
    for order in orders:
     net=ScheduledTwin(bits,i,j)
     answer,history=net.run_order(order)
     outputs.add(answer)
     assert len(net.types)==4 and answer==expected
     max_steps=max(max_steps,len(history));signatures.add(tuple(history));cases+=1
    assert outputs=={expected}
report={'passed':True,'static_priority_orders':len(orders),'cases':cases,'distinct_family_histories':len(signatures),'max_steps':max_steps,'finding':'all 24 static priority orders terminate with same two Boolean outputs for supports n<=3','limit':'Not all dynamically changing redex schedules; no general confluence or local-add theorem.'}
out=Path(__file__).resolve().parents[1]/'results/all-static-copy-query-priorities.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
