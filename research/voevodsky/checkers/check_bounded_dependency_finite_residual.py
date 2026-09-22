"""Source-derived finite dependency bound before residual minimization.

The proof uses finite field domains and syntactically inspectable rules.
Exhaustive abstract-domain closure certifies an inductive finite carrier;
reachable behavior is then computed separately and minimized.
"""
from pathlib import Path
from itertools import product
from collections import deque
import importlib.util
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/causal-interface-construction-contract.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
c = json.loads(p.read_text())
fields, rules, labels = c['fields'], c['rules'], c['labels']
# These are source syntax domains, frozen before graph exploration.
domains = {'end': list(range(64)), 'origin': [0,1], 'pending': [None,0,1],
           'received': [None,0,1], 'issued': [None,0,1]}
assert set(fields) == set(domains)
cp = OUT / 'bounded-dependency-finite-residual-contract.json'
save(cp, {'owning_rule_contract_sha256': sha(p),
 'domain_justification': 'end is a six-event subset mask; origin is a binary initialization; record and issued values are absent or binary.',
 'domains': domains, 'maximum_dependency_fields':5,
 'derivation': 'Outputs and guards seed dependency closure; retained update reads recursively enlarge it. Validate all references against the declared finite domains.',
 'prediction': 'The finite domain carrier is inductive under every declared rule and bounds the complete residual observer. Reachability and minimization preserve outputs and admission.',
 'scope': 'Actual inspectable five-field rule language and fixed labels, with atomic source-bound snapshots. No hidden callbacks, unbounded storage, or unknown future operations.'})
subprocess.run([sys.executable, str(N / 'checkers/verify_causal_observer_interface.py')], check=True, capture_output=True, text=True)
spec = importlib.util.spec_from_file_location('expr', N / 'checkers/construct_causal_observer_interface.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def dependencies(rs):
 live = set().union(*(m.reads(x) for x in c['outputs']))
 for rule in rs.values(): live |= m.reads(rule['guard'])
 while True:
  old = set(live)
  for rule in rs.values():
   for target, expr in rule['updates'].items():
    if target not in domains: raise ValueError('undeclared update target')
    if target in live: live |= m.reads(expr)
  if not live <= set(domains): raise ValueError('undeclared dependency')
  if old == live: return live
live = dependencies(rules)
assert len(live) == 5
# Every rule expression is inspectable, with no dynamically introduced variable.
for rule in rules.values():
 assert m.reads(rule['guard']) <= live
 assert set().union(*(m.reads(x) for x in rule['updates'].values())) <= live

def step(state, label):
 env = dict(zip(fields,state)); name,*args=label; rule=rules[name]
 if not m.evaluate(rule['guard'],env,args): return False,state
 new = dict(env)
 for target,expr in rule['updates'].items(): new[target] = m.evaluate(expr,env,args)
 return True,tuple(new[f] for f in fields)
def output(state):
 env=dict(zip(fields,state))
 return tuple(m.evaluate(x,env,[]) for x in c['outputs'])
carrier = list(product(*(domains[f] for f in fields)))
carrier_set = set(carrier)
assert len(carrier)==3456
induction_checks=0
for state in carrier:
 for label in labels:
  ok,nxt=step(state,label)
  assert nxt in carrier_set
  if not ok: assert nxt==state
  induction_checks+=1
initial = list(map(tuple,c['initial_states']))
assert all(s in carrier_set for s in initial)
# Range narrowing from initial values is a separate sound abstraction, still
# computed on Cartesian field values rather than known reference states.
abstract = {f:{s[i] for s in initial} for i,f in enumerate(fields)}
rounds=0
while True:
 new={f:set(v) for f,v in abstract.items()}
 for state in product(*(sorted(abstract[f],key=repr) for f in fields)):
  for label in labels:
   _,nxt=step(state,label)
   for i,f in enumerate(fields): new[f].add(nxt[i])
 rounds+=1
 if new==abstract: break
 abstract=new
narrowed_bound=1
for values in abstract.values(): narrowed_bound*=len(values)
seen=set(initial); todo=deque(initial); graph={}
while todo:
 state=todo.popleft(); row=[]
 for label in labels:
  ok,nxt=step(state,label); row.append((ok,nxt))
  if nxt not in seen: seen.add(nxt);todo.append(nxt)
 graph[state]=row
states=sorted(seen,key=repr); ids={s:i for i,s in enumerate(states)}
table=[[(ok,ids[t]) for ok,t in graph[s]] for s in states]
outputs=[output(s) for s in states]
spec=importlib.util.spec_from_file_location('minimize',N/'checkers/check_compressed_observer_live_lift.py')
mi=importlib.util.module_from_spec(spec);spec.loader.exec_module(mi)
_,q,_=mi.partition(outputs,table)
_,current,_=mi.partition(outputs,[row[:16] for row in table])
assert len(q)<=len(states)<=narrowed_bound<=len(carrier)
# Deliberately undeclared historical read must fail before exploring states.
import copy
bad=copy.deepcopy(rules)
bad['audit-hidden']={'guard':{'var':'unbounded_past_counter'},'updates':{}}
try: dependencies(bad)
except ValueError: pass
else: raise AssertionError('unmodeled history dependency passed admission')
assert sha(p)==json.loads(cp.read_text())['owning_rule_contract_sha256']
report={'passed':True,'contract_sha256':sha(cp),
 'derived_dependencies':sorted(live),'syntactic_cartesian_bound':len(carrier),
 'inductive_domain_transition_checks':induction_checks,
 'abstract_range_rounds':rounds,
 'derived_ranges':{f:sorted(v,key=repr) for f,v in abstract.items()},
 'narrowed_cartesian_bound':narrowed_bound,
 'source_reachable_states':len(states), 'full_language_minimal_states':len(q),
 'current_language_minimal_states':len(current),
 'undeclared_history_dependency_rejected':True,
 'theorem':'A finite inductive carrier of dependency values, sufficient to evaluate all guards, retained updates and outputs, gives a finite residual observer. Its size is at most the product of domain cardinalities; composition follows by induction on words.',
 'qualification':'This proves the conditional finite-representability statement and checks its premises on the actual rules. It does not infer a finite dependency carrier from finite program text alone.',
 'scope':'Finite-state bound, not a dimension bound for real-valued analytical interfaces or a claim about arbitrary future extensions.'}
save(OUT/'bounded-dependency-finite-residual.json',report)
print(json.dumps(report,indent=2))
