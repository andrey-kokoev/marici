# Charged-cycle one-loop neutral backreaction

## Bounded question

Does the declared charged messenger cycle generate a nonzero correction to
the neutral quark Yukawas once the first finite loop is included?

## Frozen benchmark

This packet fixes the smallest calculable source slice:

- one generation and scalar coupling coefficients;
- diagonal positive vectorlike masses
  \(M_{A^u},M_{A^d},M_{B^u},M_{B^d}\);
- positive charged-scalar mass \(m_\chi\) and zero charged vacuum value;
- constant real neutral insertions \(s=\langle S\rangle\) and
  \(x=\langle X\rangle\);
- zero external momentum and four-dimensional Euclidean loop normalization;
- the WP627 and WP635 vertices plus their Hermitian conjugates;
- no claim yet about generation mixing, RG improvement, or detector response.

The loop is ultraviolet finite. The displayed overall sign depends on the
Lagrangian and Wick-rotation convention; the existence, coupling monomial,
mass dimension, and nonzero magnitude do not.

## Two neutral backreaction routes

The up correction follows the open fermion chain

\[
Q_L\to A_R^u\to A_L^u
\xrightarrow{C_A\chi}A_R^d\to A_L^d
\xrightarrow{Y_S^dS}B_R^d
\xrightarrow{C_B^*\chi^\dagger}B_L^u\to u_R.
\]

The charged scalar closes between the two cross-edges. The two same-chirality
segments supply the loop-momentum numerator, while the other two propagators
supply \(M_{A^u}M_{A^d}\). The down correction is the conjugate route and
supplies \(M_{B^u}M_{B^d}\).

Define the positive finite kernel

\[
K_5(a,b,c,d,e)={1\over16\pi^2}
\int_0^\infty {t^2\,dt\over
(t+a^2)(t+b^2)(t+c^2)(t+d^2)(t+e^2)}.
\]

Up to the declared common sign convention, the corrections are

\[
\delta Y_u=
Y_H^u C_A Y_S^d C_B^*Y_X^u,sx,
M_{A^u}M_{A^d}K_5,
\]

\[
\delta Y_d=
Y_H^d C_A^*Y_S^u C_BY_X^d,sx,
M_{B^u}M_{B^d}K_5.
\]

The five kernel arguments are the four messenger masses and \(m_\chi\).
Gauge charge closes because each constituent vertex is gauge neutral. The
coupling products are invariant relative to their neutral Yukawa endpoints
under the full declared field-rephasing groupoid.

## Exact equal-mass result

For all five masses equal to \(M>0\),

\[
K_5(M,M,M,M,M)={1\over192\pi^2M^4}.
\]

Consequently,

\[
\delta Y_u={Y_H^u C_A Y_S^d C_B^*Y_X^u\,sx
\over192\pi^2M^2},
\qquad
\delta Y_d={Y_H^d C_A^*Y_S^u C_BY_X^d\,sx
\over192\pi^2M^2}.
\]

On the unit-coupling slice with \(s=x=M=1\), each correction magnitude is
\(1/(192\pi^2)\), while setting either cross-edge to zero makes it vanish.
Thus WP643's exact tree-level product form does not survive this loop.

## Selector boundary

Nonzero backreaction is not yet selection. The correction depends on the free
complex product \(C_AC_B^*\), four other coupling normalizations, two neutral
insertions, and five masses. Varying these source coordinates moves the
`physical16` output continuously; no source equation selects a proper image or
fixed numerical displacement.

The next gate is generation lifting. Promote every coupling to its declared
flavor tensor, compute \(\delta Y_{u,d}\), canonically rediagonalize, and form
the rank of the induced 16-coordinate response over all fitted sheets. Only a
source relation that lowers that image rank can become a selector candidate.

## Reproduction

Run:

    uv run --with sympy python research/flavor/checkers/wp644_charged_cycle_one_loop_backreaction.py

The generated result is
`research/flavor/results/wp644_charged_cycle_one_loop_backreaction.json`.
