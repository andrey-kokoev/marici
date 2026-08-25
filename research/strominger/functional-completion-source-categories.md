# Source-authorized functional completions form a strict inclusion ladder

## 1. Bundles and test spaces

Let `L^w -> S^2` denote the spin-weight `w` line bundle. Scalar hard-source
distributions live in `D'(S^2,L^0)`; shear data live in
`D'(S^2,L^2) plus D'(S^2,L^-2)`. All dualities below pair opposite spin
weights and use the round-sphere density.

Because `S^2` is compact, `C_c^infinity=C^infinity`. The smooth test space is
a nuclear Frechet space and its strong dual is the space of distributions.
This ambient dual is a representability space, not by itself an authorized
source category.

## 2. The inclusion ladder

For a finite puncture set `P`, write

\[
 \mathcal J_P^N=
 \operatorname{span}\{\partial_z^r\partial_{\bar z}^s\delta_\xi:
 \xi\in P,\ r+s\leq N\}.
\]

Then

\[
 \mathcal J_P^{\rm fin}=\underset{N}{\operatorname{colim}}\mathcal J_P^N
\]

is a strict LF space: every element has finite order, and each bounded stage
is finite dimensional. Its strong dual is the product of all formal jet
coordinates, but that product is not the source itself.

The useful global ladder is

\[
 C^\infty
 \subset H^r
 \subset L^2
 \subset L^1
 \subset \mathcal M
 \subset H^{-s}\quad(s>1)
 \subset\mathcal D',
\]

where `M` is the finite signed Radon-measure space. The inclusions involving
`H^r` are read with the appropriate nonnegative `r`; on the compact sphere,
`L^2` embeds continuously into `L^1` and hence into absolutely continuous
finite measures.

Finite atomic measures

\[
 \mathcal A_{\rm fin}=
 \left\{\sum_{i=1}^n e_i\delta_{\xi_i}:n<\infty\right\}
\]

are not a vector subspace with fixed labels, but their linear span is weak-*
dense in `M`. Countable atomic packets with `sum_i |e_i|<infinity` define
Radon measures even when punctures accumulate. Their completion retains total
variation control; arbitrary coefficientwise products do not.

## 3. Sobolev thresholds for point jets

In two angular dimensions,

\[
 \partial^\alpha\delta_\xi\in H^{-s}
 \quad\Longleftrightarrow\quad s>|\alpha|+1.
\]

Thus a fixed finite jet stage embeds into sufficiently negative Sobolev space,
but no single finite `s` contains jets of unbounded order. The LF union and a
negative-Sobolev completion are therefore incomparable as completed source
types unless an order/regularity policy is specified.

Every finite Radon measure lies in `H^{-s}` for `s>1`. The endpoint `s=1`
fails already for a delta function. Curve-supported measures have the softer
local threshold `s>1/2`, reflecting codimension one rather than two.

## 4. Wavefront-refined sectors

The ambient distribution space decomposes further by wavefront authority:

- point jets have the full nonzero cotangent fiber at each puncture;
- curve sources are conormal to their supporting curve;
- smooth hard flux has empty wavefront set;
- a proposed characteristic sector must have wavefront contained in the
  characteristic cone of the grade-three operator.

In a local real dyad, the magnetic principal symbol is proportional to

\[
 \xi_x\xi_y(\xi_x^2-\xi_y^2),
\]

so its characteristic directions are the four dyad-relative lines
`xi_x=0`, `xi_y=0`, and `xi_x=plus/minus xi_y`. Membership in a distribution
space does not show that admissible stress-energy generates wavefront on those
lines.

## 5. Authority classes

| category | mathematical status | source authority at this stage |
|---|---|---|
| finite labelled jets | constructed and previously verified | admitted |
| finite atomic measures | hard-particle source packets | admitted |
| countably atomic `l1` measures | total-variation closure of finite atomic packets | admitted atomic closure |
| all finite Radon measures | weak-* closure of finite atomic packets | candidate continuum-flux closure |
| `L2` news/flux histories | finite-energy candidate | requires time-integrated energy condition |
| negative Sobolev spaces | regularity envelope | representable, not automatically constructible |
| conormal curve distributions | extended defects/shells | requires a derived matter source |
| characteristic distributions | algebraic kernel candidates | unauthorized pending source derivation |
| full `D'` or infinite point jets | ambient carrier | not an admitted completion |

The distinction is categorical: closure in a topology preserves only limits
whose norms or seminorms remain controlled. It does not license every element
of a larger carrier containing that closure.

## 6. Consequence for the extension program

There are three different questions:

1. Does the grade-three operator have a kernel in the ambient space?
2. Does that kernel intersect a finite-energy or Radon-measure completion?
3. Is any such intersection in the image of the hard BMS source constructor?

Only a positive answer to all three produces a physical kernel class.

## Evidence

`checkers/functional_completion_source_categories_checks.py` verifies the
finite-stage dimensions, strict LF growth, point-jet Sobolev thresholds,
measure and curve thresholds, total-variation convergence of accumulating
atomic packets, and the real characteristic factorization.
