"""Derivation independence does not imply effect-observation independence."""
from pathlib import Path
import json
row_deps={'Z':(), 'W':('Z',),'V':('Z',),'U':('Z',),'T':('W','V','U')}
effects={'W':{'read':set(),'write':{'slot'}},'V':{'read':{'slot'},'write':set()},'U':{'read':{'other'},'write':set()}}
def conflict(a,b):
 ea=effects.get(a,{'read':set(),'write':set()});eb=effects.get(b,{'read':set(),'write':set()})
 return bool(ea['write'] & (eb['read']|eb['write']) or eb['write'] & (ea['read']|ea['write']))
def allowed(a,b):
 if a in row_deps[b] or b in row_deps[a]:raise ValueError('ROW_DEPENDENCY')
 if conflict(a,b):raise ValueError('EFFECT_CONFLICT')
 return True
def run(seq):
 slot=0;seen=[]
 for event in seq:
  if event=='W':slot=1
  if event=='V':seen.append(slot)
 return tuple(seen)
assert run(('Z','W','V','U','T'))==(1,)
assert run(('Z','V','W','U','T'))==(0,)
assert set(row_deps['W'])==set(row_deps['V'])=={'Z'}
try:allowed('W','V')
except ValueError as err:assert str(err)=='EFFECT_CONFLICT'
else:raise AssertionError('unsafe swap admitted')
assert allowed('W','U') and allowed('V','U')
try:allowed('Z','W')
except ValueError as err:assert str(err)=='ROW_DEPENDENCY'
else:raise AssertionError('dependency swap admitted')
report={'passed':True,'row_only_independence_W_V':True,'effect_conflict_W_writes_V_reads':'slot','observations_W_then_V':[1],'observations_V_then_W':[0],'typed_effect_conflict_refuses_swap':True,'disjoint_U_swaps_allowed':True,'scope':'Synthetic stateful trace overlay on otherwise equal mathematical square row derivations. Effect labels require evidence; no claim of actual external effects, source issuer grant or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/effect-sensitive-trace-swap.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
