# Operative residue as future separation

Owner: `marici.Nima`

## Problem

A projection

\[
p:X\to Y
\]

can identify distinct upstream states.  Their difference should not be called
physical residue merely because `p` forgets it.  The difference is operative
only relative to the admissible successor family `U`.

For `x_0,x_1 in X` with `p(x_0)=p(x_1)`, define

\[
x_0\sim_{\mathcal U}x_1
\iff
u(x_0)=u(x_1)\quad\text{for every }u\in\mathcal U.
\]

The residue between the two lifts is operative exactly when

\[
p(x_0)=p(x_1)
\quad\text{but}\quad
x_0\not\sim_{\mathcal U}x_1.
\]

This is a relative Yoneda criterion: a distinction exists operationally when
some admitted future probe distinguishes it.  It does not quantify over all
mathematical maps.

## Three finite models

### Route interference

Let `X=Q^2`, `p(A,B)=A+B`, and compare `(0,0)` with `(5,-5)`.  Both display
zero.  A successor that retains the left route, `u(A,B)=A`, distinguishes
them.  If the only admitted successors factor through `p`, it cannot.

### Quantum instrument fiber

Two instruments can have the same effects and therefore the same one-use
probabilities.  A repeat-measurement successor distinguishes the QND map from
the outcome-conditioned flip map.  Their difference is operative because it
changes the distribution of later records.

### Repair quotient

If two representatives differ by a declared repair and every legal successor
descends through the quotient, no successor distinguishes them.  The hidden
difference is gauge/repair data, not an operative residue.

## Theorem schema

Let `U` be closed under legal composition and contain the declared current
readout.  The relation `~_U` is an equivalence relation.  Enlarging the
successor family can only refine its classes; restricting access can only
coarsen them.

Therefore physical distinguishability has two independent inputs:

1. the upstream state or route object;
2. the source-authorized successor family.

Neither the current readout nor the upstream object alone determines it.

## Deutsch--Popperian conjecture

A Marici coherence residue is physically meaningful exactly when it separates
future constructor possibilities within the source-authorized successor
category.  Residues invisible to every legal successor are presentation or
repair data.

## Falsifiers

- A declared operative residue has no distinguishing legal successor.
- A declared repair is distinguished by a successor that supposedly descends
  through the repair quotient.
- Adding successors merges rather than refines observational classes.
- Removing successor access refines rather than merges observational classes.

## Scope

The finite checker proves only the set-theoretic structure and three explicit
models.  It does not establish which successors are physically authorized in
any sector; that authority must come from the frozen source.

