# 1651 — Independent Gaussian Cut Coherences Satisfy the Nested Cocycle

## Higher-coherence test

Entry 1650 derives the first Cut/evolution coherence

\[
H_i=C_iD-D_{\widehat i}C_i.
\]

Test whether two internal Gaussian pushforwards leave a secondary associativity obstruction.

## Labelled test

Use internal occurrences \(3,4\),

\[
H_{\rm int}=q_1q_3q_4,
\qquad
f=p_1q_3q_4.
\]

Then

\[
Df=-q_3^2q_4^2+p_1p_3q_4+p_1q_3p_4.
\]

For independent centered Gaussian Cut states with variances \(\nu_3,\nu_4\),

\[
C_3C_4(Df)=-\nu_3\nu_4,
\qquad
D_{\rm obs}(C_3C_4f)=0.
\]

## Cocycle identity

The composite commutator telescopes:

\[
\boxed{
H_{34}
=
C_3H_4+H_3C_4.
}
\]

On the test observable,

\[
H_4(f)=-\nu_4q_3^2,
\qquad
C_3H_4(f)=-\nu_3\nu_4,
\qquad
H_3C_4(f)=0.
\]

Reversing the order gives

\[
C_4H_3(f)+H_4C_3(f)=-\nu_4\nu_3.
\]

The checker verifies 1,024 cocycle identities and 1,024 Cut-order identities.

## Narrow result

\[
\boxed{
\text{The first Wick coherence is associative and order-independent for independent Gaussian Cuts.}
}
\]

No secondary obstruction appears in this finite sector. The non-strict Cut/evolution comparison of Entry 1650 is therefore controlled by a coherent lax structure rather than an arbitrary defect.

This supports the shared-calculus hypothesis: existing Cut incidence plus coefficient pushforward generates the required coherence.

The result is restricted to independent Gaussian internal coefficient states. Correlated Cut states need a joint pushforward and may not factor into commuting one-occurrence contractions.

## Durable artifacts

- research/benincasa/checkers/nested_cut_wick_cocycle.rs
- research/benincasa/results/nested-cut-wick-cocycle.json
- research/benincasa/nested-cut-wick-cocycle.md

## Next falsifier

Repeat the nested comparison for a correlated two-occurrence Gaussian state. Freeze the joint covariance and compare direct joint pushforward with both sequential conditional contractions. Determine whether their discrepancy is explained by the existing correlation/process-tensor coefficient object or produces a genuine higher coherence class.
