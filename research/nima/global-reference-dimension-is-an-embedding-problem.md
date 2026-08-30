# Global reference dimension is an embedding problem

## Question

Does the dimension of an invisible gauge orbit determine the number of scalar
reference channels needed to recover it?

## Claim boundary

Only locally and linearly. Globally, the minimum continuous reference is an
embedding problem for the unresolved fiber. This packet proves the circle
case relevant to a residual phase gauge.

## Linear lower bound

For a linear observation \(L:V\to W\) with kernel \(K\), a linear reference
\(R:V\to U\) restores faithfulness exactly when \(R|_K\) is injective. Hence
\(\dim U\geq\dim K\). This is the existing kernel-reference theorem.

The bound does not imply that every nonlinear or compact one-dimensional
fiber embeds in one real coordinate.

## Circle obstruction

Suppose dagger exchange leaves a residual phase orbit \(U(1)\). No continuous
map

\[
r:S^1\longrightarrow\mathbb R
\]

is injective. If it were, compactness of \(S^1\) and the Hausdorff property of
\(\mathbb R\) would make \(r\) a homeomorphism onto its image. The image is a
compact connected subset of \(\mathbb R\), hence a closed interval. A circle
is not homeomorphic to an interval.

Therefore one real scalar reference cannot globally fix a phase, despite the
phase orbit having real dimension one.

## Two-quadrature repair

The standard map

\[
z\longmapsto(\operatorname{Re}z,\operatorname{Im}z)
\]

embeds \(S^1\) in \(\mathbb R^2\). Two real quadratures, or one genuinely
complex reference channel retaining both quadratures, suffice.

A single local angle coordinate is not a counterexample. It requires a branch
cut and cannot define one continuous global reference port.

## Effect of a Real structure

If independently source-derived linear and antilinear exchanges have trivial
mixed square, the phase orbit first descends to the two-point orientation
fiber \(\mu_2\). One signed real reference can then separate the two points.

Thus there are two distinct architectures:

1. dagger only: retain two real quadratures to fix \(U(1)\);
2. compatible linear and dagger exchanges: prove the Real-structure coherence,
   then use one signed augmentation to fix \(\mu_2\).

The second architecture uses fewer readout coordinates because it contains
more source-derived structure. It is not a cheaper presentation of the first.

## Cross-sector consequences

- Pure flavor rates observe magnitudes and remain sign- or phase-blind.
  Recovering phase requires interference or another signed quadrature, not
  merely absolute calibration.
- A luminosity monitor can fix one positive common-gain coordinate because
  that fiber is contractible, but it cannot by itself recover a phase.
- Optical homodyne tomography needs two quadratures globally unless a trusted
  phase frame has already reduced the admissible orbit.
- A theta/Tate endpoint scalar can orient a Real line only after the mixed
  exchange square has been proved trivial.

## DPC

For each unresolved fiber \(F\), determine the minimum admissible reference
object by:

1. identifying \(F\) after all source-derived coherencers;
2. specifying the topology retained by completion;
3. proving that the proposed reference map embeds \(F\);
4. rejecting dimension counting as sufficient when \(F\) is nonlinear or
   topologically nontrivial;
5. requiring the embedding coordinates to be physically constructible.

## Disposition

The minimum reference problem is not port counting. It is source-authorized
embedding of the unresolved fiber. For a phase circle, one real reference is
globally impossible and two quadratures are minimal in the standard linear
carrier.

## Verification

The checker check_global_reference_embedding.py verifies exact collisions for
individual linear quadratures, injectivity of the two-quadrature inclusion on
the same hostile family, and separation of the two-point orientation fiber by
one signed scalar.
