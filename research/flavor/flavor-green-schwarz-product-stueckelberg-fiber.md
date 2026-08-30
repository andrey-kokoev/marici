# Green--Schwarz cancellation fixes a product, not the flux or physical threshold: WP781

## Question

Does the minimal Green--Schwarz completion left by WP780 make the oriented
family flux and its physical portal unavoidable?

## Minimal effective constructor

Let the anomalous fermion variation have coefficient \(A\). Let an axion shift
with coefficient \(k\), and let its Wess--Zumino coupling have coefficient
\(c\). Gauge invariance requires

\[
A-kc=0.
\]

Thus

\[
A=kc.
\]

This fixes only a product. For every nonzero \(\rho\),

\[
k\longmapsto \rho k,
\qquad
c\longmapsto \frac{c}{\rho}
\]

preserves the anomaly cancellation equation.

## The physical threshold varies along the allowed fiber

The Stückelberg term gives a mass of the form

\[
M_F^2=g_F^2f_a^2k^2.
\]

Under the product-preserving rescaling,

\[
M_F^2\longmapsto \rho^2 M_F^2.
\]

The static exchange below this threshold scales as

\[
\frac{g_F^2}{M_F^2}=\frac{1}{f_a^2k^2}
\longmapsto
\frac{1}{\rho^2}\frac{g_F^2}{M_F^2}.
\]

Therefore anomaly cancellation can protect the gauge variation while leaving
the mediator threshold and low-energy portal magnitude continuously
undetermined.

## Orientation and flux remain unselected

Reversing the matter charges reverses an odd Abelian anomaly coefficient.
Reversing the axion shift coefficient restores the same cancellation, while
the Stückelberg mass remains unchanged. Simultaneously reversing charge and
flux preserves the chiral index:

\[
(-q)(-m)=qm.
\]

The integer \(m\) does not occur in the local Green--Schwarz cancellation
equation. Hence that equation selects neither \(m=3\) nor its orientation.

## Authority boundary

This packet tests the minimal four-dimensional Green--Schwarz effective
theory. It does not infer a compactification lattice from the existence of
effective coefficients. A concrete geometry can quantize these data, as in
generalized Green--Schwarz constructions in
[F-theory](https://arxiv.org/abs/1210.6034), but the relevant intersection
lattice, characteristic vector, and flux tadpole must be supplied and tested
as one source object.

The accompanying Stückelberg mass is standard in anomalous Abelian effective
theories; see [Corianò, Irges, and Morelli](https://arxiv.org/abs/hep-ph/0703127).

## Classification

The minimal Green--Schwarz constructor is an anomaly rigidifier. It is not an
oriented-flux selector and does not fix portal magnitude, threshold survival,
or detector response. The smallest decisive pair is

\[
(k,c),
\qquad
(2k,c/2).
\]

They cancel the same anomaly, but their mediator masses differ by four and
their low-energy exchanges by one quarter.

The next admissible branch must name a concrete compactification intersection
lattice whose primitive characteristic vector fixes \(k,c,f_a\), and oriented
flux \(m=3\) simultaneously, then derive its production and decay ports.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp781_green_schwarz_product_stueckelberg_fiber.py

Generated result:
research/flavor/results/wp781_green_schwarz_product_stueckelberg_fiber.json
