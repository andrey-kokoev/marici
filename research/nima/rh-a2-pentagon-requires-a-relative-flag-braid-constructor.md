# The RH A2 pentagon requires a relative-flag braid constructor

Author: `marici.Nima`

Date: 2026-08-26

Status: exact algebraic candidate and unresolved source-authority gate

## Correction to the single-flag picture

The six-coordinate incidence flag is the smallest carrier that retains a
primal line, a dual plane, and their coherence. It is not by itself a
five-chart cluster object.

An exchange atlas compares factorizations of relative transport between two
flags. The relevant finite carrier is therefore a moving decorated flag
relative to a reference decorated flag. On the open cell, its transport is
represented by elementary root operations in (SL(3)).

This distinction matters. The reference flag supplies ordered ports. The
moving flag supplies state. Their relative transporter supplies the
factorization that can mutate.

## Exact rank-two braid refactorization

Let

\[
x_1(a)=I+aE_{12},
\qquad
x_2(b)=I+bE_{23}.
\]

For (a+c\ne0), direct multiplication gives

\[
x_1(a)x_2(b)x_1(c)
=
x_2\!\left(\frac{bc}{a+c}\right)
x_1(a+c)
x_2\!\left(\frac{ab}{a+c}\right).
\]

This is the finite type-(A_2) braid refactorization. It does not identify
intermediate states. It says that two ordered three-stage constructor trees
have the same endpoint transporter on the open chart (a+c\ne0).

The denominator is not cosmetic. The hypersurface (a+c=0) is the chart
wall where this factorization ceases to be defined. Any theta/Tate use of the
refactorization must type that wall and provide the next chart.

## Pentagon recurrence

The coefficient shadow of the type-(A_2) exchange relation is

\[
z_{k-1}z_{k+1}=1+z_k.
\]

Starting from (z_1=a) and (z_2=b), the next three coordinates are

\[
z_3=\frac{1+b}{a},
\qquad
z_4=\frac{1+a+b}{ab},
\qquad
z_5=\frac{1+a}{b}.
\]

The recurrence then returns (z_6=a) and (z_7=b). Algebraically, this is
the five-step cluster period. It explains why a pentagon can appear after
the six-coordinate flag and the (A_2) root closure have already appeared.

## Source gate

The formulas do not yet establish a theta/Tate pentagon. They require four
source facts:

1. The two elementary root operations must be actual labelled constructors.
2. Their ordered three-stage composites must act on one common rigged domain.
3. Addition and inversion in the braid parameters must be induced by source
   composition, not fitted from the matrix identity.
4. Each chart wall must carry an authorized transition rather than being
   silently excluded.

The current programme has candidates for the two simple-root directions:
the jet shear and one wall incidence. The dual wall incidence needed to close
the full (SL(3)) action is still only a typed requirement. Consequently the
braid identity is an exact finite model, but its theta realization is not yet
constructed.

## Categorical form

The object being sought is not a cyclic permutation of five channels. It is
a groupoid of source factorizations:

- objects are decorated relative-flag charts;
- arrows are admitted elementary root constructors;
- two three-arrow paths are compared by the braid cell above;
- chart-wall arrows provide the remaining transitions;
- the fivefold coefficient period is the scalar shadow of this atlas.

This resolves the earlier count puzzle. Six coordinates describe the
primal--dual carrier. Five vertices describe presentations of relative
transport. Three is the projective dimension of one complete flag. These
numbers belong to different categorical levels.

## Decisive finite falsifier

Choose two independently source-derived elementary constructors and extract
their parameters before composing them. If their three-stage products fail
the exact braid refactorization, or if the right-hand parameters require an
unauthorized division, the source pentagon is absent even though the ambient
Lie algebra is (A_2).

The present verdict is therefore precise: the (A_2) carrier and abstract
pentagon are real, while the missing coherencer is a source-authorized
relative-flag braid constructor.

