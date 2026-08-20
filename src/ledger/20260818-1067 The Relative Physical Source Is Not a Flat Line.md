---
authors:
  - marici.Nima
date: 2026-08-18
---
# 664 — The Relative Physical Source Is Not a Flat Line

## Hard-to-vary claim

The nonzero physical source retained by Entry 663 does not span a flat
rank-one subsystem of either nineteen-dimensional occurrence block.  Its
first covariant derivatives in two independent kinematic directions are
independent of the source and of one another.

## Derived parameter connection

For a labelled form with \(K_E\)-pole level \(k\), marked pole levels
\(m_i\), and numerator \(f\), parameter differentiation is represented by

\[
(\gamma-k)f\,\partial_\xi K_E
\quad\text{at }K_E\text{-level }k+1,
\]

together with

\[
-m_i f\,\partial_\xi q_i
\quad\text{at marked level }m_i+1.
\]

These are reduced using the same chain-level relative pivots as Entry 663.
No fitted connection matrix is introduced.  Formal derivatives of the
frozen polynomial coefficients are evaluated exactly over
\(\mathbb F_{32003}\) by a degree-four-exact five-point stencil.

## First-jet result

For the constant physical source \(s\), both occurrence families give

\[
\boxed{
\dim\langle s,\nabla_xs,\nabla_ys\rangle=3.
}
\]

Thus the retained source line is not connection-stable.  This conclusion
already follows at first order and does not depend on iterated-connection
conventions.

## Frozen connection-algebra closure

At the tested kinematic point, repeatedly closing under the two induced
connection endomorphisms spans the full relative block:

\[
\dim\operatorname{Sat}_{\nabla_x,\nabla_y}(s)=19.
\]

This holds for both reflected partners at Kummer weight five and for the
\(q_{g_{23}}\) partner at weight seven.  The number nineteen is a frozen
connection-algebra saturation.  It is not asserted to equal the rank of the
full differential-module orbit, because higher covariant jets also contain
derivatives of the connection coefficients.  The rank-three first jet is
the convention-independent obstruction needed here.

## Consequence

Relative-before-absolute reduction successfully preserves the physical
source, but it does not isolate the desired small coefficient object.  A
rank-one algebraic or regulator line cannot be obtained by declaring the
source itself to be horizontal.  Any small physical subsystem must use
additional structure that cancels or projects its two transverse first
derivatives—most naturally the unsplit reflected pair, its boundary
homotopy, or physical-chain/Gysin data.

This narrows the rank-thirty-five frontier:

\[
\boxed{
\text{the first possible cancellation is between the two reflected
occurrence derivatives, not within either occurrence alone.}
}
\]

## Updated frontier

Construct the common chain-level target for the \(q_{g_{23}}\) and
\(q_{g_{31}}\) relative blocks, retaining their shared three-wall labels.
Map the unsplit source sum into that target and test whether its two
transverse first derivatives cancel, coincide, or generate a genuinely
larger subspace.

## Evidence

- `research/benincasa/physical_four_mark_residue_twisted_derham.py`;
- Entries 658--663.

## Outcome contract

~~~json
{
  "claim": "The physical source retained by the chain-level relative quotient spans a flat line in a single occurrence block.",
  "status": "falsified",
  "relative_block_dimension": 19,
  "source_first_jet_rank": 3,
  "frozen_connection_algebra_saturation_rank": 19,
  "full_differential_module_rank_claimed": false,
  "replications": [
    {"partner": "q_g23", "gamma": 5},
    {"partner": "q_g31", "gamma": 5},
    {"partner": "q_g23", "gamma": 7}
  ],
  "next_experiment": "Test first-derivative cancellation for the unsplit reflected source in a common chain-level target."
}
~~~
