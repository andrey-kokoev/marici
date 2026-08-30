"""Exact capability fiber over a fixed binary effect algebra."""
import json
from pathlib import Path
import sympy as sp

I=sp.I
c,s=sp.Rational(3,5),sp.Rational(4,5)
ket0=sp.Matrix([1,0]); ket1=sp.Matrix([0,1])
dag=lambda a:a.conjugate().T
outer=lambda a,b:a*dag(b)
E0=sp.diag(1,c*c)
E1=s*s*outer(ket1,ket1)
K0=sp.diag(1,c)

states={
 "absorptive_z_minus":ket0,
 "qnd_z_plus":ket1,
 "x_plus":sp.Matrix([1,1])/sp.sqrt(2),
 "y_plus":sp.Matrix([1,I])/sp.sqrt(2),
}
# Analyzer projectors: second click after a known unitary is equivalent to
# testing one of these three rank-one directions.
projectors={
 "Z":outer(ket1,ket1),
 "X":outer(sp.Matrix([1,-1])/sp.sqrt(2),sp.Matrix([1,-1])/sp.sqrt(2)),
 "Y":outer(sp.Matrix([1,-I])/sp.sqrt(2),sp.Matrix([1,-I])/sp.sqrt(2)),
}

records={}
kraus={}
for name,psi in states.items():
    K1=-I*s*outer(psi,ket1)
    kraus[name]=K1
    assert sp.simplify(dag(K1)*K1-E1)==sp.zeros(2)
    P=outer(psi,psi)
    signatures={axis:str(sp.simplify(s*s*sp.trace(P*proj)))
                for axis,proj in projectors.items()}
    records[name]={
      "successor_projector":[[str(sp.simplify(x)) for x in P.row(i)] for i in range(2)],
      "sequential_click_signatures":signatures,
      "unanalysed_repeat_probability":signatures["Z"],
    }

assert len({tuple(v["sequential_click_signatures"].values()) for v in records.values()})==len(states)
assert records["absorptive_z_minus"]["unanalysed_repeat_probability"]=="0"
assert records["qnd_z_plus"]["unanalysed_repeat_probability"]=="16/25"

# Rational continuum of click successors.
t=sp.symbols("t", real=True)
psi_t=sp.Matrix([(1-t*t)/(1+t*t),2*t/(1+t*t)])
assert sp.simplify((dag(psi_t)*psi_t)[0]-1)==0
Kt=-I*s*outer(psi_t,ket1)
assert sp.simplify(dag(Kt)*Kt-E1)==sp.zeros(2)
repeat_t=sp.factor(s*s*psi_t[1]**2)

result={
 "schema":"marici.instrument-capability-fiber.v1",
 "fixed_effects":{
  "no_click":[[str(x) for x in E0.row(i)] for i in range(2)],
  "click":[[str(x) for x in E1.row(i)] for i in range(2)],
 },
 "factorization":"K_x = U_x sqrt(E_x); partial-isometry data are invisible to one-use probabilities",
 "fixed_no_click_kraus":[[str(x) for x in K0.row(i)] for i in range(2)],
 "sample_capabilities":records,
 "rational_family":{
  "psi_t":["(1-t^2)/(1+t^2)","2t/(1+t^2)"],
  "repeat_probability":str(repeat_t),
 },
 "checks":{
  "all_click_effects_identical":True,
  "sample_sequential_signatures_distinct":True,
  "rational_family_normalized":True,
  "rational_family_effect_fixed":True,
 },
 "verdict":(
  "A fixed binary effect algebra supports a continuous projective capability "
  "fiber. Single-use records forget the fiber coordinate; controlled "
  "sequential analyzers recover it operationally."
 )
}
out=Path(__file__).parents[1]/"results"/"instrument_capability_fiber.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
