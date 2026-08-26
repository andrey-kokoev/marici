# Sector-denominator factorization has an odd exponential gauge

## Obstruction

Suppose a centered completed section has a reflected factorization

\[
F(z)=u(z)D_+(z)D_+(-z),
\]

with nonvanishing normalization (u). The scalar product does not determine
the sector factor (D_+).

For every odd entire function (g), define

\[
\widetilde D_+(z)=e^{g(z)}D_+(z).
\]

Since

\[
g(-z)=-g(z),
\]

the reflected product is unchanged:

\[
\widetilde D_+(z)\widetilde D_+(-z)
=
D_+(z)D_+(-z).
\]

The exponential factor is zero-free, so it also preserves the divisor of
each sector factor.

## Basepoint normalization is insufficient

At the centered basepoint,

\[
g(0)=0.
\]

Therefore

\[
\widetilde D_+(0)=D_+(0).
\]

The full odd-exponential gauge survives normalization at the most natural
source-fixed point. It also preserves every finite collection of centered
even product derivatives that depends only on (F).

Thus neither the functional equation, the sewn scalar product, nor one
basepoint value selects the sector denominator.

## Determinant-line typing

The primary objects should therefore be determinant lines

\[
L_{+,X},\qquad L_{-,X},
\]

with a source-defined sewing map

\[
L_{+,X}\otimes L_{-,X}\longrightarrow L_X.
\]

A scalar determinant is a framed section of one of these lines. The source
must supply the frame or a natural bonding law; it cannot be reconstructed
from the scalar product after sewing.

For cutoffs (X\subset Y), a genuine source determinant must carry a bonding
map compatible with the underlying sector operators. In finite dimensions,
block elimination should give a declared Schur-complement relation of the
form

\[
\frac{D_{+,Y}(z)}{D_{+,X}(z)}
=
\det S_{Y/X}(z),
\]

where (S_{Y/X}) is constructed from the newly added labelled source states.
The quotient is not allowed to be chosen merely to make the completed scalar
identity hold.

## Naturalness gate

The odd-exponential ambiguity is removed only by additional source data such
as:

- a concrete sector operator (M_{+,X});
- a declared determinant functor on its operator ideal;
- natural cutoff bonding or Schur-complement maps;
- a frame transported by those maps;
- boundary counterterms fixed by finite Euler-cutoff reconstruction;
- compatibility with reciprocal reflection before scalar projection.

Accretivity proves that the resulting denominator is zero-free. It does not
select which zero-free framed determinant represents the source.

## Connection to tensor sewing

The two-sector join is not an affine identification of two scalar torsors. It
is a tensor product, and mixed grades can survive before the final scalar
readout. Compressing immediately to (D_+(z)D_+(-z)) erases precisely the
information that could distinguish a source frame from an odd-exponential
refactoring.

This matches the emerging marked-subgraph lesson: commuting local
translations can have a nonzero mixed tensor grade even when their final
compact projection is unchanged.

## Finite falsifier

Given a proposed cutoff family (D_{+,X}), introduce the hostile refactoring

\[
D_{+,X}(z)
\longmapsto
e^{c_X z}D_{+,X}(z).
\]

It preserves reflection sewing and the centered basepoint for every real or
complex coefficient (c_X). If all declared tests remain unchanged, the
proposal has not identified a source determinant; it has identified only a
scalar factorization class.

The first decisive test is therefore whether the cutoff bonding law fixes

\[
c_Y-c_X.
\]

If it does not, arbitrary incoherence can accumulate through completion even
though every finite sewn scalar is exact.

## Consequence

The Hurwitz confinement route remains viable, but its missing input is sharper
than a factorization identity. It requires a source-framed, cutoff-natural
determinant functor. Without that functor, denominator sewing can be fitted
after the fact and carries no authority beyond the completed scalar kernel.
