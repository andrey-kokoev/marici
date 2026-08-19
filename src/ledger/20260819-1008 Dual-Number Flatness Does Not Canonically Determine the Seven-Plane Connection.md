# Dual-Number Flatness Does Not Canonically Determine the Seven-Plane Connection

## The apparent next step is underdetermined

Entries 1003 and 1006 prove that the exact-valuation object

\[
E_2(C)=
\frac{\ker\Lambda\cap\operatorname{im}\Lambda}
     {\ker\Lambda\cap\operatorname{im}\Lambda^2}
\]

has a free rank-seven lift along both coordinate tangent directions of the
triangle wall.  It is tempting to read the two lifts as connection matrices.
That inference is not canonical.

Let

\[
B=k[\tau]/(\tau^2),
\qquad E_B\simeq B^7,
\qquad E_0=E_B/\tau E_B.
\]

A trivialization reducing to the identity on \(E_0\) may be changed by

\[
g=1+\tau H,
\qquad H\in\operatorname{End}_k(E_0).
\]

This preserves the special fiber, freeness, all three mixed-rank censuses,
and the exact-valuation definition.  It changes the first-order transport by
\(H\).  Therefore the set of first-order identifications is a torsor under

\[
\boxed{\operatorname{End}_k(E_0)}.
\]

No connection matrix is selected by dual-number flatness alone.

## Why the fixed presentation does not repair this

The relation presentation has fixed labelled source and ambient monomial
bases, but its differential varies with the external parameters.  For a
representative in the ambient cokernel, remaining inside
\(E_2(C_{X+\tau})\) requires correcting the representative by relations and
choosing a lift through the kernel--image intersections.  Flatness proves
that such corrections exist.  It does not choose one.

Equivalently, if the varying presentation is

\[
d_X:F_X\longrightarrow V_X,
\]

a connection on its cohomology requires chain-level operators satisfying

\[
\partial_i d_X+A_{V,i}d_X-d_XA_{F,i}=0.
\]

The mixed rank packets contain \(d_X\) and \(\partial_i d_X\), but not the
operators \(A_{F,i},A_{V,i}\) or a canonical homotopy producing them.

## Occurrence covariance is insufficient

Let

\[
\sigma:E_{2,12}\overset\sim\longrightarrow E_{2,31}
\]

be Entry 938's source-labelled occurrence map.  Gauge changes remain
occurrence compatible whenever

\[
H_{31}\sigma=\sigma H_{12}.
\]

At minimum, every scalar choice

\[
H_{12}=H_{31}=c\,1
\]

satisfies this condition.  Hence occurrence naturality cannot by itself
select a unique connection.

## Corrected frontier

The next admissible input is not another tangent rank calculation.  It must
be one of the following equivalent source-derived structures:

1. a relative logarithmic de Rham operator on the complete labelled
   presentation, including its external-parameter component;
2. chain-level operators \((A_F,A_V)\) and their homotopy-coherence equation;
3. a crystal/stratification comparison over the first infinitesimal
   neighborhood of the parameter diagonal, with identity and cocycle laws.

Only after such data are constructed may the induced connection on \(E_2\)
be computed and tested for curvature, occurrence covariance, and comparison
with the generic rank-seven algebraic kernel.

Thus Entries 1003 and 1006 remain valid flatness theorems, while the phrase
"derive the connection from the flat family" is superseded by

\[
\boxed{
\text{derive external chain-level transport first, then descend it to }E_2.
}
\]

## Sequence

- allocator claim: `seqclaim-475c4b33170577178a2fbf57`.
