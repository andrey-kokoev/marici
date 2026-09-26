"""Both orders of every enabled individual redex pair on exact tiny forests."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product,combinations
from pathlib import Path
import json
from forest_canonical import canonical
from typed_net_invariant import validate
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay
 from check_admitted_mutation_closure import step

def agents(net):
 return [n for n in net.types if n.startswith(('COPY','Q1','Q2','E_')) and net.wires[n+'.p'].endswith('.p')]
def family(n):return 'COPY' if n.startswith('COPY') else ('E' if n.startswith('E_') else n[:2])
states=diamonds=0;by_pair={}
for n in range(3):
 for bits in product((0,1),repeat=n):
  for indices in product(range(n+3),repeat=2):
   pending=[()];seen=set()
   while pending:
    prefix=pending.pop();net,choices=replay(bits,indices,prefix)
    assert validate(net) is None
    key=canonical(net,True)
    if key in seen:continue
    seen.add(key)
    for a,b in combinations(agents(net),2):
     pair_a={a,net.wires[a+'.p'].split('.')[0]}
     pair_b={b,net.wires[b+'.p'].split('.')[0]}
     assert pair_a.isdisjoint(pair_b)
     left=step(net,a);right=step(net,b)
     assert b in agents(left) and a in agents(right)
     assert validate(left) is None and validate(right) is None
     left=step(left,b);right=step(right,a)
     assert validate(left) is None and validate(right) is None
     assert canonical(left,True)==canonical(right,True),(bits,indices,prefix,a,b)
     pair='/'.join(sorted((family(a),family(b))))
     by_pair[pair]=by_pair.get(pair,0)+1;diamonds+=1
    pending.extend(prefix+(c,) for c in choices)
   states+=len(seen)
assert by_pair.get('E/E',0)>0
report={'passed':True,'exact_states':states,'individual_redex_diamonds':diamonds,'family_pairs':by_pair,'scope':'All enabled pairs in extended n<=2 inputs; two-step equality modulo tagged forest isomorphism, not universal confluence proof.'}
out=Path(__file__).resolve().parents[1]/'results/exact-individual-diamonds.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
