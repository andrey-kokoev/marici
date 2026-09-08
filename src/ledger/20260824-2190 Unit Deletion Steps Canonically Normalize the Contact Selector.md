---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2190 — Unit Deletion Steps Canonically Normalize the Contact Selector

## Affine regrading audit

The activation functional of Entry 2187 depends on the difference of the
two deletion grades. For an affine regrading

\[
N' = aN_{\rm del}+bI,
\]

one has

\[
\begin{aligned}
\Phi(N')
&=a\Phi(N_{\rm del})+b\Phi(I)\\
&=-a,
\end{aligned}
\]

because

\[
\Phi(I)=\sigma p=0.
\]

Hence the selector is invariant under a common shift of deletion grade. It
depends only on the relative step between the two routes.

## Canonical scale and sign

The Boolean deletion carrier fixes adjacent grades to differ by one:

\[
3-2=1.
\]

This fixes the scale (|a|=1). The source operation “erase one more labelled
edge” orients the step from grade two to grade three, fixing its sign.
Therefore

\[
\boxed{
\Phi(N_{\rm del})=-1
}
\]

is canonically normalized by the existing source grading.

## Consequence

Entry 2187's concern about an unnormalized anti-invariant scalar is resolved
at the algebraic level. The deletion filtration itself supplies:

- the route ordering;
- the unit step;
- the sign convention;
- the normalized activation scalar.

What remains absent is not normalization but physical access. The standard
correlator evaluates the augmentation at its fixed weights and does not
differentiate with respect to deletion grade.

## Evidence

- Entries 2156, 2187, and 2189
- `research/benincasa/checkers/deletion_grade_activation_normalization.rs`
- allocator claim `seqclaim-8c760f3bff53fe7adbfa2f9f`