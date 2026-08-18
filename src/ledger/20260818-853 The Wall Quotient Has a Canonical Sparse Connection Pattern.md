# 20260818-853 The Wall Quotient Has a Canonical Sparse Connection Pattern

## Question

After Entries 851--852 fix the localization maps and block variance, does the existing four-stratum exact-reduction system determine any part of the wall quotient connection independently of its large primitive nullspace?

## Audit

Use the source-normalized quotient basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110})
\]

and the generic source geometry already frozen in the marked-relative reduction engine.  For each of three generic kinematic samples and both base derivatives, reduce the derivatives of all twelve classes while retaining every primitive exact variable.

The fixed-coordinate mask is unchanged:

\[
3847=2^0+2^1+2^2+2^8+2^9+2^{10}+2^{11}.
\]

In particular, all first three output coordinates are fixed for every differentiated marked class, despite the remaining primitive nullspace.

## Result

For both base directions the induced quotient matrix has the common pattern

\[
\boxed{
A_{3,\mu}=
\begin{pmatrix}
\alpha_\mu&0&0\\
\beta_\mu&\gamma_\mu&0\\
\delta_\mu&0&\varepsilon_\mu
\end{pmatrix}.
}
\]

The nine absolute columns have zero wall coordinates, as required by Entry 852.  The two primitive wall lines do not mix with one another.  Only the top class can feed both primitive wall lines.

This pattern was reproduced at

\[
(u,v)=(7,11),(13,19),(23,29)
\]

over

\[
\mathbb F_{2305843009213693951}
\]

for both \(\partial_u\) and \(\partial_v\).

## Scope

This is stronger than a sparsity-selected rank-twelve solution: these coordinates are invariant across the complete primitive exact-lift nullspace of the frozen reduction problem.

It is not yet a characteristic-zero formula for \(A_3\), and the sample table must not be rationally fitted.  The next calculation remains an independent one-dimensional wall-Laurent reduction deriving

\[
\alpha_\mu,\beta_\mu,\gamma_\mu,\delta_\mu,\varepsilon_\mu
\]

from the oriented residue forms.  The matrices in the durable packet are reconstruction checks only.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`
- `research/benincasa/marked-wall-quotient-samples.json`
- Epistemic event `ev-000000000468-d59651f0-bc82-4590-b89d-eeb8e53d113a`
