"""Exact WP625 audit of the symmetric clock second moment."""
import itertools, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
A = (-2, -1, 0, 1, 2)
states = list(itertools.product(A, repeat=5))
target = [x for x in states if sum(x) == 6]
orbits = sorted({tuple(v.count(a) for a in A) for v in target})
def rep(o): return tuple(a for a,n in zip(A,o) for _ in range(n))
records = [(o, sum(x*x for x in rep(o))) for o in orbits]
a=(-2,2,2,2,2); b=(1,1,1,1,2)
qmin=min(sum(x*x for x in s) for s in states)
mins=[s for s in states if sum(x*x for x in s)==qmin]
checks={
"target_has_five_orbits":len(orbits)==5,
"second_moments_are_exact":sorted(q for _,q in records)==[8,10,12,14,20],
"S_Q_is_faithful":len({(6,q) for _,q in records})==5,
"hostile_pair_is_separated":sum(x*x for x in a)==20 and sum(x*x for x in b)==8,
"positive_Q_rigidifies_conditionally":min(q for _,q in records)==8,
"balanced_orbit_is_unique":sum(q==8 for _,q in records)==1,
"unconstrained_Q_minimum_is_zero":qmin==0,
"unconstrained_minimum_has_sum_zero":{sum(x) for x in mins}=={0},
"Q_does_not_select_target_sum":all(sum(x)!=6 for x in mins),
"negative_Q_selects_boundary":max(sum(x*x for x in s) for s in states)==20}
if not all(checks.values()): raise SystemExit(checks)
result={"work_package":"WP625","status":"PASS","checks":checks,
"admitted_state_domain":"five-clock alphabet quotient by S5",
"probe_family":["S=sum x_i","Q=sum x_i^2"],
"contextual_partition_at_S_6":[{"occupancy":list(o),"Q":q} for o,q in records],
"classification":"Q separates and conditionally rigidifies occupation but does not select S=6",
"smallest_exact_falsifier":"equal-mean hostile pair has Q=20 versus Q=8",
"selector_failure":"unconstrained positive Q selects all-zero state with S=0",
"physical_probe":"measure total clock power with mean and flavor record",
"instrument_gate":"second-moment channel needs same-lineage calibration"}
(ROOT/"results"/"wp625_clock_second_moment_rigidifier.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
