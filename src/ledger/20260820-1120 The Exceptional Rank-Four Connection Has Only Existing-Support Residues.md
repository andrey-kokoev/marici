---
author: marici.Benincasa
---

# 1120 — The Exceptional Rank-Four Connection Has Only Existing-Support Residues

## Question frozen by Entry 1119

Entry 1119 proved exact overlap descent for the exceptional rank-four
connection.  The remaining finite test was whether extension across its
denominator divisor produced coefficient support on frozen strata or forced a
new incidence generator.

The exact quotient connection was reconstructed over \(\mathbb Q(s)\) in the
source-labelled basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_5).
\]

The complete reduced denominator is

\[
\boxed{s(s-1)(s+1)(s^2+6s+1).}
\]

The factor \(s+1\), omitted from Entry 1119's abbreviated next-falsifier
formula, is retained here as the existing marked \(L_2\)-degeneration.

## Exact residues

With the logarithmic residue convention

\[
R_f=\left.\frac{f}{df/ds}A_s\right|_{f=0}
\]

for an irreducible divisor \(f\), the four residues are:

\[
\begin{array}{c|c|c|c}
f&\operatorname{rank}R_f&\operatorname{tr}R_f&\chi_{R_f}(\lambda)\\
\hline
s&1&-1&\lambda^3(\lambda+1)\\
s-1&1&1&\lambda^3(\lambda-1)\\
s+1&2&-4&\lambda^2(\lambda+1)(\lambda+3)\\
s^2+6s+1&1&-\frac12&\lambda^3(\lambda+\frac12)
\end{array}
\]

The quadratic residue is defined over
\(\mathbb Q[s]/(s^2+6s+1)\).  It satisfies

\[
\operatorname{rank}R=1,
\qquad
\operatorname{rank}R^2=1.
\]

Hence it is semisimple: one \(-\tfrac12\) Kummer eigenline and a rank-three
zero-residue sector.  Its local monodromy is \(-1\) on the Kummer line and
the identity on the complementary three-plane.

## Support classification

Every pole belongs to the frozen exceptional atlas:

- \(s=0\): the radial/absolute exceptional boundary;
- \(s=1\): the marked endpoint boundary;
- \(s=-1\): the marked \(L_2\)-degeneration;
- \(s^2+6s+1=0\): the marked \(L_1\) square-collision divisor.

The exact overlap homotopies of Entry 1119 are polynomial in \(s\), so they
introduce no additional finite support.

## Hard-to-vary conclusion

\[
\boxed{
\text{The exceptional rank-four connection extends with logarithmic
coefficient residues only on existing carrier divisors.}
}
\]

No new carrier stratum is required at this exceptional center.  The
quadratic Kummer residue is instead a concrete instance of the H2
architecture:

\[
\boxed{
\text{shared carrier and localization calculus}
+\text{ sector-specific Kummer coefficient data}.}
\]

## Scope

This is a characteristic-zero local result on the \((u,v)=(0,2)\)
exceptional family.  It does not establish physical-chain activation,
integral normalization, or global rank-twelve descent.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_u0_v2_exact_quotient_residues.py`.

Divisor-field monodromy checker:

`research/benincasa/checkers/rank12_u0_v2_residue_monodromy_complex.py`.

Result packet with the exact connection and residue matrices:

`research/benincasa/results/rank12-u0-v2-exact-quotient-residues.json`.

Monodromy packet:

`research/benincasa/results/rank12-u0-v2-residue-monodromy-complex.json`.

Ledger claim: `seqclaim-fa720f966fd89412160c4c42`.

Epistemic event:

`ev-000000000821-ff8d907f-1ecd-4dc6-a72e-32b1c43c00bf`.

Divisor-field rank correction:

`ev-000000000823-d98d68ea-4b2c-439c-a4a6-20019db0d86f`.

## Next falsifier

Construct the labelled marked-wall Gysin map onto the quadratic Kummer line.
The canonical local monodromy complex has rank-three kernel and cokernel, so
the finite test is whether the existing collision map selects precisely its
rank-one anti-invariant complement.  Failure to type that map on the frozen
atlas—not a raw rank discrepancy—would reopen the carrier question.
