# Off-seam count is an exact witness but not a continuous Green margin

Event 10282 defined

\[
M_\eta
=
\sum_{\Re\rho\ne1/2}
m_\rho e^{-\eta(\Im\rho)^2}.
\]

It is positive and vanishes exactly under RH. However, it is a rank/counting
witness, not a continuous transverse-energy margin.

Let an off-seam reciprocal pair have distance

\[
d=|\Re\rho-1/2|.
\]

As \(d\downarrow0\), its contribution to \(M_\eta\) remains

\[
m_\rho e^{-\eta\gamma^2},
\]

then drops discontinuously to zero when \(d=0\) and the zero is reclassified
as a seam atom. Thus \(M_\eta\) depends on an already-separated off-seam
divisor and is not continuous under divisor motion through the seam.

This is acceptable for exact zero exclusion after spectral identification,
but it cannot be the coercivity quantity explaining completion stability.

## Continuous transverse energy

The natural continuous witness is

\[
E_\eta
=
\sum_\rho
m_\rho
\left(\Re\rho-\frac12\right)^2
e^{-\eta(\Im\rho)^2}.
\]

It has the required properties:

\[
E_\eta\ge0,
\]

\[
E_\eta=0
\quad\Longleftrightarrow\quad
\Re\rho=\frac12
\ \text{for every nontrivial zero},
\]

and each pair contribution tends continuously to zero as \(d\downarrow0\).

A linear-distance version

\[
L_\eta
=
\sum_\rho
m_\rho
\left|\Re\rho-\frac12\right|
e^{-\eta(\Im\rho)^2}
\]

also detects RH, but \(E_\eta\) is better matched to a quadratic Green energy.

## Constructor distinction

The two witnesses belong at different levels:

- \(M_\eta\): spectral rank after the divisor is already split into seam and
  off-seam sectors;
- \(E_\eta\): transverse Green energy that may be defined before such a hard
  classification.

Therefore

\[
M_\eta=0
\]

is a clean final spectral test, while

\[
E_\eta=0
\]

is the appropriate candidate for an operator/energy explanation.

The decisive source theorem would construct an operator \(N_\perp\) whose
spectral value on a zero state is the normal displacement

\[
N_\perp\psi_\rho
=
\left(\Re\rho-\frac12\right)\psi_\rho.
\]

Then

\[
E_\eta
=
\operatorname{Tr}
\left(
e^{-\eta H_t^2}
N_\perp^*N_\perp
\right)
\]

in a declared determinant/trace-class frame. This formula must not be used
before the zero-state representation and trace authority are established.

## Margin warning

Even \(E_\eta=0\) is an exact RH criterion, not automatically a uniform
coercivity margin. A family of hypothetical zeros can approach the seam with
\(d_j\to0\), making the energy arbitrarily small. A strict lower margin would
assert a zero-free transverse gap, which is stronger than RH and generally
not expected.

Thus the final architecture should separate:

\[
\text{five-margin constructor coercivity}
\to
\text{spectral identification}
\to
E_\eta=0
\to
\text{RH}.
\]

One must not reinterpret RH itself as a positive uniform distance of zeros
from the seam.
