# Double-slit and Gaussian impurity share an exterior-square port

## QND amplitude object

For the exact controlled-pointer double-slit source, arrange the global
amplitudes as a path-by-pointer matrix

\[
M=\frac1{\sqrt2}
\begin{pmatrix}
1&0\\
c&s
\end{pmatrix},
\qquad c^2+s^2=1.
\]

The two occurrence restrictions are

\[
\rho_{\rm path}=MM^\dagger,
\qquad
\rho_{\rm pointer}=M^\dagger M.
\]

They obey strict exterior-square naturality:

\[
\det\rho_{\rm path}
=
\det\rho_{\rm pointer}
=
|\det M|^2
=
\left|\wedge^2M\right|^2.
\]

Thus local mixedness is not an extra cell created by restriction.  It is the
local image of a global relational Plucker coordinate.

## Complementarity identity

For the balanced path restriction,

\[
V=2|\rho_{LR}|=|c|,
\qquad
4\det\rho_{\rm path}=s^2.
\]

The which-path separator gives \(D=|s|\).  Therefore

\[
\boxed{
1-V^2
=D^2
=4\det\rho_{\rm path}
=4|\wedge^2M|^2.
}
\]

The double-slit duality is literally an exterior-square identity.

## Dictionary to Benincasa Entry 2031

Benincasa's resolved pure Gaussian pair has labelled local and cross ports

\[
\det A-\frac14=-\det C.
\]

The exact common operation is not equality of the sector coefficients.  It is
the diagram shape:

\[
\begin{array}{c|c}
\text{double slit}&\text{Gaussian pair}\\
\hline
M&V_{k,-k}\\
MM^\dagger&A_k\\
|\wedge^2M|^2&-\det C_{k,-k}\\
\det(MM^\dagger)&\det A_k-1/4
\end{array}
\]

In both sectors:

1. occurrence restriction commutes with the exterior-square readout;
2. the retained local coefficient is unchanged by forgetting the partner;
3. the discarded cross port explains the local impurity;
4. global purity fixes their relation;
5. no Beck--Chevalley defect or new Carrier cell is required.

The numerical normalization and sign conventions remain sector-specific.
The shared calculus is exterior-square naturality plus a source purity
relation.

## Consequence

This corrects the informal phrase “coherence is destroyed.”  In the admitted
pure interfaces,

\[
\boxed{
\text{local coherence is converted into a global exterior-square relation
and becomes invisible only after the relational port is forgotten.}
}
\]

## Verification

```text
uv run --with sympy python research/nima/checkers/check_double_slit_exterior_square_port.py
```
