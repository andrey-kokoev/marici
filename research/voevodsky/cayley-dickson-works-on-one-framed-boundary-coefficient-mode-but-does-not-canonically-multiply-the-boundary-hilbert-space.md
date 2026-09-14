# Cayley--Dickson works on one framed boundary coefficient mode but does not canonically multiply the boundary Hilbert space

## Successful coefficient construction

Given one quaternionic coefficient algebra `H`, its Cayley--Dickson double is

\[
\mathbb O
=
\mathbb H
\oplus
\mathbb H\ell
\]

with

\[
(a,b)(c,d)
=
(ac-\overline db,
da+b\overline c).
\]

The exact checker constructs the seven imaginary units over the rationals and verifies:

- all seven square to `-1`;
- all 21 distinct pairs anticommute;
- a nontrivial norm-multiplicativity sample;
- a left Moufang identity sample;
- a nonzero associator sample.

Thus two **framed quaternionic coefficient lines** do produce a valid octonion coefficient fiber.

## Why this does not yet act on the semilocal boundary

A quaternionic Hilbert space `K` is a right or left module over `H`. It has scalar multiplication

\[
K\times\mathbb H
\to
K,
\]

but generally no vector--vector multiplication

\[
K\times K
\to
K.
\]

The Cayley--Dickson formula contains products such as `ac` and `bar(d)b`. If `a,b,c,d` are boundary vectors rather than quaternion coefficients, these products are undefined.

Therefore

\[
\boxed{
K^{\mathbb H}
\oplus
K^{\mathbb H}
}
\]

is not automatically an octonion algebra.

It is only an octonion-module candidate after a coefficient algebra and compatible action have been specified.

## Rank-one framed case

If a quaternionic boundary mode is a rank-one module with a chosen unit vector `u`, then

\[
K_u
=
u\mathbb H
\cong
\mathbb H.
\]

Two copies can then be identified with

\[
\mathbb H
\oplus
\mathbb H\ell
\cong
\mathbb O.
\]

But changing the frame `u` by a unit quaternion changes the coordinate multiplication. Unless the frame is selected by source geometry and the changes lie in the automorphism group `G2`, the octonion product is not canonical.

## Infinite prolate spectrum

The boundary feature is expected to contain infinitely many prolate/Sonin modes. Modewise octonion coefficients would lead formally to a measurable field

\[
\int^\oplus
\mathbb O_\lambdad\nu(\lambda).
\]

Pointwise octonion multiplication is not closed on plain `L2`: the product of two `L2` sections is generally only `L1`. A workable algebraic core would be

\[
L^\infty
\cap
L^2
\]

or a bounded continuous/Schwartz section algebra, followed by a module completion.

Thus even after framing, the Hilbert completion is naturally an octonion module, not a normed division algebra.

## Associativity conflict with operator composition

The cutoff, Fourier, and scaling maps compose associatively as operators. Octonion multiplication does not. Therefore the octonion product cannot replace operator composition in the realization category.

At most it can organize coefficient fibers or boundary channels, while categorical composition remains associative and the octonionic associator is represented by additional coherent data.

## Source-derived acceptance test

A semilocal octonionic boundary requires:

1. construction of the quaternionic opposite-polarity sewing;
2. a source-derived rank-one quaternionic line in each retained boundary mode, or a principal quaternionic frame bundle;
3. transition functions reduced from `Sp(1)` data to octonion automorphisms in `G2`;
4. a dense section algebra closed under pointwise Cayley--Dickson multiplication;
5. compatibility of conjugation with Hermitian adjoint;
6. invariance of the positive boundary norm;
7. a Moufang/alternativity check after sewing.

No current source result supplies items 2--4.

## Executable check

Run:

```text
python research/voevodsky/checkers/check_cayley_dickson_boundary_mode.py
```

Artifacts:

- `research/voevodsky/checkers/check_cayley_dickson_boundary_mode.py`
- `research/voevodsky/results/cayley_dickson_boundary_mode.json`

## Disposition

The octonionic experiment succeeds exactly at one framed coefficient mode:

\[
\boxed{
\mathbb H
\oplus
\mathbb H\ell
\cong
\mathbb O.
}
\]

It does not yet globalize to the semilocal boundary Hilbert space. The first missing geometric datum is a canonical quaternionic boundary line/frame field compatible with opposite-polarity sewing.
