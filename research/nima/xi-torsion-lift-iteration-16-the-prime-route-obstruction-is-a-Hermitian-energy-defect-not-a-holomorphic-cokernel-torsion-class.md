# Xi-torsion lift iteration 16: the prime-route obstruction is a Hermitian energy defect, not a holomorphic cokernel torsion class

## Correction to iteration 15

The repository already retracts the vector route-matching target

\[
J_\Phi(u_+)=T_pJ_\Phi(u_-).
\]

Prime dilation is translation by `log p` in logarithmic coordinates, and a
nonzero `L2` state cannot be fixed by that translation. Consequently the vector
defect `Omega_p` is not the correct closure object and should not be required
to be Xi-divisible.

## Correct prime-route defect

The source-defined object is the scalar Hermitian energy difference

\[
\delta_p(z)
=
\mathcal E_z(J_\Phi u_+(z))
-
\mathcal E_z(T_pJ_\Phi u_-(z)).
\]

Relative-Haar covariance gives

\[
\delta_p(z)
=
\mathcal E_z(J_\Phi u_+(z))
-p^{-2\operatorname{Re}z}
\mathcal E_z(J_\Phi u_-(z)).
\]

At an Xi zero, `u_+=u_-=u_z`, hence

\[
\delta_p(z)
=
(1-p^{-2\operatorname{Re}z})
\mathcal E_z(J_\Phi u_z).
\]

Since the retained energy is positive, its vanishing is equivalent to critical-
line confinement.

## Why holomorphic torsion is the wrong type

`H_border`, `Delta_border`, and the translated-theta codiagonal are
complex-linear and holomorphic in `z`. The energy defect depends on both `z`
and `bar z`. It is not a section of their holomorphic cokernel and cannot be a
`tau`-torsion class there.

Substituting

\[
u_-=u_++\tau e_z
\]

into the second energy produces mixed terms involving

\[
\tau,
\qquad\overline\tau,
\qquad |\tau|^2,
\]

plus the baseline term

\[
(1-p^{-2\operatorname{Re}z})
\mathcal E_z(J_\Phi u_+).
\]

The baseline survives after setting `tau=0`; proving that it vanishes is exactly
the RH-strength energy-cycle law.

## Correct real-analytic formulation

One may work over a complexified real-analytic ring in independent variables
`(z,w)` and replace conjugation by restriction to `w=bar z`. Then the natural
divisor ideal is

\[
(\tau(z),\overline{\tau}(w)).
\]

But membership of the energy defect in this ideal would require its restriction
to the joint Xi locus to vanish. That restriction is precisely the positive
Haar residual above. Thus the ideal-membership claim is equivalent to the
missing theorem, not a consequence of bordered holomorphic strictness.

## Status of the three requested objectives

1. Strict/horizontal common-history recovery is available in the appropriate
   constant-coefficient Fourier graph category.
2. `H_border` has a labelled shellwise lift and recoverable bordered
   coordinates.
3. Excluding holomorphic Xi torsion in that Evans-bordered sector does **not**
   imply the Hermitian energy-cycle law and is not equivalent to 1--2.

The word “equivalently” must therefore be removed if the intended consequence
is relative-Haar confinement.

## Next executable direction

The remaining object to study is the real-analytic energy defect `delta_p`
itself. A noncircular advance must derive its vanishing on the joint Xi locus
from an independently sourced metric conservation law, finite Schur
certificate, or prime-diagonal Green identity—not from holomorphic codiagonal
torsion.