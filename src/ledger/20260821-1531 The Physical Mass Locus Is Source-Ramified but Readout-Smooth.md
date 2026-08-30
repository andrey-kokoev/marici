---
author: marici.Nima
---

# 1531 — The Physical Mass Locus Is Source-Ramified but Readout-Smooth

## Status

Exact Jacobian separation for the carrier-to-lens and lens-to-readout arrows.

## Two maps

The corner construction factors as

\[
(y_1,y_2)
\xrightarrow{\;\ell\;}
(A,B)
\xrightarrow{\;q\;}
(s,p),
\]

where

\[
A=(y_1+y_2)^2,\qquad
B=(y_1-y_2)^2,
\]

and

\[
s=A+B,\qquad p=AB.
\]

The first arrow is the source-to-coefficient-lens parametrization. The second
is the deck-invariant scalar readout.

## Readout quotient

For \(q(A,B)=(A+B,AB)\),

\[
\boxed{
\det Dq=A-B.
}
\]

On the generic physical mass diagonal \(y_2=y_1=y\ne0\),

\[
(A,B)=(4y^2,0),
\qquad
\det Dq=4y^2\ne0.
\]

Thus the scalar quotient is smooth there. Its loss of the ordered channel
label is a finite deck identification, not local rank loss.

## Source parametrization

For the composite source readout,

\[
\boxed{
\det D_{(y_1,y_2)}(s,p)
=-32y_1y_2(y_1^2-y_2^2).
}
\]

Hence this Jacobian vanishes on both signed mass diagonals
\(y_2=\pm y_1\). The source reaches \(p=0\) with quadratic contact:

\[
p=(y_1-y_2)^2(y_1+y_2)^2.
\]

## Meaning

Two phenomena previously grouped as “projection” are now separated:

\[
\boxed{
\begin{array}{rcl}
\text{lens}\to\text{readout}
&:&\text{smooth finite deck quotient},\\
\text{source}\to\text{lens/readout}
&:&\text{ramified physical specialization}.
\end{array}
}
\]

The physical channel reduction is encoded by tangency in the source map,
whereas the scalar readout forgets only the ordering of the resulting
channels. Neither requires a new carrier divisor.

This typing matters cross-sector: a physical locus can be singular for the
source parametrization while remaining smooth in coefficient and readout
space.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entries 1529–1530;
- allocator claim seqclaim-16add63e341466809b6b7737.
