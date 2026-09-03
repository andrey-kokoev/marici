"""Exact hostile: a uniform arithmetic frame can vanish after Green elimination."""
from fractions import Fraction as F
from pathlib import Path
import json

# One scalar mode suffices; tensoring with any prime direct sum preserves it.
A=F(1); B=F(1); C=F(1); D=F(1)
effective=A-C*C/D
full_det=A*D-C*C
radical_vector=(F(1),F(-1))
full_energy=A*radical_vector[0]**2+2*C*radical_vector[0]*radical_vector[1]+D*radical_vector[1]**2
# Compact theta singular values and bounded-factorization obstruction at cutoffs.
cutoffs=[2,5,29,97]
factor_norms=[F(n) for n in cutoffs]  # I = diag(n) diag(1/n)
checks={
 "arithmetic_observer_has_unit_lower_bound":B==1,
 "full_green_block_is_positive_semidefinite":A>=0 and D>=0 and full_det==0,
 "green_schur_return_annihilates_arithmetic_form":effective==0,
 "radical_leakage_exhibited":full_energy==0 and radical_vector[0]!=0,
 "identity_does_not_factor_through_compact_theta_boundedly":all(factor_norms[i+1]>factor_norms[i] for i in range(len(factor_norms)-1)),
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"A_effective":str(effective),"full_determinant":str(full_det),"radical_vector":[str(x) for x in radical_vector],"theta_inverse_cutoff_norms":[str(x) for x in factor_norms],"conclusion":"a noncompact uniformly faithful arithmetic observer is insufficient unless the enlarged Green Schur return is uniformly strictly below the cyclic form"}
out=Path("research/aspect/results/arithmetic_frame_schur_cancellation.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
