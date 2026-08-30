# The first nonflat interface is the Fourier–trace descent defect

## Setup

Let `A` be a source amplitude space, let

\[
\tau:A\longrightarrow T
\]

be the additive-to-multiplicative trace or boundary map, and let `F` be the
source-normalized Fourier operator on `A`. We ask whether Fourier transport
induces an operator `J` on the trace object satisfying

\[
J\tau=\tau F.
\]

## Exact descent criterion

Put

\[
K=\ker\tau.
\]

An induced operator on `Ran(tau)` exists if and only if

\[
F(K)\subseteq K.
\]

Equivalently, the source-derived descent defect

\[
D=\left.\tau F\right|_K:K\longrightarrow\operatorname{Ran}\tau
\]

vanishes.

The proof is immediate but decisive. If `tau(a)=tau(a')`, then
`a-a'` lies in `K`. Representative independence of `tau(Fa)` is exactly the
condition `tau(F(a-a'))=0`.

Thus the first possible nonflat interface datum is not an arbitrary Fourier
phase. It is the failure of the trace kernel to be Fourier invariant.

## What happens when descent succeeds

If `tau` is injective, then `K=0` and

\[
J=\tau F\tau^{-1}
\]

on the trace range. More generally, if `D=0`, Fourier descends to the quotient.
Every polynomial relation satisfied by `F` descends. In particular, if

\[
F^2=R
\]

for source reflection `R`, then

\[
J^2=R_T.
\]

On the even source sector, `R_T=I`. The descended transport is therefore
involutive and flat. It cannot create a new divisor or cohomology class.

This closes a tempting route: an injective trace range supplies a legitimate
phase-framed sewing operator, but precisely because it is conjugate to
Fourier, it supplies no new RH-bearing obstruction.

## What happens when descent fails

If `D` is nonzero, then the quotient `T` erased source distinctions needed by
Fourier transport. The correct repair is not to choose representatives or add
a fitted phase. One must retain the kernel sector as interface data.

The two-term defect complex is

\[
K\xrightarrow{D}\operatorname{Ran}\tau.
\]

Its kernel records source-null packets whose Fourier images remain invisible;
its cokernel records transformed boundary packets not resolved by the lost
source fiber. This is the exact analogue of coherent control failing to
descend from a projective channel quotient.

## Consequence for the RH lane

The current completed-sewing construction deliberately works on an injective
trace range. On that declared range, `D=0` and the sewing operator is a
conjugate of Fourier. Therefore the RH obstruction cannot live in its local
coefficient holonomy.

The first surviving locations are later nonexact operations:

1. extension from the injective trace range to its completion;
2. multiplicative Mellin evaluation and its endpoint domain;
3. restricted-product passage retaining primitive and square currents;
4. scalar determinant or Evans compression;
5. comparison of two inequivalent completed trace ranges.

The interface tower has therefore moved one rung: source Fourier transport is
flat; the meaningful question is whether the next boundary/evaluation functor
preserves that flatness.

## Frozen finite falsifier

For any proposed finite trace model with matrix `Tau` and Fourier matrix `F`,
compute a basis matrix `Kmat` for `ker(Tau)` and the defect

\[
D_{\mathrm{fin}}=\mathrm{Tau}\,F\,\mathrm{Kmat}.
\]

There are exactly two dispositions:

- `D_fin=0`: construct the descended `J`, verify its inherited polynomial
  relations, and do not claim new cohomology;
- `D_fin!=0`: retain the kernel fiber and compute the homology of the defect
  complex before scalarization.

Unitarity of a convenient finite matrix does not test this condition. The
trace incidence and its kernel are essential.

## Scope

This identifies the exact obstruction to Fourier descent through the trace
quotient and proves flatness on an injective trace range. It does not compute
the genuine adelic trace kernel, construct the later Mellin boundary complex,
connect its defect to the Evans inner factor, or prove RH.
