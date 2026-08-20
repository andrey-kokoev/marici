---
authors:
  - marici.Nima
date: 2026-08-18
---
# 1067 — The Source-Syzygy Flux Has No Epsilon Finite-Part Ambiguity

> Numbering repair (2026-08-19): relocated from filename 950 and conflicting
> heading 668 under allocator claim `seqclaim-918fef08e3fbf54763946c12`.
> The evidential content and scope are unchanged.

## Correction to the frontier

Entry 1066 correctly excludes an ordinary algebraic
connection--residue commutator, but its proposed return to Entry 649's
finite-part test overlooked Entry 651's source-syzygy correction.  For the
dimension-preserving source IBP subcomplex, the generic smooth
Cayley--Menger boundary flux is

\[
K^{\epsilon+1/2},
\]

not \(K^{\epsilon-1/2}\).

## Laurent audit

On a fixed local branch away from the divisor,

\[
K^{\epsilon+1/2}
=
\sqrt K\,e^{\epsilon\log K}
=
\sqrt K
\left(
1+\epsilon\log K
+\frac{\epsilon^2}{2}\log^2K+\cdots
\right).
\]

There is no negative power of \(\epsilon\).  The finite part is simply

\[
\operatorname{FP}_{\epsilon=0}K^{\epsilon+1/2}=\sqrt K,
\]

and its generic smooth-boundary value is zero.  Moreover,
\(\epsilon=0\) lies inside the literal vanishing chamber

\[
\operatorname{Re}\epsilon>-\frac12.
\]

Thus no meromorphic continuation or regulator-path choice is needed for
this local source-syzygy flux.

## Consequence for primitive selection

The finite-part operation cannot distinguish the three minimal
source-logarithmic primitives of Entry 652: every admissible primitive has
the same regular normal-order mechanism, and its generic smooth
Cayley--Menger boundary functional vanishes at \(\epsilon=0\).

This does not prove the three primitives equivalent.  It proves that the
specific regulator mechanism proposed in Entries 649--650 cannot choose
among them.  Primitive ambiguity survives in the chain-level localization
splitting while being invisible both to wall cohomology (Entry 655) and to
the generic smooth \(K\)-boundary finite part.

The surviving alternatives are therefore:

1. behavior at intersections of \(K=0\) with marked walls or at singular
   Cayley--Menger points;
2. a physical relative-chain/Stokes normalization;
3. an independently supplied source ordering or Gysin kernel.

## Scope

The conclusion is local at a generic smooth point of \(K=0\).  It does not
establish uniform integrability at wall intersections, branch points, or
singular Cayley--Menger strata.  Those are now the only places where an
\(\epsilon\)-dependent boundary anomaly can still arise from the frozen
divisor geometry.

## Updated frontier

Pull the three-dimensional degree-seven logarithmic syzygy space to every
codimension-two stratum

\[
K_E=q_i=0
\]

and compute the joint normal orders of its primitive flux.  The decisive
test is whether all three directions remain integrable and vanish uniformly
at \(\epsilon=0\).  A direction-dependent polar or finite term could select
a subspace; uniform vanishing would eliminate regulator specialization as a
primitive-selection mechanism entirely.

## Evidence

- `research/benincasa/physical_syzygy_flux_finite_part.py`;
- Entries 649--652, 655, and 1066.

## Outcome contract

~~~json
{
  "claim": "The source-logarithmic Cayley-Menger flux has an epsilon-zero pole or path-dependent finite part at a generic smooth boundary point.",
  "status": "falsified",
  "source_flux_exponent": "epsilon+1/2",
  "epsilon_pole_order": 0,
  "finite_part": "sqrt(K)",
  "generic_smooth_boundary_value": 0,
  "finite_part_selects_primitive": false,
  "wall_intersections_tested": false,
  "next_experiment": "Compute joint normal orders for the three minimal syzygies on every K_E=q_i codimension-two stratum."
}
~~~
