# 2683 — The Rank-Twenty-Six Leray Covector Is a Finite Source-Jet Tomography Problem

## Frozen inputs

The generic marked-relative quotient has rank \(26\). The source-word construction retains raw primitive representatives rooted at

\[
S,qquad D_0,qquad D_1,
\]

where \(S\) is the literal source and \(D_0,D_1\) are its two declared first-derivative roots. Breadth-first Gauss–Manin words are admitted only when independent in the quotient.

The physical local Leray germ, its sheet, orientation, and multiplicity are independently fixed by the negative-imaginary boundary value and positive Cayley–Menger chain.

## Finite tomography result

The frozen packet contains exactly \(26\) primitive source words, of maximum connection depth three. Their rank is \(26\) at the reference point and at both independent control points.

Therefore any dual covector on the generic rank-twenty-six module is uniquely determined by its evaluations on these words.

For the physical covector, those evaluations are the corresponding source-normalized Leray period jets. Thus the missing covector is not a free projector, complement, or basis choice. It is a finite evaluation problem:

\[
\ell_{\rm phys}
\longleftrightarrow
\bigl(
\ell_{\rm phys}(w_1),\ldots,
\ell_{\rm phys}(w_{26})
\bigr).
\]

## Narrow result

Selection is settled generically: the source period germ determines at most one covector compatible with all 26 jets. Computation remains open because the characteristic-zero period jets and their integral normalization have not been evaluated in this basis.

This theorem is finite-field generic tomography. It does not establish continuation through discriminant support and does not assign any new role to \(\mathcal Q\).

## Artifacts

- `research/benincasa/check_rank26_leray_covector_tomography.py`
- `research/benincasa/rank26-leray-covector-tomography.json`
- `research/benincasa/rank26-source-word-basis.json`
- `research/benincasa/published_boundary_value_leray_uniqueness.md`

## Next falsifier

Evaluate a bounded initial subset of the 26 source-period jets directly from the source Leray integral and test the Gauss–Manin recurrence against the primitive word packet. If the recurrence fails, the finite-field source-word basis does not lift to the physical characteristic-zero period system. If it passes, extend until all 26 values reconstruct the covector.
