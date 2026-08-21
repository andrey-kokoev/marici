---
title: "The Five-Cycle Infinity Constant Is a Graph-Specific Mixed-Tate Logarithmic Period"
date: 2026-08-20
entry: 1310
status: active-narrow-result
author: marici.Benincasa
---

# 1310 — The Five-Cycle Infinity Constant Is a Graph-Specific Mixed-Tate Logarithmic Period

Sequence claim: `seqclaim-a2f254dad36d926bdfc80b78`.

## Exact five-cycle value

Entry 1303 leaves the leading infinity coefficient

\[
C_5=\lim_{z\to\infty}z^7\Pi_{C_5}(z).
\]

At coalesced focus all five edge radii equal \(r\). The complete 180-term
canonical function becomes radial. Its eleven exact selected-size profiles
reduce the coefficient to a rational integral on \([0,\infty)\).

Exact rational partial fractions give

\[
\boxed{
C_5
=
4\pi\left[
-\frac{3797899}{995328}
+\frac{17729}{2916}\log 2
-\frac{87}{256}\log 3
-\frac{2225}{147456}\log 5
\right].
}
\]

Numerically,

\[
C_5=0.01131604369561690\ldots
\]

The independent Gauss--Legendre computation gives
\(0.01131604369562018\ldots\); the difference is below
\(4\times10^{-15}\).

## Lower-cycle comparison

Apply the identical unit-weight, coalesced-focus, physical \(d^3\ell\)
convention to the frozen 28-term four-cycle packet. Its four selected-size
profiles give

\[
\boxed{
C_4
=
4\pi\left[
\frac{485}{432}
-\frac{1481}{648}\log 2
+\frac{27}{64}\log 3
\right].
}
\]

Numerically,

\[
C_4=0.02486434847891004\ldots
\]

and

\[
\frac{C_5}{C_4}
=
0.45511120893496071\ldots
\]

There is no equality or evident universal numerical normalization.

## Classification

The decimal \(C_5\) is graph-specific. Its coefficient class is not exotic:

\[
\boxed{
C_n\in
\pi\left(
\mathbb Q+\sum_{k=2}^{n}\mathbb Q\log k
\right)
}
\]

for the verified cases \(n=4,5\).

The logarithmic alphabet is compiled directly from the integer connected-
region sizes appearing in the frozen OFPT walls. At five sites, the new
\(\log 5\) term appears because size-five one-cut-total factors enter the
selected profile. Thus the reusable structure is the wall-size logarithmic
period class, not the numerical constant.

This is evidence for sector-specific coefficient periods generated from the
existing labelled carrier.

## Verification

The checker:

1. derives the selected-size multiplicities from the source packets;
2. computes all partial-fraction coefficients over exact \(\mathbb Q\);
3. verifies cancellation of the total simple-pole coefficient at infinity;
4. evaluates the remaining rational and logarithmic boundary terms;
5. compares the five-cycle answer with independent high-order quadrature.

## Scope

The displayed pattern is verified only at four and five cycles. It is not an
all-\(n\) theorem.

## Next falsifier

Derive the general coalesced-focus profile enumerator from the OFPT
triangulation. Test at six sites whether

\[
C_6\in\pi\left(\mathbb Q+\sum_{k=2}^{6}\mathbb Q\log k\right)
\]

and whether the \(\log 6\) coefficient is nonzero. Failure would locate the
first higher-depth infinity period; success would support a carrier-compiled
mixed-Tate theorem for the leading asymptotic coefficient.
