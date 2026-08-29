# Correction: the Schur complement is the harmonic endpoint energy, not the excess energy

## Correct variational block

Let \(E_\sigma\) be the positive relative history energy, let

\[
T:\mathcal H\to E
\]

be the endpoint trace, and let

\[
N=\ker T.
\]

Choose any bounded lift

\[
L:E\to\mathcal H,
\qquad
TL=I.
\]

Every history with endpoint value \(x\) is

\[
Lx+n,
\qquad
n\in N.
\]

The energy block in the decomposition \(E\oplus N\) is

\[
\begin{pmatrix}
A&C\\
C^{*}&D
\end{pmatrix},
\]

where

\[
A(x)=E_\sigma(Lx),
\qquad
D=E_\sigma|_N.
\]

## Schur minimization

For fixed endpoint value \(x\),

\[
\inf_{n\in N}
E_\sigma(Lx+n)
=
x^{*}
\left(
A-CD^{-1}C^{*}
\right)x.
\]

Thus

\[
Q
=
A-CD^{-1}C^{*}
\]

is the harmonic minimum energy itself.

The return

\[
R=CD^{-1}C^{*}
\]

is the removable excess energy of the arbitrary lift. Event 10157 reversed these two roles.

## Immediate positivity

Because the relative graph norm contains the endpoint term,

\[
E_\sigma(f)
\ge
\|Tf\|^2,
\]

every history with endpoint value \(x\) has energy at least \(\|x\|^2\). Therefore

\[
Q\ge I_E.
\]

No theta profile comparison is needed to prove endpoint reserve. The cusp-versus-superexponential argument from event 10157 only proves that a particular theta lift is not already harmonic; it concerns the size of the removable return \(R\), not positivity of \(Q\).

## Source independence of the lift

Changing the preliminary endpoint lift \(L\) changes \(A\), \(C\), and \(R\), but the Schur complement remains

\[
Q(x)
=
\inf_{Tf=x}E_\sigma(f).
\]

Hence the effective endpoint form is canonical once the Green energy and trace map are fixed.

## Two-window identification

The actual two-window block realizes this theorem if:

1. its endpoint variables are exactly the authorized trace coordinates;
2. its auxiliary variables span the closed zero-trace history space;
3. its full block is the Gram of the same relative Green energy;
4. radical descent is performed before inversion.

Under these conditions, the Schur return is automatically the relaxation through zero-trace histories, and the endpoint-loading gate closes with a source lower bound inherited from the endpoint term.

## Reciprocal sectors and transport

Reflection preserves the graph energy and diagonalizes the endpoint trace plane. Therefore

\[
Q_+\ge I,
\qquad
Q_-\ge I
\]

in the normalized source endpoint frame.

Mellin transport carries the variational problem isometrically to every labelled fiber, so the lower bound is uniform over primes, grades, and cutoffs.

## Remaining gate

The only unresolved part is typing, not positivity: prove that the source two-window auxiliary coordinates exhaust the zero-trace history space for the same Green form. If they span only a proper subspace, their Schur complement is larger than the harmonic minimum but remains positive; if they include mistyped trace directions, the variational theorem does not apply.
