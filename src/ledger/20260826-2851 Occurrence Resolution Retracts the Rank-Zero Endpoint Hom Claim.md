# 2851 — Occurrence Resolution Retracts the Rank-Zero Endpoint Hom Claim

## Defect in Entry 2849

Entry 2849 treated the displayed positive-\(a\)-sheet period as a closed rank-one local system. It is not.

The positive endpoint collision lies at

\[
A_+=(5+4\kappa)p^2,
\qquad A=a^2.
\]

There are two labelled collision occurrences:

\[
a=+\sqrt{A_+},
\qquad
a=-\sqrt{A_+}.
\]

A loop around \(\kappa=-5/4\) sends

\[
\sqrt{A_+}\longmapsto-\sqrt{A_+}
\]

and therefore exchanges the two occurrences. It does not act by a sign on a closed positive-sheet line.

## Full occurrence monodromy

In the ordered occurrence basis, the monodromy is

\[
T=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The invariant and anti-invariant generators are

\[
e_++e_-,
\qquad
e_+-e_-.
\]

Hence

\[
\dim\ker(T-I)=1.
\]

The displayed positive-sheet period covector is anti-invariant because the two local \(da/w\) periods have opposite signs. But selecting that anti-invariant summand is a projection after occurrence resolution, not the monodromy of the full endpoint object.

## Correction

Entry 2849's claim that the full endpoint Hom object has invariant rank zero is retracted. It established only that the positive-sheet scalar truncation does not descend by itself.

The global endpoint-combination hypothesis is therefore reopened in a narrower, correctly typed form: construct the comparison on the full marked and unmarked occurrence modules, then determine which character is selected by the source physical chain.

No scalar \(VU-I\) or period-ratio test is admissible before that occurrence-resolved comparison exists.

## Next falsifier

Derive the full two-occurrence marked residue packet at \(\xi=-1\), including the values of the marked rational factor at both \(a\)-collision germs. Compare its deck representation with the unmarked two-occurrence packet at \(\xi=+1\). A physical scalar can survive only in a common character selected by an independently derived chain covector.

## Durable artifacts

- research/benincasa/check_soft_endpoint_occurrence_monodromy.py
- research/benincasa/soft-endpoint-occurrence-monodromy.json

