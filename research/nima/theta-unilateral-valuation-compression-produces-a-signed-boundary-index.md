# Unilateral valuation compression produces a signed boundary index

## Source-derived polarization

The bilateral valuation chain has a canonical split by valuation sign:

\[
\ell^2(\mathbb Z)
=
\ell^2(\mathbb N_0)
\oplus
\ell^2(\mathbb Z_{<0}).
\]

This is not a spectral projector chosen from a desired inequality. It is the
original direct-versus-reciprocal cone distinction.

Compress the bilateral shift to the nonnegative cone. The resulting operator
is the unilateral shift \(S\) on \(\ell^2(\mathbb N_0)\).

For one prime \(p\), grade \(k\), and \(z=x+it\), define

\[
T_{p,k}(z)
=
\frac{p^{-k/2}}{k}
\left(
e^{kz\log p}S^k
-
e^{-kz\log p}S^{*k}
\right).
\]

## Exact self-commutator

Let

\[
P_k
=
I-S^kS^{*k}.
\]

This is the rank-\(k\) projection onto the first \(k\) valuation states. Since

\[
S^{*k}S^k=I,
\]

a direct calculation gives

\[
T_{p,k}^*T_{p,k}
-
T_{p,k}T_{p,k}^*
=
\frac{2p^{-k}}{k^2}
\sinh(2kx\log p)P_k.
\]

All phase-dependent cross terms cancel.

Therefore:

- for \(x>0\), \(T_{p,k}\) is strictly hyponormal on the boundary defect;
- for \(x<0\), it is strictly cohyponormal;
- for \(x=0\), the self-commutator vanishes.

The horizontal coordinate acquires a source-local orientation through the
finite-rank defect of unilateral transport.

## Kernel and cokernel exchange

The recurrence for

\[
T_{p,k}(z)v=0
\]

splits into \(k\) residue classes. Along each class, successive coefficients
have modulus ratio

\[
e^{2kx\log p}.
\]

For \(x>0\), a nonzero kernel sequence grows and is not square summable.
Hence

\[
\ker T_{p,k}(z)=0.
\]

For \(x<0\), each residue class supplies one square-summable kernel vector.
Hence

\[
\dim\ker T_{p,k}(z)=k.
\]

The adjoint gives the reciprocal statement for the cokernel. Away from the
seam the Toeplitz operator is Fredholm, and its defect moves from kernel to
cokernel as \(x\) changes sign. On the seam its symbol touches zero and the
Fredholm gap closes.

This is a genuine index-theoretic explanation of why the seam is special. It
does not inspect any zeta zero.

## Relation to the two sectors

The direct cone supplies injectivity on one side of the seam. The reciprocal
cone supplies the reflected injectivity on the other side. Neither cone is
the whole system; the completed object must sew their complementary defect
spaces.

Thus the two-sector architecture is no longer merely functional-equation
symmetry. It is a pair of oriented Fredholm charts whose kernel and cokernel
roles exchange at the common seam.

## Why this is not yet RH

The theorem is exact for one prime and one grade. The completed arithmetic
current contains many powers and primes. For a sum

\[
T(z)=\sum_{p,k}T_{p,k}(z),
\]

self-commutators contain mixed terms

\[
T_{p,k}^*T_{q,\ell}
-
T_{q,\ell}T_{p,k}^*.
\]

The single-edge positivity does not automatically survive these cross terms.
Nor does local injectivity imply injectivity of an infinite coupled sum.

The new RH-bearing question is therefore finite and noncircular:

Does the source assembly make the mixed self-commutator terms cancel, form a
positive Gram matrix, or become an exact boundary current?

## Smallest hostile test

Take two source edges

\[
T_1=aS-bS^*,
\qquad
T_2=cS^2-dS^{*2}.
\]

Compute

\[
[T_1+T_2]^*(T_1+T_2)
-
(T_1+T_2)(T_1+T_2)^*.
\]

Separate:

1. the positive single-edge boundary projections;
2. the mixed \(1\)-by-\(2\) commutator;
3. its smallest principal minor on the first three valuation states;
4. its transformation under reciprocal reflection.

If the mixed minor becomes negative for source coefficients in an open
half-strip, the hyponormal orientation route fails at the first interaction.
If it is an exact boundary square, the calculation identifies the missing
coherence law.

## Completion gate

Even if every finite cutoff is hyponormal and injective on its appropriate
side, completion requires a cutoff-independent lower bound or strict graph
exactness. The prime-vacuum cocycle already warns that:

- the primitive grade is distributional;
- the square grade is Hilbert but not absolutely summable;
- only the connected tail is ordinarily summable near the seam.

The signed boundary index must therefore extend through the three-grade rigged
carrier. Scalar determinant convergence is not enough.

## Disposition

Unilateral valuation compression supplies the first source-derived
orientation mechanism found in this programme:

\[
\operatorname{sgn}
\left(
T^*T-TT^*
\right)
=
\operatorname{sgn}(\Re z)
\]

on each individual source edge.

This is stronger than seam unitarity and different from coercivity. The next
decisive computation is whether source-authorized arithmetic assembly
preserves this signed boundary index or destroys it through mixed
commutators.
