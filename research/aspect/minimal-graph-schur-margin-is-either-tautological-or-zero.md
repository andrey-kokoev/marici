# The minimal graph Schur margin is either tautological or zero

## Question

Does the source-forced arithmetic–analytic graph coupling retain a nontrivial uniform margin after the arithmetic identity factor is removed?

## Minimal graph form

Let \(U:V\to H\) be weighted theta synthesis. The minimal graph energy retaining arithmetic provenance and enforcing analytic matching is

\[
Q(v,h)=\|v\|^2+\|Uv-h\|^2.
\]

Its block operator is

\[
M=
\begin{pmatrix}
I+U^*U&-U^*\\
-U&I
\end{pmatrix}.
\]

The Schur complement of the analytic identity block is exactly

\[
I+U^*U-U^*U=I.
\]

Thus the arithmetic lower margin is supplied entirely by copying \(v\). It contains no theta spectral information.

## Remove the tautological channel

After removing the provenance term \(\|v\|^2\), the remaining matching energy is

\[
Q_{\rm match}(v,h)=\|Uv-h\|^2
\]

with block

\[
M_{\rm match}=
\begin{pmatrix}
U^*U&-U^*\\
-U&I
\end{pmatrix}.
\]

Every graph vector \((v,Uv)\) is an exact null vector:

\[
Q_{\rm match}(v,Uv)=0.
\]

Therefore the matching residual alone is not confining. Its vanishing means that arithmetic and analytic presentations agree; it does not imply that the represented arithmetic state vanishes.

## Singular-mode audit

On a singular mode \(Uv=sv\),

\[
M_s=
\begin{pmatrix}
1+s^2&-s\\
-s&1
\end{pmatrix},
\qquad
\det M_s=1.
\]

Without the identity term,

\[
M_{s,\rm match}=
\begin{pmatrix}
s^2&-s\\
-s&1
\end{pmatrix},
\qquad
\det M_{s,\rm match}=0.
\]

This dichotomy is independent of whether \(s\) tends to zero: the full determinant is a tautological unit, while the nontrivial matching block is singular on the entire synthesis graph.

## Consequence

The minimal source-forced graph architecture does not transfer a nontrivial uniform confinement margin into the residual Schur complement. To obtain an RH- or scalar-null-bearing determinant, one needs an additional source-authorized operator acting nontrivially along graph directions. It must not be a fitted mass term, a copied identity, or bounded postprocessing of compact theta synthesis.

## Verification

`research/aspect/checkers/check_minimal_graph_schur_margin.py` verifies the determinant, both Schur complements, and exact graph nulls for rational singular modes.

## Disposition

The strong Deutschian conjecture fails for the minimal graph coupling: the identity channel gives only tautological strength, and removing it leaves exact graph nulls. The next question is whether any independently sourced arithmetic operator couples to graph directions; absent such an operator, strong scalar-null confinement must be withdrawn.
