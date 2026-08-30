# 1716 — Nested Zero-Marginal Conditioning Is an Iterated Simplex Blowup

## Falsifier

Entry 1715 left open whether two simultaneously vanishing mixture marginals
glue by ordinary iterated simplex blowups or require an overlap extension.
Freeze the labelled family

\[
\pi_{0k}=\varepsilon\delta s_k,
\qquad
\pi_{1k}=\varepsilon r_k,
\]

with \(S=\sum_k s_k\) and \(R=\sum_k r_k\).

## Exact comparison

Iterated conditioning gives

\[
\frac{\delta S}{R+\delta S}\frac{s_k}{S}
=
\boxed{\frac{\delta s_k}{R+\delta S}},
\]

which is also the direct conditional weight.  The common first normal scale
\(\varepsilon\) cancels exactly.  At \(\delta=0\), ordinary specialization
forgets the vanished row, whereas the exceptional flag retains \([s_k]\).

The overlap transition is multiplication of the outer exceptional coordinate
by the inner projective coordinate.  It is strictly associative and leaves no
residual Čech cocycle.

## Narrow result

\[
\boxed{
\text{nested zero-marginal mixture conditioning is resolved by ordinary
iterated labelled simplex-face blowups.}
}
\]

No extension class and no new Cut carrier stratum occur in this finite model.
The additional information is a flag in the sector-specific mixture
coefficient object.

## Durable artifacts

- `research/benincasa/checkers/nested_simplex_conditioning.rs`
- `research/benincasa/results/nested-simplex-conditioning.json`
- `research/benincasa/nested-simplex-conditioning.md`

## Next falsifier

Test three nested vanishing marginals and two different parenthesizations of
conditioning.  Preserve every label and compare the full exceptional flags;
any nontrivial associator would be the first coefficient-level coherence datum
beyond ordinary simplex blowups.
