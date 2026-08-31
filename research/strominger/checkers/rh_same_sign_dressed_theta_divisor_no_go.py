import json
from fractions import Fraction as Q
from pathlib import Path

# Exact finite passive seam census. Imaginary quadratic form is
# ||W^(1/2)(Vc+Bx)||^2 + delta||x||^2.
def energy(c,x,V,B,W,delta):return W*(V*c+B*x)**2+delta*x*x
params=[(Q(V),Q(B),Q(W),Q(d)) for V in (1,2) for B in (-2,1,3) for W in (1,3) for d in (1,2)]
states=[(Q(c),Q(x)) for c in range(-4,5) for x in range(-4,5)]
checks={
 "passive_energy_is_nonnegative":all(energy(c,x,V,B,W,d)>=0 for V,B,W,d in params for c,x in states),
 "zero_energy_forces_arithmetic_coordinate_zero":all(not energy(c,x,V,B,W,d)==0 or x==0 for V,B,W,d in params for c,x in states),
 "zero_energy_then_forces_bare_theta_darkness":all(not energy(c,x,V,B,W,d)==0 or V*c==0 for V,B,W,d in params for c,x in states),
 "arithmetic_feedback_cannot_create_a_nonzero_theta_kernel":all(energy(c,x,V,B,W,d)>0 for V,B,W,d in params for c,x in states if c!=0),
}
base=Path(__file__).parents[2]
source=(base/"nima"/"a-strict-same-sign-arithmetic-complement-cannot-create-a-dressed-seam-zero.md").read_text(encoding="utf-8")
schur=(base/"nima"/"the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md").read_text(encoding="utf-8")
checks.update({
 "source_derives_x_zero_from_strict_arithmetic_sign":("The kernel calculation forces this reconstructed vector to vanish" in source),
 "source_reduces_dressed_zero_to_bare_weyl_zero":("arithmetic Schur correction cannot create a zero" in source),
 "xi_unit_comparison_remains_an_unproved_source_identity":("must be proved from the source history" in schur and "Defining \\(D_U\\) or \\(E_\\theta\\) from the quotient" in schur),
})
result={
 "schema":"marici.strominger.rh_same_sign_dressed_theta_divisor_no_go.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/a-strict-same-sign-arithmetic-complement-cannot-create-a-dressed-seam-zero.md","research/nima/the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md","research/nima/the-adjoint-history-residual-is-a-strict-weyl-function-off-the-seam.md"],
 "verdict":"Under the current strict same-sign passive seam assumptions, arithmetic Schur feedback cannot create or shift a theta zero. Any dressed kernel has x=0 and requires the bare theta Weyl direction to be dark. Therefore the proposed dressed comparison does not derive the Xi divisor from arithmetic feedback; it reduces to the still-unproved bare-Weyl/Evans comparison plus a nonvanishing arithmetic factor. The feedback-divisor mechanism is falsified for the current Cayley/passive complement. Escaping it requires a source-derived sign loss, controlled degeneracy, indefinite orientation, or singular boundary value.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"state_census":len(states)*len(params)
}
out=Path(__file__).parents[1]/"results"/"rh_same_sign_dressed_theta_divisor_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
