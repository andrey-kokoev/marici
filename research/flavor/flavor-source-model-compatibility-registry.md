# Source-model compatibility registry

## Bounded question

Does the currently admitted connector construction define one compatibility-
certified source model from which a complete coupled beta vector field can be
generated without borrowing fitted flavor readout data?

## Admitted model family

The audit is restricted to the relational connector family assembled in
WP483, WP484, the gauged entrance completion, WP492, and WP545. It does not
identify this enlarged experiment with the original full weak-basis quotient.
Its gauge factors are

\[
SU(3)_F\mathbin\times SO(3)_P\mathbin\times SO(3)_E,
\]

where the last factor is present only in the gauged entrance completion.

The largest source-authorized field registry is:

| field | declared source typing | unresolved export typing |
|---|---|---|
| \(S_{\alpha i}\) | real scalar, connector bifundamental of the row and port orthogonal factors | kinetic normalization and threshold state |
| \(X_i\) | scalar \(SU(3)_F\) adjoint and \(SO(3)_P\) vector | kinetic normalization and complete mixed potential |
| \(H^{u,d}_\alpha\) | electroweak-doublet scalar row triplets | hypercharge convention, kinetic normalization, complete two-triplet potential, threshold state |
| \(A^{u,d}_{L,R,\alpha}\) | vectorlike row-vector messenger pairs | exact Standard Model representations, kinetic normalization, threshold map |
| \(B^{u,d}_{L,R,i}\) | vectorlike port-vector messenger pairs | exact Standard Model representations, kinetic normalization, threshold map |

The canonical interaction-shape registry contains separately normalized
\(Y_H^{u,d}\), \(Y_S^{u,d}\), \(Y_X^{u,d}\), \(Z_A^{u,d}\), and
\(Z_B^{u,d}\). The shapes of \(Y_H\), \(Y_X\), and \(Z_B\) are symmetry
forced in the declared grammar. Componentwise \(Y_S\) and identity \(Z_A\)
also require the explicit diagonal-incidence locality axiom. Up and down
shapes may coincide, but their ten scalar normalizations must not be aliased.

## Exact compatibility result

The checker treats every index occurrence as a typed endpoint. The three
renormalizable connector routes close exactly:

\[
\bar QH^{u,d}_\alpha A^{u,d}_{R\alpha},\qquad
\bar A^{u,d}_{L\alpha}S_{\alpha i}B^{u,d}_{Ri},\qquad
\bar B^{u,d}_{Li}X_i q^{u,d}_R.
\]

This proves syntactic compatibility of the declared route grammar, not
closure of the quantum field theory. Four independent export gates fail:

1. exact Standard Model representations are absent for both messenger stages;
2. canonical kinetic normalizations and threshold states are not jointly
   supplied;
3. WP545 proves at least eighteen unresolved running coordinates;
4. no one-scheme finite matching map joins both messenger thresholds to a
   calibrated physical readout.

The smallest closure falsifier is omission of the single connector-adjoint
alignment coupling: parallel and orthogonal configurations have identical
radial data but different gauge counterterms. The checker also deliberately
rejects an up/down normalization alias, deletion of the locality axiom, an
unbound connector index, and a fabricated complete-export flag.

## Disposition

The current source supplies a presentation rigidifier and a syntactically
closed messenger route family. It does not yet supply a source-generated
numerical selector, a complete RG operation on the faithful `physical16`
quotient, or an experimentally calibrated instrument. Beta generation is
therefore refused at the compatibility boundary rather than performed on an
underdeclared truncation.

The next admissible constructor is a source-model export that fills every
registry gap, names all invariant contractions, derives all beta components
and threshold maps in one scheme, and only then tests transversality to the
remaining physical lens direction. Measured-ten or `physical16` coordinates
may validate the resulting readout; they may not fill source-model fields.

## Reproduction

Run:

    python research/flavor/checkers/wp626_source_model_compatibility_registry.py

The generated result is
`research/flavor/results/wp626_source_model_compatibility_registry.json`.

