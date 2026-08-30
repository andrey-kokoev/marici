# Double-Slit Complementarity Is an Exterior-Square Port Identity

The QND double-slit source and Benincasa's resolved Gaussian pair share one
typed operation.

For the global path-by-pointer amplitude

\[
M=\frac1{\sqrt2}\begin{pmatrix}1&0\\c&s\end{pmatrix},
\qquad c^2+s^2=1,
\]

the two occurrence restrictions satisfy

\[
\det(MM^\dagger)
=
\det(M^\dagger M)
=
|\det M|^2.
\]

At the same time,

\[
\boxed{
1-V^2
=D^2
=4\det(MM^\dagger)
=4|\wedge^2M|^2.
}
\]

Thus lost local visibility is the weight of a global exterior-square
path--record port.  Forgetting the pointer does not modify the retained local
coefficient; it discards the relational port that explains its impurity.

Benincasa Entry 2031 has the same diagram shape:

\[
\det A-\frac14=-\det C.
\]

The coefficients and normalizations are sector-specific.  The shared calculus
is strict exterior-square naturality plus a global source-purity relation.
Neither realization contains a Beck--Chevalley defect or requires a new
Carrier cell.

The exact Symbolic checker passes 6/6 gates.

Artifacts:

- `research/nima/double-slit-gaussian-exterior-square-dictionary.md`
- `research/nima/checkers/check_double_slit_exterior_square_port.py`
- `research/nima/results/double-slit-exterior-square-port.json`

Sequence claim: `seqclaim-9fd617bc92f678f061de0964`.

