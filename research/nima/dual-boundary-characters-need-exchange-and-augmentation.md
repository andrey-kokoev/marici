# Dual boundary characters need exchange and augmentation

## Question

What is the smallest categorical object that can reconstruct two reciprocal
boundary characters from their scalar product without fitting a normalization?

## Claim boundary

This packet proves a finite algebraic reconstruction theorem for a
complex-linear exchange in a declared common frame. It does not construct the
theta/Tate boundary carriers, prove continuity of their traces, or establish a
determinant identity. An antilinear dagger exchange has a larger stabilizer;
that correction is classified in
`exchange-modality-classifies-the-residual-boundary-gauge.md`.

## Product forgetting

Let two one-dimensional boundary lines carry nonzero coefficients
\(\kappa_+\) and \(\kappa_-\). A scalar determinant readout sees only

\[
m=\kappa_+\kappa_-.
\]

For every nonzero \(\lambda\), the reciprocal rescaling

\[
(\kappa_+,\kappa_-)
\longmapsto
(\lambda\kappa_+,\lambda^{-1}\kappa_-)
\]

preserves \(m\). The product port therefore has an anti-diagonal
\(\mathbb G_m\)-kernel and cannot reconstruct either boundary coefficient.

## Exchange reduction

Adjoin a source-derived complex-linear exchange law identifying the two
coefficients in one declared common frame:

\[
\kappa_+=\kappa_-.
\]

If the product is normalized to one, exchange reduces the continuous gauge to

\[
\kappa_+=\kappa_-\in\{1,-1\}.
\]

Thus exchange removes reciprocal rescaling but does not select orientation.
The remaining sign is not visible to either the product or exchange equation.

## Augmentation gate

A source-derived augmentation \(\epsilon\) selecting the positive unit fixes
the last ambiguity:

\[
\epsilon(\kappa_+)=1.
\]

The reconstruction architecture is consequently not a scalar character. It is
the diagram consisting of two boundary lines, their product pairing, an
exchange comparison, and an augmentation. Each component has a distinct job:

- the pairing constructs the scalar totalization;
- exchange kills the continuous anti-diagonal gauge;
- augmentation selects the remaining discrete orientation.

No component can be inferred from the other two.

## Categorical form

Let \(L_+\) and \(L_-\) be invertible line objects, let
\(e:L_+\to L_-\) be the source exchange, and let
\(p:L_+\otimes L_-\to\mathbf 1\) be the scalar pairing. The automorphisms of
the pair preserving \(p\) form the anti-diagonal copy of \(\mathbb G_m\).
Requiring commutation with \(e\) leaves its two-torsion subgroup \(\mu_2\).
A compatible augmentation kills \(\mu_2\).

Therefore the forgetful map from augmented exchanged dual pairs to scalar
products is faithful on this normalization coordinate, while the corresponding
map without augmentation is not.

## Immediate theta/Tate gate

For any proposed pair of primitive and square boundary characters, ask for
three independently source-derived maps:

1. the joint determinant pairing;
2. a complex-linear sheet exchange in a declared common boundary frame;
3. an endpoint or archimedean augmentation fixing the unit orientation.

The scalar completed functional equation supplies at most the first image. It
does not construct the exchange or augmentation. An antilinear reciprocal
dagger must be typed separately and does not substitute for the linear
exchange. A hostile reciprocal rescaling falsifies any reconstruction claim
made before those maps exist.

## Disposition

The finite reconstruction problem is resolved. Product plus exchange is still
two-valued; product plus exchange plus augmentation is unique. The live
source-specific problem is to derive the exchange and augmentation maps on the
actual completed boundary carriers.

## Verification

`check_dual_boundary_exchange_augmentation.py` verifies product invariance,
the exchange reduction to two signs, the augmentation selection, and hostile
independence of the three gates.
