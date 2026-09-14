# The active relative-boundary restriction has exactly two nondegenerate parity minors

## Question

Does deleting the inactive \(S_{12}\) boundary component from the mined intersection matrix produce a three-dimensional pairing of the same arithmetic type as one elementary conductor factor?

## Claim boundary

This classifies minors of the published matrix. Deleting a row and column is not automatically a cohomological subquotient; connection stability and source authorization remain to be proved.

## Active rows

The relative dual basis rows are

\[
(S_3,S_{12},S_{23},S_{13}).
\]

Since the worked Stokes step has zero \(S_{12}\) coefficient, retain the active rows

\[
(S_3,S_{23},S_{13}).
\]

Starting from

\[
C=
\begin{pmatrix}
0&-1&1&0\\
1&0&0&0\\
1&1&0&1\\
-1&0&1&-1
\end{pmatrix},
\]

delete the \(S_{12}\) row and one canonical-form column.

## Complete minor census

The four determinants, indexed by omitted canonical column, are

\[
(2,0,0,2).
\]

Therefore exactly two omissions yield nondegenerate active pairings.

Omitting column 1 gives

\[
C_{\widehat1}=
\begin{pmatrix}
-1&1&0\\
1&0&1\\
0&1&-1
\end{pmatrix},
\qquad \det C_{\widehat1}=2.
\]

Omitting column 4 gives

\[
C_{\widehat4}=
\begin{pmatrix}
0&-1&1\\
1&1&0\\
-1&0&1
\end{pmatrix},
\qquad \det C_{\widehat4}=2.
\]

Both have Smith invariants

\[
(1,1,2)
\]

and the same unique mod-two cokernel character

\[
(1,1,1),
\]

which tests the parity sum of the active boundary and its two endpoints.

Omitting column 2 or 3 produces determinant zero, so those restrictions cannot provide a full-rank three-dimensional comparison.

## Conductor match

Each elementary conductor factor \(J_i\) also has Smith invariants \((1,1,2)\). Unlike the earlier stabilized comparison, the active relative minors now match the conductor factor dimension directly.

This provides two exact candidate relative matrices for one wallwise parity step. The number two arises from the source matrix rather than from an arbitrary basis enumeration.

## Remaining tests

A legitimate relative subquotient must show that:

1. deleting \(S_{12}\) is induced by the actual Stokes differential, not only by its vanishing coefficient in one calculation;
2. one of canonical columns 1 or 4 is a source-derived complement;
3. the retained three-dimensional space is preserved by the Gauss–Manin connection;
4. an integral basis comparison carries the chosen minor to \(J_i\);
5. site exchange supplies the second wall factor.

## Disposition

The published intersection matrix contains exactly two full-rank active-boundary minors of the required elementary conductor Smith type. They are candidate pairings, not yet admitted relative subquotients.
