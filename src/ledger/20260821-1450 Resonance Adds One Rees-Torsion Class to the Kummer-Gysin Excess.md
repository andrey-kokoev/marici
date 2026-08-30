---
author: marici.Benincasa
---

# 1450 — Resonance Adds One Rees-Torsion Class to the Kummer–Gysin Excess

## Status

Exact logarithmic/Rees model of Entry 1448's resonant exceptional fiber. The
calculation separates the generic flat line from the class that exists only at
the resonant associated grade.

## Rees parameter

Write the exceptional Kummer exponent as

\[
\alpha=m+s,
\qquad
m\in\mathbb Z,
\qquad
R=\mathbb Q[[s]].
\]

Meromorphically gauge away the integral factor \((t-1)^m\), while retaining
its divisor as a labelled lattice modification. The remaining connection on

\[
U=\mathbb P^1\setminus\{0,1,\infty\}
\]

is

\[
\nabla_s=d+s\,d\log(t-1).
\]

## Global logarithmic complex

Use the ordered logarithmic basis

\[
e_0=d\log t,
\qquad
e_1=d\log(t-1).
\]

The relevant global complex is

\[
R
\xrightarrow{\ \nabla_s\ }
Re_0\oplus Re_1,
\]

with

\[
\nabla_s(1)=s e_1.
\]

Therefore

\[
\boxed{
H^1_{\log}(U,\nabla_s)
\cong
Re_0
\oplus
\left(R/(s)\right)e_1.
}
\]

## Interpretation

The first summand is the flat continuation of Entry 1448's generic rank-one
Kummer--Gysin excess. The second is supported only at the resonant Rees fiber:

\[
\begin{array}{c|c}
s\ne0 & \dim H^1=1\\
s=0 & \dim H^1=2.
\end{array}
\]

Thus ordinary specialization at integral monodromy sees one extra class, but
that class is not an independently lifting generic coefficient. It is
\(s\)-torsion.

The base factor from Entry 1448 is

\[
\delta^{m+s}
=
\delta^m e^{s\log\delta},
\]

so the same Rees parameter records the logarithmic base monodromy. The integer
\(m\) remains part of the labelled lattice even though it is invisible in the
meromorphic local-system isomorphism class.

## Classification

\[
\boxed{
\text{one generic Kummer--Gysin line}
+
\text{one resonant Rees-torsion class}.
}
\]

Both are coefficient data on the forced resolution of an existing
partial-energy intersection. Neither requires a new carrier wall.

## Epistemic boundary

This is the logarithmic de Rham/Rees object. It does not by itself prove that
the torsion class is selected by a physical relative chain. The source
positive chamber misses \(X_1+y=0\), so any Betti activation requires analytic
continuation to that existing support.

## Next falsifier

Transport the source rapid-decay chain around \(\delta=0\) and test whether its
specialization pairs with the torsion generator \(e_1\). A zero pairing makes
the resonant class physically invisible; a nonzero pairing yields a supported
logarithmic endpoint correction without changing the carrier.

## Durable provenance

- Entry 1448's blowup chart \(q=\delta t\);
- allocator claim `seqclaim-0a991e508ef82edf13ad9ace`.
- epistemic event `ev-000000001541-7597dc7b-5b17-40d9-a141-9350050dd585`.
