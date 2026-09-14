# A cofinite complement assigns only a finite defect to the compact analytic channel

## Question

What is the simplest constructive architecture for stable joint observation when the analytic channel is compact?

## Claim boundary

A complementary observer may leave a finite-dimensional defect unobserved if the analytic channel is injective on that defect. Projection onto the orthogonal complement gives a canonical model. Equivariance requires the defect subspace to be invariant. This construction proves existence of stable complements but does not claim minimal target dimension or uniqueness.

## Problem

Let \(X,Y\) be Hilbert spaces and let

\[
A:X\to Y
\]

be bounded, possibly compact. The compact-channel theorem says a stable complement must be bounded below outside a finite-dimensional defect. We now construct exactly such a complement.

## Bold conjecture

A complement must observe every source direction directly; assigning any nonzero kernel to the compact analytic channel destroys stability.

## Named rivals

1. A finite-dimensional defect is admissible if \(A\) detects it injectively.
2. Any infinite-dimensional defect is admissible when \(A\) is coordinatewise nonzero.
3. Symmetry equivariance requires the defect to be invariant.
4. The analytic channel may cancel the complement on mixed defect/cofinite vectors and defeat stability.

## Finite-defect construction

Let \(K\subset X\) be finite-dimensional and suppose

\[
A|_K:K\to Y
\]

is injective. Let

\[
P=P_{K^\perp}:X\to K^\perp
\]

be the orthogonal projection. Define the complementary observer

\[
D=P.
\]

Then

\[
T=\binom AP:X\to Y\oplus K^\perp
\]

is bounded below.

### Proof by closed range

The projection \(P\) is bounded below on the finite-codimensional subspace \(K^\perp\). Its kernel is \(K\). Since \(A|_K\) is injective,

\[
\ker A\cap\ker P
=
\ker A\cap K
=0.
\]

A direct sequential argument avoids any compact-perturbation assumption on \(A\). If \(\|x_n\|=1\) and \(Tx_n\to0\), then \(Px_n\to0\), so \(x_n\) approaches the finite-dimensional unit sphere in \(K\). A convergent subsequence tends to \(k\in K\) with \(\|k\|=1\) and \(Ak=0\), contradicting injectivity of \(A|_K\). Therefore \(T\) is bounded below.

The sequential argument also resolves rival 4: cancellation in \(A(k+e)\) cannot coexist with \(e\to0\) and a nonzero limiting defect vector.

## Quantitative bound

Let

\[
a_K=
\inf_{k\in K,\ \|k\|=1}\|Ak\|>0,
\qquad
M=\|A\|.
\]

Write \(x=k+e\) with \(k\in K\), \(e\in K^\perp\). Fix

\[
\alpha=\frac{a_K}{2(M+a_K)}.
\]

If \(\|e\|\ge\alpha\|x\|\), then

\[
\|Tx\|\ge\|Px\|=\|e\|\ge\alpha\|x\|.
\]

Otherwise \(\|k\|\ge(1-\alpha)\|x\|\), and

\[
\|Ax\|
\ge
a_K\|k\|-M\|e\|
\ge
\frac{a_K}{2}\|x\|.
\]

Hence \(T\) has the explicit lower bound

\[
m(T)\ge
\min\left\{
\frac{a_K}{2(M+a_K)},
\frac{a_K}{2}
\right\}.
\]

The estimate is conservative but source-explicit.

## Infinite-defect no-go for compact analytic channels

Assume \(A\) is compact and \(D\) vanishes on an infinite-dimensional closed subspace \(K\). Choose an orthonormal sequence \((k_n)\) in \(K\). Then

\[
Dk_n=0,
\qquad
Ak_n\to0
\]

because compact operators send orthonormal sequences to norm-null sequences. Therefore

\[
Tk_n\to0.
\]

No lower bound exists. This rejects rival 2.

Thus a compact analytic channel can carry at most a finite-dimensional defect of a stable complementary observer.

## Symmetry-compatible construction

Let a group \(G\) act unitarily on \(X\). The projection \(P_{K^\perp}\) is \(G\)-equivariant exactly when \(K\) is a reducing invariant subspace. Therefore an equivariant finite-defect complement requires:

1. a finite-dimensional reducing subrepresentation \(K\subset X\);
2. injectivity of \(A|_K\);
3. the complement \(D=P_{K^\perp}\), or another equivariant operator bounded below there.

If the symmetry representation has no nonzero finite-dimensional reducing subrepresentation, the canonical equivariant projection complement has zero defect and must be bounded below on all of \(X\).

## Relation to genuine quotient descent

For a quotient \(G\to H\) with kernel-variation subspace \(X_K\), a descended analytic observer annihilates \(X_K\). If \(X_K\) is infinite-dimensional, it cannot be assigned as the defect of a compact analytic channel. The complement must be bounded below on it.

If \(X_K\) is finite-dimensional, the finite-defect construction can assign it to \(A\) only if \(A\) is injective there, which contradicts genuine quotient annihilation unless \(X_K=0\). Thus quotient-kernel variation is never an admissible defect for the descended channel itself.

## Green/Real worked example

The compact Euler-to-radial channel may detect a finite exceptional subspace while the discrete arithmetic observer carries the cofinite margin. The defect subspace must be compatible with the retained prime, grade, Real, and reciprocal decompositions if the complement is to preserve those structures.

The fold

\[
C_uF^2=W_uC_u
\]

transports invariant defect subspaces unitarily. The Real identity

\[
U^\top=U^*
\]

controls the reverse map on the analytic component but does not enlarge the allowed defect beyond finite dimension.

## Constructor-role specification

A `cofinite_complementary_observer` must declare:

- its finite-dimensional kernel \(K\);
- a lower bound on \(K^\perp\);
- an analytic defect map \(A|_K\);
- proof that \(A|_K\) is injective;
- symmetry, Real, and reciprocal invariance of \(K\) when required.

Without these fields, “complementary” records only intention, not stable reconstruction.

## Strongest falsification attempt

The possible cancellation of \(Ak\) by \(Ae\) is the strongest elementary objection. The sequential proof eliminates it because loss of the complementary observation forces \(e\to0\), while finite dimensionality makes the remaining defect subsequence converge. The theorem would fail for infinite-dimensional \(K\), exactly as the orthonormal counterexample shows.

## Disposition

The bold conjecture is rejected. A stable complement may leave a finite-dimensional defect, but the analytic channel must detect that defect injectively. Compactness makes finite dimensionality necessary. Symmetry compatibility further types the defect as a reducing subrepresentation. This provides the first constructive observer design, rather than only a no-go criterion.
