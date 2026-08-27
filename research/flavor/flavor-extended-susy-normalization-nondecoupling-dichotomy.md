# Extended-SUSY normalization/nondecoupling dichotomy: WP751

## Question

Can exact extended supersymmetry supply the stronger operator normalization
that WP750 requires while retaining the soft mass needed for the
nondecoupling portal?

## Admitted normalization

Use a canonically normalized \(N=2\) gauge multiplet and hypermultiplet. In the
declared convention the hypermultiplet interaction obeys

\[
y_{\mathrm{hyper}}^2=2g^2.
\]

This is the desired kind of source restriction: the matter interaction is
tied to the gauge metric rather than assigned an independent Wilson
coefficient.

## Exact-symmetry branch

The heavy-vector mass is

\[
M_V^2=2q^2g^2v^2.
\]

Exact \(N=2\) supersymmetry admits no soft scalar mass in this sector, so

\[
m_{\mathrm{soft}}^2=0,
\qquad
\epsilon
=\frac{m_{\mathrm{soft}}^2}{M_V^2+m_{\mathrm{soft}}^2}
=0.
\]

The additional nondecoupling portal therefore vanishes. This is consistent
with the standard construction of nondecoupling \(D\)-terms as a soft-breaking
effect in the gauge-breaking sector; see
[Maloney, Pierce, and Wacker](https://arxiv.org/abs/hep-ph/0409127).

## Broken-symmetry branch

After breaking to \(N=1\), the local exchange-even spurion operator has a
Wilson coefficient \(c\). Writing its breaking scale as \(x^2\) gives

\[
m_{\mathrm{soft}}^2=cx^2,
\qquad
\epsilon=\frac{cx^2}{2q^2g^2v^2+cx^2}.
\]

The portal is restored, but both \(c\) and \(x\) are new source data. Even
imposing the strongest WP749 correlation,

\[
x^2=g^2v^2,
\]

leaves

\[
\epsilon=\frac{c}{2q^2+c}.
\]

At \(q^2=1\), the admissible values \(c=1\) and \(c=3\) again give contrasts
\(g^2/6\) and \(3g^2/10\), with residual \(2g^2/15\).

## Disposition

There is an exact normalization/nondecoupling dichotomy:

- exact \(N=2\) fixes the supersymmetric interaction but yields no additional
  portal;
- generic local breaking restores the portal but also restores the
  Wilson-coefficient fiber.

Extended supersymmetry alone is therefore not the sought hard-to-vary source
explanation. The conclusion is bounded: it does not exclude an independently
required geometric or topological breaking operation that uniquely fixes its
twist, coefficient, sign, and relation to the gauge metric.

The sharp successor is a source-derived breaking constructor, such as
Scherk–Schwarz or orbifold breaking, audited for whether its twist is
quantized rather than chosen. It must still prove anomaly freedom, an
attractive RG basin, threshold support, physical16 descent, and a calibrated
instrument.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp751_extended_susy_normalization_nondecoupling_dichotomy.py

Generated result:
research/flavor/results/wp751_extended_susy_normalization_nondecoupling_dichotomy.json
