# Three-cell Adams defect: Lean packet

Source: `research/grothendieck/three-cell-adams-defect-positivity-theorem.md`.

For complex consecutive correlations `a`, `b` and direct correlation `c`,
`threeCellGramDeterminant` is the real determinant expression

\[
1-|a|^2-|b|^2-|c|^2+2\operatorname{Re}(ab\overline c),
\]

where squared moduli are represented by `Complex.normSq`.

`threeCellGramMatrix` is the actual `Fin 3` Hermitian matrix from the source.
`threeCellGramMatrix_isHermitian` proves its adjoint symmetry and
`threeCellGramMatrix_det` proves that its matrix determinant is exactly the
complex coercion of `threeCellGramDeterminant`.

`threeCellGramDeterminant_defect_identity` proves

\[
\det G=(1-|a|^2)(1-|b|^2)-|c-ab|^2.
\]

`threeCellGramDeterminant_nonnegative_iff` proves the exact defect inequality.
The exact Adams branch `c=a*b` has zero defect, and its determinant is
nonnegative whenever both consecutive edges are contractions.

`threeCell_uncontrolled_direct_edge_hostile` takes `a=b=1/2`, `c=-1`:
the consecutive edge contractions hold but the determinant is negative. Thus
separate edge bounds do not authorize an arbitrary direct prime-power edge.

Typing boundary: correlations are complex scalars, the matrix is complex
Hermitian, and its determinant value is proved real. A full matrix PSD
statement additionally needs the `Fin 3` Hermitian principal-minor criterion,
which Mathlib does not currently expose as a directly reusable theorem. The
operator-valued formula `C=AB+D_(A*) K D_B` requires ordered defect operators,
domains, and a contraction norm; it is not obtained by commuting blocks. The
prime--gamma source values `a_2,c_4` remain missing convention-fixed inputs.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans were run; the module remains outside
`MariciFormal.lean`.
