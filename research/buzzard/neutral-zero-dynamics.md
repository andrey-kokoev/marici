# Finite neutral zero dynamics

## Result

The new Lean draft separates three layers:

1. `imaginaryPart_mul_charge_eq_zero` is the scalar energy identity.
2. `finiteZeroDynamics_im_mul_kreinCharge` derives
   \(\operatorname{Im}(z)\operatorname{Re}\langle x,Kx\rangle=0\) from the
   finite matrix assumptions. `kreinCharge_im_eq_zero` supplies the separate
   fact that the charge is real when `K` is Hermitian.
3. `finiteZeroDynamics_kreinNeutral_of_offReal` combines those facts to prove
   the exact constructor statement: every off-real witness has zero complex
   Krein charge.
4. `finiteZeroDynamics_real_of_kreinCharge_ne_zero` states the pointwise
   exclusion principle: a nonneutral admissible witness can occur only on the
   real seam. This is deliberately weaker than a uniform definiteness theorem.
5. The three-state fixture realizes an invisible, neutral state at \(z=i\)
   and proves that the cleared transfer numerator is \(z^2+1\), hence vanishes
   at \(i\) and \(-i\).

## Types and assumptions

The carrier index is any finite type with decidable equality. Matrices and
vectors are complex. The boundary scale `α` is real. The finite identity uses:

- \(A^*=A\);
- \(K^*=K\);
- \((A-zI)x=-b\), encoded as `A *ᵥ x - z • x = -b`;
- \(c^*x=0\);
- \(AK=KA\);
- \(Kb=\alpha c\).

Invertibility of `K`, nonzero `x`, and nonzero `α` are not needed to derive
the energy identity. They belong to the interpretation of `K` as a genuine
metric and of `x` as a characteristic state.

## Exact hostile

The fixture uses

\[
A=\operatorname{diag}(-1,0,1),\qquad
K=\operatorname{diag}(1,-1,1),
\]

with \(b=(1,1,1)\) and \(c=(1,-1,1)=Kb\). It records carrier-metric
commutation, actuator-to-sensor transport, numerator \(z^2+1\), and an
explicit invisible neutral state at \(z=i\). The carrier and metric are also
stated Hermitian. `threeStateNegativeImaginaryState` supplies the conjugate
witness at \(z=-i\), and `threeStateHostile_has_conjugate_neutral_pair`
packages the two dynamics, invisibility, and neutrality certificates.
The two `neutral_by_general_theorem` results independently derive the same
neutrality conclusions by instantiating the reusable finite theorem with
\(\alpha=1\). This checks that the hostile fixture and abstract interface have
matching types rather than merely parallel formulas.

The Hermitian realness step uses Mathlib's canonical
`Matrix.IsHermitian.im_star_dotProduct_mulVec_self` interface rather than a
local expansion of conjugated finite sums.

## Completion boundary

No completion theorem is stated in Lean. A faithful completion version needs
a normed directed family, convergence of the dynamics residual and sensor
pairing, uniform control of the paired residual, and a nondegenerate limiting
charge interface. None follows from the finite identity alone.

## Verification status

Per Nima's instruction, no Lean compilation or project build was run. The
draft is not imported into `MariciFormal.lean`. Static placeholder inspection
is the only permitted local check for this increment.
