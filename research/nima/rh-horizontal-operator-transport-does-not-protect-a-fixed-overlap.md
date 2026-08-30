# Horizontal operator transport does not protect a fixed overlap

## Question

Can the fifth-tower repair be obtained by constructing a regular
operator-valued connection and identifying the completed scalar with a vacuum
overlap of its horizontal transport?

The answer is no without an additional incidence theorem.

## Exact polynomial hostile

Let

\[
A=
\begin{pmatrix}
-1&-1\\
1&1
\end{pmatrix}.
\]

Then `A^2=0`. Its normalized horizontal transport is the entire polynomial

\[
U(z)=I+zA
=
\begin{pmatrix}
1-z&-z\\
z&1+z
\end{pmatrix},
\qquad
U'(z)=AU(z).
\]

For every `z`,

\[
\det U(z)=1.
\]

Thus the operator transport is globally invertible, its determinant line is
horizontal, and its determinant section never vanishes.

Take the fixed reference vector and covector

\[
v=e_1,
\qquad
q=e_1^T.
\]

Their fixed-frame overlap is

\[
qU(z)v=1-z,
\]

which vanishes at `z=1`.

The transported state remains nonzero there:

\[
U(1)v=(0,1)^T.
\]

The zero is destructive alignment with the fixed observer, not loss of
invertibility or failure of horizontality.

## Consequence for the proposed C2 proof

A regular operator connection protects:

- the transported full frame;
- its top exterior determinant;
- any covector transported contragrediently with that frame.

It does not protect a projection back onto a fixed reference line. Therefore
the known architecture

\[
U_z\Omega=\Omega_z,
\qquad
\Xi(z)\sim\langle\Omega,\Omega_z\rangle
\]

does not gain zero exclusion merely from a regular horizontal `U_z`.

## Required incidence theorem

The connection route survives only if the actual Evans section is identified
with an internally protected determinant object, rather than an arbitrary
matrix coefficient. At least one of the following must be source-derived:

1. the fixed overlap equals a nonvanishing unit times the determinant of a
   horizontal full frame on each open half-plane;
2. the fixed reference line is invariant under the source connection;
3. the moving line remains uniformly transverse to the fixed observer wall;
4. the overlap is the determinant section of a source complex, together with
   an independently constructed contraction proving acyclicity;
5. a source incidence law couples the fixed observer to the determinant-line
   connection and rejects the polynomial hostile above.

The first option is impossible to assert from scalar equality alone. The
second is stronger than reciprocal transport. The third is the strict observer
gap already isolated. The fourth returns to the Koszul/Fredholm route. The
fifth is the genuinely new fifth-tower constructor.

## DPC

For any horizontal-transport proposal, compute separately:

- the operator determinant;
- the moving-state norm or nonzero status;
- the contragredient moving-observer pairing;
- the fixed-reference overlap;
- the incidence map relating the last quantity to the first three.

Reject if only the first three are controlled. The finite hostile is the
nilpotent connection above: determinant one, entire horizontal transport, and
an exact zero of the fixed overlap.

## Verdict

The operator-valued connection is necessary infrastructure but is not yet the
RH mechanism. The decisive object is the source-derived incidence between its
horizontal determinant data and the fixed Evans observer. Without that
incidence, the fifth tower again protects the wrong quantity.

