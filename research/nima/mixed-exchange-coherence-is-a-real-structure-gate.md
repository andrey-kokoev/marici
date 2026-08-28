# Mixed exchange coherence is a real-structure gate

## Question

When linear sheet exchange and antilinear dagger exchange both exist, do they
automatically define the real structure needed by an oriented augmentation?

## Claim boundary

No. Their composite is antilinear, but it is a real structure only when a
separate coherence scalar is trivial. This is a one-dimensional finite theorem,
not a construction of the theta/Tate exchanges.

## Composite exchange

Let \(E:L_+\to L_-\) be complex-linear and let \(J:L_+\to L_-\) be
conjugate-linear. Their comparison on \(L_+\) is

\[
K=J^{-1}E.
\]

In a coordinate, every antilinear automorphism has the form

\[
K_c(z)=c\overline z,
\qquad c\in\mathbb C^\times.
\]

Its square is the linear scalar

\[
K_c^2(z)=|c|^2z.
\]

Thus the mixed-exchange coherence defect is

\[
\delta=|c|^2.
\]

The two exchanges define a real structure exactly when \(\delta=1\).

## Fixed-ray criterion

A nonzero fixed vector satisfying \(K_c(z)=z\) exists exactly when
\(|c|=1\). Necessity follows by taking norms. For a unit \(c\neq-1\), the
vector \(1+c\) is fixed; for \(c=-1\), the vector \(i\) is fixed.

Therefore an augmentation cannot orient a common real ray until the
mixed-exchange square has been checked. Merely possessing both exchange maps is
insufficient.

## Categorical interpretation

The comparison of the linear and antilinear exchanges is itself a coherencer.
Its square is a scalar automorphism of the identity. Trivializing that scalar
is the next coherence cell. Only after this cell exists does the boundary line
descend from a complex line with two comparisons to a Real line with two
orientations.

This identifies a strict four-stage reconstruction ladder:

1. pairing removes no reciprocal gauge;
2. dagger exchange restricts it to phase;
3. linear exchange plus a trivial mixed square restricts it to sign;
4. augmentation selects the sign.

## Finite falsifier

Take \(c=2\). Both exchange maps remain invertible, but \(K_c^2=4\) and no
nonzero fixed vector exists. Any construction that declares a real boundary
frame from invertibility alone fails on this one scalar witness.

## Disposition

The missing coherencer is explicit: prove that the source comparison
\(J^{-1}E\) has trivial square. If theta/Tate supplies no linear exchange, or
if the mixed square is nontrivial, the orientation programme remains phase
ambiguous before any positivity question is reached.

## Verification

`check_mixed_exchange_real_structure.py` verifies the square, fixed-vector
criterion, exact unit-phase witnesses, and the hostile scalar \(c=2\).
