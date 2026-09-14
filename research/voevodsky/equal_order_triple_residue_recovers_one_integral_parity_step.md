# The equal-order triple residue recovers one integral parity step

## Question

Does the equal-order normal residue at the triple relative divisor merely match the conductor eigenvalue pattern over characteristic zero, or does it retain the elementary integral parity defect?

## Claim boundary

This computes the integral eigenlattice of a candidate normal residue. Equal vanishing order remains a chosen deformation datum, not a source-authorized nearby-cycle map.

## Equal-order residue

For equal vanishing orders of

\[
X_1-Y,
\qquad X_2+Y,
\qquad X_1+X_2,
\]

the selected relative subconnection has normal residue

\[
R_{\rm eq}=
\begin{pmatrix}
2&0&0\\
-1&1&1\\
1&1&1
\end{pmatrix}.
\]

Its eigenvalues are \(2,2,0\). Primitive integral eigenvectors may be chosen as

\[
e_1=(-1,1,0)^T,
\qquad
e_2=(1,0,1)^T,
\qquad
k=(0,-1,1)^T,
\]

where \(e_1,e_2\) have eigenvalue two and \(k\) has eigenvalue zero.

Let

\[
W=(e_1\ e_2\ k)=
\begin{pmatrix}
-1&1&0\\
1&0&-1\\
0&1&1
\end{pmatrix}.
\]

Then

\[
W^{-1}R_{\rm eq}W=\operatorname{diag}(2,2,0),
\qquad
\det W=-2.
\]

Thus the residue diagonalizes over characteristic zero, but its integral eigenvectors span an index-two sublattice.

## Integral character

The Smith invariants of \(W\) are

\[
(1,1,2).
\]

Its unique mod-two left cokernel character is

\[
(1,1,1),
\]

the same active-boundary-plus-two-endpoints parity carried by the selected relative pairing.

Hence one equal-order nearby residue reproduces not only the spectral shape but also one elementary conductor parity step.

## Relation to the two-wall conductor

One relative residue contributes one index-two eigenlattice defect. The completed conductor has two commuting index-two factors, exchanged by the two wall labels. Therefore a wall-labelled pair of such normal residues has the correct arithmetic architecture for the observed \((\mathbb Z/2)^2\) cone defect.

This is a structural match, not yet a construction: the source must supply two normal deformations, their site exchange, and their compatibility in a single relative totalization.

## Strongest falsification attempt

The residue spectrum alone could have lost the integral defect. It does not: every integral eigenbasis has even determinant because the primitive eigenspaces above generate an index-two lattice. Conversely, this success depends on equal vanishing orders. For general \((m_B,m_C,m_E)\), the nonzero eigenvalues are \(2m_E\) and \(m_B+m_C\), and the equal-Kummer shape need not survive.

## Disposition

Conditional on equal-order transverse specialization, the relative normal residue realizes one elementary parity defect integrally. The remaining authority blocker is the source-derived choice of equal vanishing orders and the construction of two compatible wall-labelled nearby-cycle objects.
