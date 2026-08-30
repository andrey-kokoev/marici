# The Euler endpoint coboundary has a canonical bordered determinant lift

## Coboundary state

Fix a finite prime cutoff \(X\) and grade cutoff \(K\), and set

\[
H_{X,K}
=
\sum_{p\le X}\sum_{1\le k\le K}
\frac1k p^{-k/2}S_{k\log p}.
\]

To keep notation light, write \(H_X\) for this finite polynomial throughout the finite bordered construction. Removing the suppressed grade cutoff requires the separate Fredholm and completion gates stated below. Let \(\varepsilon\) be translation augmentation.

For a source state \(G\), define the relative Euler state

\[
u_X(G)
=
\left(
H_X-\varepsilon(H_X)I
\right)G.
\]

Endpoint evaluation gives

\[
E_0u_X(G)
=
E_0(H_XG)-\varepsilon(H_X)E_0(G).
\]

Therefore

\[
E_0u_X(G)
=
J_X(G),
\]

where \(J_X(G)\) is the complete weighted prime-power endpoint current.

This state is constructed before scalar readout. It retains the primitive,
square, and connected translation components in one relative vector.

## Bordered determinant

On the finite source carrier \(V_X\), define

\[
D_X(G)
=
\begin{pmatrix}
I_{V_X} & u_X(G)\\
E_0 & 0
\end{pmatrix}.
\]

The Schur-complement identity gives

\[
\det D_X(G)
=
-E_0u_X(G)
=
-J_X(G).
\]

Thus the Euler endpoint current has a canonical determinant-line lift. It is
not obtained by fitting an operator whose ordinary trace equals the current.
It is obtained by bordering the source-derived coboundary state with its
source-derived endpoint observer.

## Exact zero-to-state bridge

If \(J_X(G)=0\), then

\[
D_X(G)
\binom{-u_X(G)}{1}
=
0.
\]

Conversely, a nonzero kernel of \(D_X(G)\) forces \(J_X(G)=0\). Hence the
finite endpoint zero is exactly the cohomology locus of the bordered
two-term complex

\[
0
\longrightarrow
V_X\oplus\mathbb C
\xrightarrow{D_X(G)}
V_X\oplus\mathbb C
\longrightarrow
0.
\]

The kernel generator is forward-derived from \(H_X\), \(G\), and \(E_0\). No
division by \(J_X\) and no prior zero set are used.

## Grade filtration inside the border

Write

\[
u_X
=
u_X^{(1)}+u_X^{(2)}+u_X^{(\ge3)}
\]

using the homogeneous split of \(H_X\). Then

\[
E_0u_X^{(1)}=J_X^{(1)},
\qquad
E_0u_X^{(2)}=J_X^{(2)},
\qquad
E_0u_X^{(\ge3)}=J_X^{(\ge3)}.
\]

The border therefore carries all three grades as typed columns before their
scalar sum. A source-valid completion must retain this filtration rather than
replace the column by the already aggregated number \(J_X\).

The third-order determinant normalization applies to the internal
translation packet; the bordered determinant applies the endpoint evaluation
wall. They are different determinant operations and must remain ordered.

## Groupoid naturality

For a translated base state \(S_aG\), the coboundary state changes with the
groupoid object. The endpoint cocycle gives a canonical comparison between
the borders based at \(G\) and \(S_aG\).

For two staged translations, the relative columns satisfy the transported
sum law inherited from

\[
b_G(a+b)
=
b_G(a)+b_{S_aG}(b).
\]

Consequently, the scalar bordered determinants agree along the two paths of a
commuting prime square, while their intermediate columns retain the correct
translated source states.

This is the finite determinant realization of the groupoid cocycle.

## Stable reduction and its meaning

In unrestricted finite-dimensional linear algebra, triangular maps reduce

\[
D_X(G)
\]

to

\[
I_{V_X}\oplus\bigl(-J_X(G)\bigr).
\]

Therefore the border does not prove nonvanishing. It gives an exact
zero-to-state bridge and nothing more at finite cutoff.

The construction becomes analytically informative only if the triangular
elimination fails to descend through the typed completion. The possible
failures are now concrete:

- \(u_X^{(1)}\) has no ordinary completed column;
- \(u_X^{(2)}\) has only anomaly-line completion;
- \(E_0\) is unbounded on the completed connected carrier;
- the seam interval changes the observer domain;
- reciprocal sewing does not preserve the border;
- the Gaussian Mellin trivialization does not extend to the same rigging.

The first failed triangular map is the boundary invariant. An unspecified
failure of scalar elimination is not enough.

## Relation to the zero sieve

Let \(F(w)\) be a source action on the completed bordered carrier. A line
semi-invariance law

\[
\det D(F(w)G)
=
\lambda_w\det D(G)
\]

with \(\lambda_w\ne0\) propagates bordered cohomology and therefore endpoint
zeros through the action word.

At finite cutoff, Adams and Gaussian dilation provide candidate characters.
The missing statement is that the bordered columns and observer transform
naturally, not merely that their scalar determinants have the expected ratio.

This moves the zero-sieve test one level before evaluation:

\[
D(F(w)G)
\quad\text{must be compared to}\quad
D(G)
\]

by admitted row and column transport.

## Relation to the completed \(\Xi\) bridge

The finite identity is

\[
\det D_X(G)=-J_X(G),
\]

not \(\Xi\). A categorical RH bridge still requires a completed bordered
operator \(D(s)\) whose determinant line is identified with

\[
u(s)\Xi(s)
\]

for a source-derived invertible section \(u(s)\).

That identification must arise from the same theta/Tate source and boundary
completion. Installing \(\Xi\) as the lower-right scalar block would be
circular.

## Smallest finite tests

1. Compute \(u_X(G)\) directly from the logarithmic translation operator.
2. Verify \(E_0u_X(G)=J_X(G)\) grade by grade.
3. Verify \(\det D_X(G)=-J_X(G)\).
4. At \(J_X(G)=0\), verify the kernel vector \((-u_X(G),1)\).
5. For two prime orders, compare transported bordered columns, not only final
   determinants.
6. Confirm that no inverse or contraction uses \(J_X(G)^{-1}\).

## Consequence for categorical RH

The relative determinant representation requested at the previous rung exists
at finite cutoff as a canonical bordered determinant. It connects the common
logarithmic Euler operator to an exact zero-to-state complex while preserving
the three-grade column.

The unresolved RH-bearing step is no longer the existence of a finite
determinant lift. It is the typed completion of that border and a noncircular
open-sector contraction or behavioral monicity theorem for the resulting
complex.

## Verdict

The Euler endpoint coboundary has a canonical bordered determinant lift. Its
finite determinant is exactly the endpoint current, and its kernel is the
forward-derived relative Euler state. This completes the finite
operator-to-zero bridge but deliberately leaves nonvanishing, completion, and
identification with \(\Xi\) open.
