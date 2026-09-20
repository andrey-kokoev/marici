# Xi-torsion lift iteration 17: the derived real-analytic fiber of the energy defect is exactly the positive Haar residual

## Correct local ring

Fix a Xi zero `z_0` and complexify the Hermitian parameter locally by treating

\[
z\quad\text{and}\quad w
\]

as independent variables near `(z_0,bar z_0)`. Let

\[
O^{\rm ra}_{z_0}
=\mathcal O_{z_0}\widehat\otimes
\overline{\mathcal O}_{\bar z_0}
\]

and let

\[
I_\Xi=(\tau(z),\tau^\#(w)),
\]

where `tau^#(w)=overline(tau(bar w))`. Physical values are obtained by
restricting to `w=bar z`.

## Hermitian extension of the defect

Write the polarized energy as

\[
\mathcal E_{z,w}(x,y),
\]

holomorphic in `z,w` and sesquilinear after physical restriction. The prime
route defect has a local complexification

\[
\delta_p(z,w)
=
\mathcal E_{z,w}(J_\Phi u_+(z),J_\Phi u_+^\#(w))
-p^{-(z+w)}
\mathcal E_{z,w}(J_\Phi u_-(z),J_\Phi u_-^\#(w)).
\]

Modulo `I_Xi`, the stable-history identities give

\[
u_-=u_+,
\qquad
u_-^\#=u_+^\#.
\]

Therefore the divisor-fiber class is

\[
\boxed{
[\delta_p]
=
(1-p^{-(z+w)})[E_p(u)]
\quad\text{in }O^{\rm ra}_{z_0}/I_\Xi.
}
\]

On the physical point `(z_0,bar z_0)`, this is exactly

\[
(1-p^{-2\operatorname{Re}z_0})E_p(b_{z_0}).
\]

## Simple-zero consequence

If `z_0` is a simple Xi zero, the local divisor fiber is reduced at the chosen
point. Since the retained energy is nonzero,

\[
[\delta_p]=0
\quad\Longleftrightarrow\quad
1-p^{-2\operatorname{Re}z_0}=0
\quad\Longleftrightarrow\quad
\operatorname{Re}z_0=0.
\]

Thus vanishing of the correct real-analytic cokernel class is exactly critical-
line confinement. It cannot follow formally from the holomorphic Evans
cokernel without proving RH-strength information.

## Multiple zeros

If `tau` has multiplicity `m`, the quotient retains the jets

\[
O/(u^m,\bar u^m).
\]

Vanishing of `[delta_p]` then requires not only the scalar Haar residual to
vanish but also a finite array of mixed normal jets. This is stronger than
location of the zero alone. One must not infer these multiplicity conditions
from the holomorphic divisibility of `Delta_border` in only the `z` variable.

## Global cross-pair warning

The global joint zero set of `(tau(z),tau^#(w))` contains pairs of distinct Xi
zeros. Requiring

\[
1-p^{-(z+w)}=0
\]

on every cross-pair would be much stronger and generally unrelated to RH. The
construction must be local at the physical pair `(z_0,bar z_0)` and then
restricted to the real structure. A global product-divisor argument is
invalid.

## Relationship to the three objectives

Strictness and recoverability of the complex-linear codiagonal control the
terms in `delta_p` that contain `tau(z)` or `tau^#(w)`. After quotienting by
those terms, the positive baseline above remains. Hence the topology isolates
the obstruction cleanly but does not annihilate it.

The exact missing statement is now:

\[
[\delta_p]=0
\quad\text{in the physical local real-analytic Xi fiber}.
\]

For simple zeros this statement is equivalent to RH at `z_0`.

## Verdict

The appropriate divisor-fiber calculation falsifies the proposed formal
equivalence: excluding torsion in the holomorphic bordered cokernel does not
exclude the nonzero Hermitian fiber class. The latter is precisely the Haar
residual, not a completion artifact.