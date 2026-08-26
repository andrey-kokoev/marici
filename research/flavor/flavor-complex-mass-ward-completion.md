# Complex-mass Ward completion

## Question

Can WP524's missing longitudinal and Goldstone sector be derived without
fitting a new flavor interaction, and can the independently computed residues
and widths be inserted consistently?

The Ward completion is universal pole by pole, but finite widths must be
introduced through one common complex-pole scheme. The currently composed
hierarchical widths are lower bounds, so the physical finite-width kernel is
still not instantiated.

## One-pole completion

Write \(t=q^2\), let \(\mu_p^2\) denote the pole parameter, and define

\[
d=q_\mu J_L^\mu=m_bS_R-m_sS_L.
\]

Suppressing the common signed current residue, the \(R_\xi\) vector exchange
is

\[
\mathcal A_V=
\frac{J_\mu J^\mu}{t-\mu_p^2}
-\frac{(1-\xi)d^2}
{(t-\mu_p^2)(t-\xi\mu_p^2)}.
\]

The Ward-fixed Goldstone exchange is

\[
\mathcal A_G=-\frac{d^2}
{\mu_p^2(t-\xi\mu_p^2)}.
\]

The checker proves the exact cancellation

\[
\mathcal A_V+\mathcal A_G
=\frac{J_\mu J^\mu-d^2/\mu_p^2}{t-\mu_p^2},
\]

which is independent of \(\xi\). This derives the completion from the same
massive gauge pole; it does not introduce an independently adjustable
Goldstone coupling.

## Induced operator family

Because

\[
d^2=m_b^2S_RS_R+m_s^2S_LS_L-2m_bm_sS_RS_L,
\]

the physical bilocal readout must include the vector left-left channel and
three scalar chiral structures. A lattice value for scalar \(H_0\) in the
vector channel alone is therefore not a faithful coordinate for the completed
exchange.

## Finite-width hostile test

Suppose a shifted pole \(\mu_p^2\) is inserted only into the visible vector
denominator while the longitudinal normalization and Goldstone pole retain a
real \(m_p^2\). The checker obtains

\[
\frac{\partial\mathcal A_N}{\partial\xi}
=-\frac{d^2(m_p^2-\mu_p^2)}
{(t-\mu_p^2)(t-\xi m_p^2)^2}.
\]

This is generically nonzero. At the exact hostile point frozen by the checker
it equals \(-5/4\). Thus adding a Breit--Wigner width only to the transverse
denominator destroys the Ward cancellation.

A consistent complex-mass or pole scheme must use the same \(\mu_p^2\) in
the transverse pole, longitudinal normalization, unphysical pole, and
Goldstone coupling. That requirement is structural and independent of the
numerical width.

## Residue and width authority

WP509 freezes exact matrix-residue functionals, and WP520 fixes their signed
aligned \(b\)-to-\(s\) scalar combination. WP518 transports trace residues and
resolved partial widths into a common hierarchical pole ordering. Its width
entries are explicitly lower bounds, not channel-complete total widths.

Therefore the ingredients do not yet form a legal complex pole:

- the signed current residue algebra exists;
- resolved quark and vector partial-width contributions exist;
- scalar, sub-resolution, off-shell, and other open channels are not closed;
- no pole scheme transports the resulting total self-energy through the Ward
  completion.

## Disposition

- Admitted state domain: the WP520 aligned source witness, pole by pole.
- Faithful quotient coordinate: the gauge-independent vector-plus-scalar
  bilocal operator packet.
- Source-authorized operation: Ward-related vector and Goldstone exchange with
  one common pole parameter.
- Classification: rigidifier of the allowed completion, not a numerical
  selector.
- Smallest exact falsifier: partial width insertion yields the nonzero
  \(\xi\)-derivative above.
- Instrument status: operator family typed, physical lattice values absent.
- Remaining gate: close every pole width, transport signed WP509/WP520
  residues into the same complex-pole ordering, and calculate the renormalized
  vector-plus-scalar \(B_s\) bilocal covariance.

WP525 therefore repairs the algebraic gauge completion while refusing the
premature combination of a valid residue packet with incomplete widths.
