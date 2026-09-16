# The joint source graph makes the chamber--twistor tower analytically equivariant

## Setup

At realization level \(k\), let \(E_k\) be the admitted observer source and let

\[
S_{i,k}:E_k\xrightarrow{\sim}V_{i,k}^{obs},
\qquad i=1,2,3,4,
\]

be the four complete analytic charts:

\[
S_{1,k}=I,
\qquad
S_{2,k}=U_{S,k},
\]

\[
S_{3,k}=(\Omega_{S,k}^+,\Omega_{S,k}^-),
\qquad
S_{4,k}=\mathscr R_k.
\]

Write

\[
R_{i,k}=S_{i,k}^{-1}
\]

on the observer-generated essential image. In particular,

\[
R_{4,k}(B,Q,A,C)=B.
\]

Let

\[
U_k:E_k\to E_{k+1}
\]

be an admitted source successor.

## Presentation edges

Every directed chart edge is

\[
\boxed{
C_{ij,k}=S_{j,k}R_{i,k}.
}
\]

The chart identities imply

\[
C_{jk,k}C_{ij,k}=C_{ik,k}
\]

and all tetrahedral routes are strict.

## Transported successors

Define the successor in the \(i\)-th presentation by conjugation through the source:

\[
\boxed{
T_{i,k}
=S_{i,k+1}U_kR_{i,k}:
V_{i,k}^{obs}	o V_{i,k+1}^{obs}.
}
\]

For the four charts these are:

\[
T_{1,k}=U_k,
\]

\[
T_{2,k}
=U_{S,k+1}U_kC_{21,k},
\]

\[
T_{3,k}
=(\Omega_{S,k+1}^+,\Omega_{S,k+1}^-)
U_kC_{31,k},
\]

\[
T_{4,k}
=\mathscr R_{k+1}U_kC_{41,k}^{resp}.
\]

The fourth formula is the complete-response seam transport. Since \(C_{41}^{resp}\) is the all-seam flux projection, it is continuous in the declared response topology.

## Edge naturality

For every ordered pair \(i\ne j\),

\[
\begin{aligned}
T_{j,k}C_{ij,k}
&=S_{j,k+1}U_kR_{j,k}S_{j,k}R_{i,k}\\
&=S_{j,k+1}U_kR_{i,k},
\end{aligned}
\]

while

\[
\begin{aligned}
C_{ij,k+1}T_{i,k}
&=S_{j,k+1}R_{i,k+1}S_{i,k+1}U_kR_{i,k}\\
&=S_{j,k+1}U_kR_{i,k}.
\end{aligned}
\]

Therefore

\[
\boxed{
T_{j,k}C_{ij,k}
=C_{ij,k+1}T_{i,k}
}
\]

for all twelve directed edges.

This is analytic naturality on the essential-image topologies, not merely a combinatorial square.

## Joint bulk successor

Define the joint bulk

\[
\mathcal B_k
=\left\{
(S_{1,k}g,S_{2,k}g,S_{3,k}g,S_{4,k}g):g\in E_k
\right\}.
\]

Its successor is

\[
\boxed{
\widetilde U_k
(S_{1,k}g,S_{2,k}g,S_{3,k}g,S_{4,k}g)
=
(S_{1,k+1}U_kg,
 S_{2,k+1}U_kg,
 S_{3,k+1}U_kg,
 S_{4,k+1}U_kg).
}
\]

Every coordinate projection intertwines \(\widetilde U_k\) with \(T_{i,k}\).

## Twistor

On the disjoint union of the four chart images define

\[
\tau_k(S_{i,k}g)=S_{i+1,k}g
\]

with indices modulo four. Then

\[
\tau_k^4=I.
\]

Moreover,

\[
\begin{aligned}
T_{i+1,k}\tau_k(S_{i,k}g)
&=S_{i+1,k+1}U_kg,\\
\tau_{k+1}T_{i,k}(S_{i,k}g)
&=S_{i+1,k+1}U_kg.
\end{aligned}
\]

Hence

\[
\boxed{
T_k\tau_k
=	au_{k+1}T_k.
}
\]

## Chamber action

The seven-transition dependency labels

\[
A,J,P,C,T,E,F
\]

record operation order, not presentation index. The twistor changes the chart while retaining the same source datum and completed-operation ideal. Therefore its action on the dependency complex is fiberwise:

\[
\tau_k(i,I)=(i+1,I).
\]

The source successor similarly preserves the labelled ideal:

\[
U_k(i,I)=(i,I)
\]

in the combinatorial coordinate while acting analytically on the realization data.

Consequently every one of the 18 states, 79 edges, 179 triangles, 208 tetrahedra, 121 four-simplices, and 28 maximal five-simplices is transported naturally through the tower and rotated through the four presentation charts.

## Comparison with independently defined successors

Conjugation always defines the transported analytic successor. Equality with a separately defined geometric, spectral, response, or endpoint successor is a source-naturalness statement.

The repository supplies these comparisons at the currently admitted strength:

- signed face and tetrahedral successor naturality in the observer-generated asymptotic category;
- semilocal Hardy--Titchmarsh transport on the compatible spectral image;
- exact complete-response seam transport;
- exact endpoint metric-bundle transport;
- unique natural recovery of \(H_{234}\) by faithful whiskering.

The result does not promote unresolved positive physical Gram or Sonin Green successors.

## Disposition

On the observer-generated signed analytic system, the chamber complex, all twelve directed presentation edges, the order-four twistor, and the realization successor form one strict equivariant tower:

\[
\boxed{
T_{j,k}C_{ij,k}=C_{ij,k+1}T_{i,k},
\qquad
T_k\tau_k=\tau_{k+1}T_k,
\qquad
\tau_k^4=I.
}
\]

The remaining open successor questions belong to positive metric lifts and the Sonin/endpoint Green coupling, not to the signed analytic presentation tower.
