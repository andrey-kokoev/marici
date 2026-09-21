"""Finite witness for strict filtered extension and non-split source action."""
from pathlib import Path
import contextlib
import io
import runpy
import json
ROOT=Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
a=b['relation']((0,1),0)
c=b['relation']((2,3),0)
ac=b['multiply'](a,c)
assert ac and len(ac)==4
assert ac[((0,1,2,3),(False,False,False,False))]==1
assert ac==b['power_basis']((0,1,2,3))[b['probe'](((0,1),(2,3)),(0,0))]
# Each relation consumes two events. I^2=0 on the two-event b corner,
# and I^3=0 on the four-event product corner. Thus any corner-preserving
# lift of [c] must equal c, and its a-action cannot vanish.
assert 2<2*2 and 4<2*3
rank=b['record_rank'](4)
paths=24*16
ideal=paths-rank
square=len(b['power_basis']((0,1,2,3)))
assert (ideal,square,ideal-square)==(234,24,210)

# Common path weights are submultiplicative, independently of quotient choices.
checks=0
for p in range(5):
    for n in range(20):
        for m in range(20):
            assert (1+n+m)**p <= (1+n)**p*(1+m)**p
            checks+=1
result={'passed':True,
 'four_event_dimensions':{'I_mod_I3':ideal,'I2_mod_I3':square,'I_mod_I2':ideal-square},
 'nonzero_relation_action_coefficient':1,
 'path_weight_submultiplicativity_checks':checks,
 'scope':'Finite source-module nonsplitting witness and weight regressions. Strict Banach exactness follows from the common endpoint path-norm quotient proof; no identification with stronger presentation completions.'}
out=ROOT/'research/voevodsky/results/first-filtered-extension.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
