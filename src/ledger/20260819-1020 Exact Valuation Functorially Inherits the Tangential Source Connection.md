# Exact Valuation Functorially Inherits the Tangential Source Connection

## Setup

Entry 1018 proves that the unbounded labelled source calculus carries the
exact external connection.  Let its normal parameter at the triangle wall be

\[
\Lambda=X_3-X_1-X_2.
\]

The two coordinate wall tangents are

\[
T_1=\partial_{X_1}+\partial_{X_3},
\qquad
T_2=\partial_{X_2}+\partial_{X_3}.
\]

They satisfy

\[
T_1(\Lambda)=T_2(\Lambda)=0.
\]

Consequently the exact source connection is \(k[\Lambda]\)-linear in each
tangential direction:

\[
[\nabla_{T_i},\Lambda]=0.
\]

## Descent to exact valuation

For any \(k[\Lambda]\)-module with such a connection, define

\[
E_2(C)=
\frac{\ker\Lambda\cap\operatorname{im}\Lambda}
     {\ker\Lambda\cap\operatorname{im}\Lambda^2}.
\]

Every term is connection-stable.  Indeed,

\[
\Lambda x=0
\Longrightarrow
\Lambda\nabla_Tx=\nabla_T(\Lambda x)=0,
\]

while

\[
x=\Lambda^j y
\Longrightarrow
\nabla_Tx=\Lambda^j\nabla_Ty
\qquad(j=1,2).
\]

Therefore both intersections are preserved, and the quotient inherits a
canonical induced connection:

\[
\boxed{
\nabla_T:E_2(C)\longrightarrow E_2(C).
}
\]

No splitting, pivot basis, or elimination witness enters this construction.
The endomorphism torsor of Entry 1008 disappears because the connection is
now descended from the full source complex rather than inferred from a flat
dual-number family.

## Compatibility with the direct limit

The unbounded calculus is the filtered colimit of finite pole/degree windows
with their inclusion maps.  In modules, filtered colimits are exact and
commute with finite intersections of submodules.  Hence

\[
E_2\!\left(\varinjlim C_N\right)
\simeq
\varinjlim E_2(C_N)
\]

provided the transition maps are the genuine source inclusions rather than
post hoc quotient projections.  The induced tangential connection is the
colimit of the compatible source connections.

Thus the connection-existence problem is solved abstractly at the correct
typing level.

## Remaining finite-rank gate

What is not yet proved is

\[
\dim E_2\!\left(\varinjlim C_N\right)=7.
\]

Entries 938, 952, 1003, and 1006 establish rank seven and first-order
flatness in the pole-depth-two presentation, with cutoff replication in
ambient degrees ten and eleven.  They do not establish stabilization under
increasing pole depth.

The next decisive computation is therefore narrow:

1. construct nested pole-depth windows with honest inclusion maps;
2. compute the induced maps on \(E_2\), not only their dimensions;
3. test whether the depth-two seven-plane maps isomorphically into the next
   connection-stable window;
4. only then extract connection matrices or compare with the generic
   rank-seven algebraic kernel.

The frontier is now

\[
\boxed{
\text{canonical connection exists on direct-limit }E_2;
\quad
\text{finite rank seven still requires pole-depth stabilization.}
}
\]

## Sequence

- allocator claim: `seqclaim-a320472fc5fa973b2d444190`.
