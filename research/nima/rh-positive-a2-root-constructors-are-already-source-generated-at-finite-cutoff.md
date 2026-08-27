# Positive A2 root constructors are already source-generated at finite cutoff

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite constructor theorem; common rigged-domain gate remains

## Correction

The full (SL(3)) connection requires the missing reverse wall incidence.
The positive type-(A_2) exchange atlas does not.

At finite cutoff, its two simple positive-root constructors can already be
generated from three existing source operations:

- the product-rule jet shear;
- the Fourier quarter-turn on the tail;
- the forward wall extension.

This separates two questions that had been conflated. Full frame transport
needs positive and negative roots. Positive cluster refactorization needs only
one positive Borel subgroup.

## First positive root

Let

\[
F=E_{21}
\]

be the jet generator, and let

\[
R=
\begin{pmatrix}
0&-1&0\\
1&0&0\\
0&0&1
\end{pmatrix}
\]

be the tail Fourier quarter-turn extended by the identity on the wall.
Conjugation gives

\[
RFR^{-1}=-E_{12}.
\]

Therefore the finite constructor

\[
X_1(a)=R\exp(-aF)R^{-1}
\]

is exactly

\[
X_1(a)=I+aE_{12}.
\]

No linear subtraction of physical operations is required. The upper shear is
obtained by composition with the source Fourier polarization exchange.

## Second positive root

Let the forward wall extension be

\[
W=E_{13}.
\]

The generators satisfy

\[
FW=E_{23},
\qquad
WF=0.
\]

Their finite group commutator is consequently

\[
\exp(aF)\exp(bW)\exp(-aF)\exp(-bW)
=I+abE_{23}.
\]

Thus

\[
X_2(ab)=I+abE_{23}
\]

is also an exact composite of source operations. Nonzero values of either
parameter cover every desired second-root coefficient over the scalar field.

This operation is not supplied by the commuting primitive and square Euler
jets. Those remain grades of one lower shear. The new direction comes from
mixing the jet capability with wall incidence.

## Source-generated braid

The two derived constructors obey the exact positive-(A_2) refactorization

\[
X_1(a)X_2(b)X_1(c)
=
X_2\!\left(\frac{bc}{a+c}\right)
X_1(a+c)
X_2\!\left(\frac{ab}{a+c}\right)
\]

whenever (a+c\ne0).

The equality is now more than an ambient matrix coincidence: both root
families have finite source-constructor words. The rational parameters are
coordinates of the alternative factorization, not new physical operations.

## What remains unproved

Finite constructor generation does not yet produce an analytic theta/Tate
coherence cell. The words contain Fourier conjugation, jet shear, wall
extension, inverses, and a group commutator. They must preserve one declared
common domain through every intermediate stage.

The outstanding checks are:

1. the wall extension and Fourier-conjugated jet shear share a finite-cutoff
   boundary carrier;
2. their inverses preserve the relevant graph domains;
3. the commutator-derived second root extends through the arithmetic
   completion;
4. the chart transition at (a+c=0) is represented without deleting a
   boundary state;
5. the distinguished theta minor transforms by the derived relative-flag
   law.

Failure of any one of these checks leaves the finite (A_2) theorem intact
but blocks its use in RH.

## Categorical consequence

The positive exchange category is generated rather than postulated:

- one arrow family is a Fourier conjugate of the jet arrow;
- the other is a commutator composite of the jet and wall arrows;
- the braid cell compares two admitted finite words;
- the fivefold cluster period belongs to the coordinate atlas of those
  words.

The missing coherencer has therefore moved. It is no longer the finite braid
identity. It is the analytic domain-and-completion lift of that identity.

## Falsifier

At each finite arithmetic cutoff, instantiate the actual jet, Fourier, and
wall operators on the declared boundary carrier. The route fails immediately
if either derived root differs from its elementary shear, if an intermediate
word leaves the domain, or if the two braid words disagree before scalar
projection.

