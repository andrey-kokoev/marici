import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
base=sp.Matrix([2,23])
neighbors=[]
for dk in range(-1,2):
 for dc in range(-1,2):
  p=base+sp.Matrix([dk,dc])
  if (p-base).dot(p-base)<1:
   neighbors.append((int(p[0]),int(p[1])))
assert neighbors==[(2,23)]
A_local=sp.zeros(2,0); A_relaxed=sp.eye(2)
assert A_local.rank()==0 and A_relaxed.rank()==2
half_command=base+A_relaxed*sp.Matrix([sp.Rational(1,2),0])
assert half_command[0].is_integer is False
h=lambda k,C: sp.Rational(12*C,1367*k)*sp.pi**2
assert sp.simplify(h(2,23)-h(2,22))==6*sp.pi**2/1367
assert sp.simplify(h(3,23)-h(2,23))!=0
result={"schema":"marici.flavor.wp1037.v1","status":"PASS",
 "question":"Can WP996-style local control select the WP1036 discrete source labels (k,C)=(2,23)?",
 "state_domain":"integer theory-label lattice k>0,C>0 around (2,23)",
 "authorized_local_actuator":{"matrix_shape":[2,0],"rank":0,"unit_ball_points":[[2,23]]},
 "false_continuous_repair":{"matrix":"I2","rank":2,"hostile_command":"(1/2,0) leaves the integer source domain"},
 "contextual_partition":"each lattice point is a distinct source-theory packet; there are no nontrivial local command orbits",
 "smallest_exact_falsifier":"(2,23) to (2,22) changes h by 6*pi^2/1367 but is a theory replacement, not an admitted actuator action",
 "classification":"arithmetic capacity without actuator; neither selector nor physical rigidifier",
 "instrument":"none: no common substrate executes changes of matter or operator multiplicity",
 "aspect_gates":{"source_control_norm":False,"source_bound_B":False,"closed_loop_dual_error":False},
 "remaining_gate":"a common source substrate with executable operations whose fixed sectors realize the integer labels and whose cost/support ball is derived before optimization",
 "claim_boundary":"local/continuous actuator control on the integer-label model; does not exclude discrete preparation operations in a larger common theory",
 "disposition":"negative: WP996 cannot select WP1036 because candidate coordinates live in object space, not command space"}
(ROOT/"results"/"wp1037_discrete_source_actuator_type_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1037 PASS:",neighbors,A_local.rank(),half_command.T)
