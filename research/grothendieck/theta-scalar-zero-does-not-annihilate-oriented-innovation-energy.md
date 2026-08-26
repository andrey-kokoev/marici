# Theta scalar zero does not annihilate oriented innovation energy

## Bounded question

Does a zero of the scalar Mellin readout force the reciprocal oriented energy
of the complete prime-boundary innovation tower to vanish?

## Linear readout and quadratic energy

Let

\[
\mathcal B_p=\bigoplus_{k\ge0}L^2(0,\log p)
\]

be the causal innovation space from packet 226. At a fixed spectral parameter,
the scalar Mellin readout is a linear functional

\[
\ell_s:\mathcal B_p\longrightarrow\mathbb C.
\]

The reciprocal energy is quadratic:

\[
\mathcal E_{p,s}(b)
=\sum_{k\ge1}d_k(s)\|b_k\|^2,
\]

where

\[
d_k(s)
=p^{-2\Re(s)k}-p^{-2(1-\Re(s))k}.
\]

Away from the critical seam, every (d_k(s)) has the same strict sign.
Therefore \(\mathcal E_{p,s}\) is definite on the positive-depth tower.

## Kernel obstruction

Any nonzero scalar functional on a vector space of dimension at least two has
a nontrivial kernel. Choose a nonzero positive-depth packet (b) satisfying

\[
\ell_s(b)=0.
\]

Definiteness gives

\[
\mathcal E_{p,s}(b)\ne0
\]

whenever \(\Re s\ne1/2\).

Hence there is no implication

\[
\ell_s(b)=0
\quad\Longrightarrow\quad
\mathcal E_{p,s}(b)=0
\]

on the innovation space. This is a rank obstruction: one complex scalar port
cannot annihilate a faithful quadratic energy on an infinite-dimensional
state.

## Smallest hostile packet

Take two innovation channels whose scalar readout coefficients are nonzero,
say (a_1(s)) and (a_2(s)). The packet

\[
b_1=a_2(s)v,
\qquad
b_2=-a_1(s)v
\]

for any nonzero common test vector (v) has zero scalar readout after the
obvious normalization of the two channel functionals, while

\[
\mathcal E_{p,s}(b)
=\left(d_1(s)|a_2(s)|^2+d_2(s)|a_1(s)|^2\right)\|v\|^2
\]

is strictly signed off the seam. Two channels are already enough to falsify
the proposed zero-to-energy implication.

## Consequence for the actual theta source

Partitioning the theta Mellin integral into prime windows writes its scalar
value as a coherent sum of window amplitudes. A zero says those amplitudes
cancel. It does not say that the underlying window states vanish, nor that
their squared norms cancel.

Packet 226 therefore supplies a source-derived positive orientation, but not
the zero-state bridge. The energy becomes RH-bearing only if an independently
derived operator equation converts scalar endpoint vanishing into vanishing
total boundary flux.

## Required extra law

The missing constructor must reduce the admissible zero-state space before the
scalar compression. Suitable forms include:

1. a first-order source system whose two endpoint conditions imply a Green
   flux identity;
2. a canonical Evans determinant whose zero produces a genuine boundary
   state, not merely a scalar cancellation;
3. a de Branges or canonical-system realization in which the scalar readout is
   the boundary determinant of the same positive energy system;
4. a source-derived reconstruction theorem making the scalar port jointly
   faithful with its transported descendants.

Without one of these laws, the oriented innovation energy and the scalar theta
zero remain independent observables.

## Deutschian interpretation

The causal tower explains how relationship energy is retained and why the two
valuation sectors orient it oppositely. It does not yet explain why the scalar
instrument is authorized to report a loss of that relationship. The missing
explanation is not more positivity. It is the constructor that makes scalar
nullity an executable boundary condition on the full state.

## Scope

This packet proves that scalar Mellin vanishing alone cannot annihilate the
oriented innovation energy. It does not rule out a source-derived Green or
Evans bridge, construct that bridge, or prove RH.
