# Acyclic-tail Schur self-energy: Lean packet

Source: `research/grothendieck/acyclic-tail-schur-self-energy-mechanism.md`.

The formal coefficient type is an arbitrary field `K`. The finite model has
one physical scalar channel, one even auxiliary scalar channel, and an
identical odd auxiliary determinant used as the graded denominator. For
physical entry `p`, auxiliary entry `a`, and left/right couplings `c,d`, Lean
defines

\[
M=\begin{pmatrix}p&c\\d&a\end{pmatrix},\qquad
\operatorname{sdet}(M)=\frac{\det M}{a},\qquad
\Sigma=c a^{-1}d.
\]

Under the explicit assumption `a ≠ 0`, `scalarGradedDeterminant_eq_schur`
proves

\[
\operatorname{sdet}(M)=p-\Sigma.
\]

`uncoupled_scalarGradedDeterminant` proves cancellation of identical even and
odd auxiliary factors when `c=d=0`. `scalarCoupling_defect` proves that the
difference between coupled and uncoupled effective channels is exactly
`-Σ`. The rational hostile at `p=0`, `a=c=d=1` has graded determinant `-1`,
whereas removing the coupling gives `0`; thus zero net auxiliary multiplicity
does not erase the coupling.

This is a finite scalar identity only. The source packet's matrix/operator
version still needs finite-dimensional block determinant typing (or a Schur
complement API), and its intended infinite version needs closed operator
domains, resolvents, determinant class or relative determinant, an actual
acyclic coefficient–Betti complex, and a source-derived coupling. Equality of
even/odd multiplicities alone does not construct that complex or authorize
ghost modes.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans are run, and this module remains outside
`MariciFormal.lean`.
