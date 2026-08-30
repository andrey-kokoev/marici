# Holonomy bus versus a coherent eight-sector label

Owner: `marici.Kitaev`

Status: exact information/locality obstruction for the existing six-level
ancilla; charge-sensitive coherent extraction remains open.

## Bounded question

Can the clean six-level holonomy ancilla already used for element-flux ports
mediate the conditional sector generator merely by changing its phase table?

No.  Gauge invariance requires an ancilla phase function `f(h)` to satisfy

\[
f(xhx^{-1})=f(h).
\]

It is therefore a class function.  Since `S3` has three conjugacy classes, a
gauge-invariant holonomy-only bus has at most three sector signatures and
forces the collision blocks

\[
\{A,B,C\},\qquad \{D,E\},\qquad \{F,G,H\}.
\]

The target residues `(0,1,2,3,6,7,4,5)` separate every sector, including all
members within those blocks.  An element-resolved phase table can distinguish
six holonomies, but if it is not a class function it breaks gauge centrality
and does not implement the desired block-central `Z`.

## One-shot label lower bound

Suppose a clean compute--phase--uncompute gadget writes sector `a` to an
ancilla state `eta_a`, applies one ancilla-only normal phase operator, and
uncomputes.  Distinct target phases require the `eta_a` to lie in distinct
eigenspaces, hence to be mutually orthogonal.  Eight distinct sector phases
therefore require ancilla dimension at least eight.

This lower bound applies to a one-shot coherent label bus.  It does not rule
out sequential reuse of a smaller ancilla to compute several independently
derived Boolean sector predicates.  Such predicates must still be
charge-sensitive; holonomy alone cannot supply them.

## Consequence

The existing six-level bus is sufficient for flux predicates but not for a
full sector oracle.  Any lower-arity replacement for `P1 tensor Z` must add
one of:

- a charge-sensitive `D(S3)` Fourier/irrep extraction interface with at least
  eight one-shot label states; or
- a sequence of source-derived charge-sensitive binary predicates whose
  combined signatures separate all eight sectors.

Declaring either interface by its desired output would fit the answer and is
not a derivation.

## Verification and falsifiers

Run:

```text
python research/kitaev/checkers/check_s3_holonomy_bus_sector_limit.py
```

The checker enumerates all conjugation orbits, collision blocks, target
residues, and the orthogonal-eigenspace dimension bound.  Saved output:
`research/kitaev/results/s3-holonomy-bus-sector-limit.json`.

Falsifiers are a fourth conjugacy class, a class function separating any two
sectors in the same displayed block, fewer than eight eigenspaces carrying
eight distinct phases, or a source-derived sequential predicate construction
that bypasses the one-shot assumption.

