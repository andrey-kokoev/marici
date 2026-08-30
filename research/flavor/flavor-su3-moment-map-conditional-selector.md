# SU(3) moment-map conditional selector: WP746

## Question

Can a simple rank-two gauge group turn the quantized-data idea into the correct
CP-even portal operation while removing WP716's independently rescalable gauge
metrics?

## Exact simple-group construction

Use the normalized Cartan generators of the (SU(3)) fundamental. Its weights
are

\[
\begin{aligned}
w_1&=\left(\frac12,\frac{1}{2\sqrt3}\right),\\
w_2&=\left(-\frac12,\frac{1}{2\sqrt3}\right),\\
w_3&=\left(0,-\frac{1}{\sqrt3}\right).
\end{aligned}
\]

A single simple-group Killing metric supplies the positive pairing

\[
\langle u,v\rangle=g^2u\mathbin\cdot v.
\]

On the conditional weight-ray assignment

\[
w_\chi=w_n=w_1,
\qquad
w_m=w_2,
\]

the (D)-term square gives

\[
g_n=\frac{g^2}{3},
\qquad
g_m=-\frac{g^2}{6},
\qquad
g_n-g_m=\frac{g^2}{2}.
\]

The radial Gram margin is strictly positive:

\[
4\lambda_n\lambda_m-\lambda_x^2
=g^4\det(w_1,w_2)^2
=\frac{g^4}{12}.
\]

This is the first post-WP745 construction in which quantized representation
data enters the correct CP-even positive square. The simple group fixes the
relative Cartan metric, portal sign ratio, and radial support without an
independent (g_n-g_m) coefficient.

## Ordered-orientation fiber

The same source grammar permits the channel assignment

\[
w_n=w_2,
\qquad
w_m=w_1,
\qquad
w_\chi=w_1.
\]

It preserves the unordered portal pair and the Gram margin but reverses the
ordered contrast to (-g^2/2). Before a source-derived embedding distinguishes
the physical channel labels, the Weyl-related weight data selects an orbit,
not an ordered sign. A reference that fixes the embedding changes the
stabilizer groupoid and must be stated explicitly.

## Physical-domain obstruction

The (SU(3)) fundamental is a complex three-dimensional carrier, hence six
real dimensions. It is not the admitted real irreducible (SO(3)) triplet. For
example, an imaginary off-diagonal generator sends the real vector (e_1) to
(ie_2/2), outside the real slice.

Thus the construction realizes the WP715–WP716 moment-map identities only on
the enlarged domain already diagnosed by WP725. It does not directly descend
to physical16. An anomaly-free messenger or auxiliary completion would need a
separate exact elimination map back to neutral real invariants.

## Magnitude, RG, threshold, and instrument gates

The simple group removes the relative metric freedom but not the common scale:

\[
g^2\longmapsto s g^2
\quad\Longrightarrow\quad
g_n-g_m\longmapsto s(g_n-g_m).
\]

An interacting fixed point and a source-authorized clock are still required.
Supersymmetric heavy-vector thresholds can decouple, and a low-energy
nondecoupling (D)-term requires a declared breaking sector and matching
calculation. Cartan weights are algebraic labels, not calibrated detector
channels.

## Disposition

The simple (SU(3)) moment map repairs the operator-type problem: it is a
conditional CP-even sign/ratio and radial selector on a complex carrier. It is
not yet the requested flavor selector because its ordered embedding, descent
to the real physical quotient, common gauge magnitude, RG clock, threshold
completion, and instrument remain unselected.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp746_su3_moment_map_conditional_selector.py`.

Generated result:
`results/wp746_su3_moment_map_conditional_selector.json`.
