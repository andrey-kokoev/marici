# 1657 — Quantum Cut Coproduct Must Precede Fixed-\(\hbar\) Specialization

## Quantum typing test

Entry 1656 closes the commutative/associated-grade co-Leibniz coherence. Restore the Weyl relation

\[
[q,p]=i\hbar\,1
\]

and test whether the primitive Cut/cumulant coproduct descends after fixing \(\hbar\) as one global scalar.

## Fixed-parameter failure

Set

\[
\Delta q=q\otimes1+1\otimes q,
\qquad
\Delta p=p\otimes1+1\otimes p.
\]

Then

\[
[\Delta q,\Delta p]
=
[q,p]\otimes1+1\otimes[q,p]
=
2i\hbar\,1\otimes1.
\]

But fixed scalar specialization gives

\[
\Delta(i\hbar\,1)
=
i\hbar\,1\otimes1.
\]

Thus the defining Weyl ideal acquires the residual

\[
\boxed{i\hbar\,1\otimes1}
\]

and is not preserved.

For \(N\) labelled occurrences, the residual is \((N-1)i\hbar\). The checker verifies all \(N=2,\ldots,128\).

## Homogenized repair

Before scalar specialization, promote the central quantum parameter to a primitive labelled generator:

\[
\boxed{
\Delta\hbar=\hbar\otimes1+1\otimes\hbar.
}
\]

Then

\[
[\Delta q,\Delta p]=i\,\Delta\hbar,
\]

and the relation descends exactly.

## Narrow result

\[
\boxed{
\text{The quantum Cut/cumulant coproduct must be constructed in the homogenized occurrence-resolved CCR algebra before fixed-\(\hbar\) specialization.}
}
\]

This repeats a central Marici pattern:

\[
\text{linear resolved datum}
\to
\text{coarse diagonal invariant}.
\]

The obstruction is not a new interaction or carrier cell. It is a type error caused by imposing the physical scalar parameter before occurrence-resolved sewing.

This does not yet prove that the homogenized coproduct and interaction co-Leibniz cocycle descend compatibly after the physical diagonal/normalization quotient.

## Durable artifacts

- research/benincasa/checkers/weyl_coproduct_hbar_typing.rs
- research/benincasa/results/weyl-coproduct-hbar-typing.json
- research/benincasa/weyl-coproduct-hbar-typing.md

## Next falsifier

Compute \(\Theta_D\) in the homogenized CCR algebra with primitive \(\hbar\), including normal ordering. Test its co-Hochschild identity before specialization, then determine the correctly normalized physical diagonal map. A surviving central term after the typed specialization would be the first genuine quantum coefficient correction.
