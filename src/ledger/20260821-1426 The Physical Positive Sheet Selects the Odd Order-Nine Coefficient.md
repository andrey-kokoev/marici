# 1426 — The Physical Positive Sheet Selects the Odd Order-Nine Coefficient

## Status

Exact termwise deck-parity theorem with replicated modular nonvanishing.

## Uniform-sheet coefficient

On either uniform sheet, no non-total-energy radial constant cancels. Every one of the \(180\) source terms therefore has \(\tau\)-order nine.

Its leading coefficient is

\[
c_S(r)
=
\sum_{T=1}^{180}
\frac{1}{5\prod_{q\in T\cup\{g_1,\ldots,g_5\}}c_q(S,r)},
\]

where the product contains the nine non-total-energy denominator constants.

## Exact complement relation

Global deck complement changes the sign of every one of those nine constants. Hence term by term

\[
c_{31}(r)
=
(-1)^9c_0(r)
=
-c_0(r).
\]

Thus

\[
\boxed{c_{31}=-c_0}
\]

as a rational function wherever the leading coefficients are defined.

## Nonvanishing samples

The complete source sum gives

\[
(c_0,c_{31})=(609,410)
\quad\bmod1019,
\]

and

\[
(c_0,c_{31})=(379,630)
\quad\bmod1009.
\]

In each field the entries are nonzero and exact negatives.

## Physical sheet selection

Entry 1217 freezes the Euclidean loop chamber by

\[
y_i\ge0.
\]

This selects sheet \(0\) among the two uniform sheets. Therefore the physical relative current evaluates the anti-invariant order-nine line through the distinguished positive generator

\[
\boxed{c_+.}
\]

The selection comes from the source Betti chamber, not from choosing a convenient algebraic basis or dividing an odd pair by two.

## Consequence

The order-nine coefficient object and its physical readout have different types:

\[
\text{coefficient object}
=
\text{deck-odd line},
\]

\[
\text{physical readout}
=
\text{evaluation on the positive chamber}.
\]

This explains how a deck-odd coefficient can contribute a nonzero physical mixed-Tate period without mixing with the even growth-four sector.

## Next finite falsifier

Compare the positive-sheet exceptional integral of \(c_+(\tau,r)\) with Entry 1310’s exact mixed-Tate constant \(C_5\). The normalization must follow from the \(d^3\ell\) current and source orientation; modular nonvanishing alone does not identify the two coefficients.

Artifacts:

- research/benincasa/marici-gm/src/bin/five_site_two_normal_rees.rs
- research/benincasa/results/five-site-two-normal-rees.json

Allocator claim: seqclaim-d7706d52adf42ef8cb5f0b6b.
