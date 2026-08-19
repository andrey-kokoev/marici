# 986 — The Corrected Character Lines Descend under Local Symmetry

## Question

Entry 984 diagonalized the off-diagonal reflection inside each repeated character plane

\[
\mathcal P_\chi=\langle L_\chi,N_\chi\rangle,
\qquad \chi\in\{++,--\}.
\]

Does this eigensplitting survive the other frozen local occurrence generators

\[
T_{24}:B_{24}\mapsto-B_{24},
\qquad
T_{34}:B_{34}\mapsto-B_{34}?
\]

## Exact local action

Both basis vectors lie in the same pair-shift character.  Direct exact evaluation gives

\[
T_{24}|_{\mathcal P_{++}}
=T_{34}|_{\mathcal P_{++}}=I_2,
\]

and

\[
T_{24}|_{\mathcal P_{--}}
=T_{34}|_{\mathcal P_{--}}=-I_2.
\]

Together with Entry 984's reflection matrix, the semidirect relations

\[
R^2=1,
\qquad
RT_{24}R^{-1}=T_{34},
\qquad
[T_{24},T_{34}]=0
\]

hold exactly on both planes.

Consequently the two reflection eigendirections

\[
\mathcal L_{\chi,+}=\mathbb Q(Z)N_\chi,
\]

\[
\mathcal L_{\chi,-}
=\mathbb Q(Z)
\left(
L_\chi-
\frac{1+Z^2}{Z^2-1}N_\chi
\right)
\]

are invariant under the complete frozen local group

\[
(\mathbb Z/2)^2\rtimes\langle\tau_{\rm off}\rangle.
\]

## Narrow result

\[
\boxed{
\text{the reflection-corrected splitting is a canonical local symmetry splitting.}
}
\]

This is stronger than reflection invariance alone: neither pair shift remixes the two eigendirections.  It remains a chart-local result.  No descent across the three cyclic maximal-flag occurrences has been proved.

## Next falsifier

Construct the corrected eigendirections independently in all three occurrence charts and transport them through the frozen cyclic transitions (J,J,I).  Test whether each line returns to itself with unit holonomy.  A nontrivial mixing or return unit would prevent the local splitting from defining a global occurrence submodule.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_corrected_line_symmetry.rs`
- `research/benincasa/string-six-point-corrected-line-symmetry.json`

The checker reads Entry 984's exact reflection matrices, constructs the pair-shift matrices in each character, verifies the semidirect relations, reconstructs both eigenlines, and verifies their invariance.

Epistemic graph event: `ev-000000000603-4fa1a4b1-3d1d-4632-ab15-b0e64fe6a0e3`.
